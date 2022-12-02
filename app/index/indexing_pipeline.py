from app.core.adapters.weaiate import Weaviate
from .dataloader import Data
from app.configs.constants import CANDIDATE_FEATURES
from app.index.vector_encoder import model as vector_encoder
import uuid
class Pipeline:
    """
    This class implements the insertion pipeline end-to-end
    """
    def create_schema(self,waviate_client):
        """
        Creates schema for the Candidate Class
        :param waviate_client: the waviate client
        :return: None
        """
        schema = {
            "class": "Candidate",
                "description": "Linkedin Profile for a Candidate",
            "moduleConfig": {
                "text2vec-huggingface": {
                    "model": "sentence-transformers/multi-qa-MiniLM-L6-cos-v1",
                    "options": {
                        "waitForModel": True,
                        "useGPU": True,
                        "useCache": True
                    }
                }
            },
                "properties": [
                    {
                        "dataType": [
                            "string"
                        ],
                        "description": "",
                        "name": f"{property}",
                    }

                    for property in CANDIDATE_FEATURES.keys()
                ]
        }
        print("Creating the schema")
        try:
            waviate_client.schema.create_class(schema)
            print("Created the schema")
            return 0
        except Exception as e:
            print(e)
            print("Could not create the schema",e)
            return -1


    def run(self,filename):
        """
        Implemets flow of the Insertion pipeline
        :return: 0 or None
        """
        candidates = Data().load_json(filename)
        #Check if there exists a candidate schema already
        weaviate_client = Weaviate().connect_weaviate()
        try:
            schema = weaviate_client.schema.get()
        except:
            raise Exception("Schema cannote be retrieved")

        found = False
        for class_ in schema["classes"]:
            if class_["class"] == "Candidate":
                found = True
                break

        if not found:
            print("Schema not found, creating new")
            if self.create_schema(weaviate_client) != 0:
                raise Exception("Could not create schema")
        with weaviate_client.batch as batch:
            for candidate in candidates:
                encoded_candidate = self.encode_candidate(candidate)
                vector = vector_encoder.encode(encoded_candidate['about'])
                print(encoded_candidate,vector)
                status = weaviate_client.batch.add_data_object(encoded_candidate,"Candidate",uuid.uuid4(),vector)
                print(status)
                break
        return 0

    def encode_candidate(self, candidate):
        """

        :param candidate: Returns dictionary of the candidate in desired format, see format at https://1drv.ms/t/s!ApHIlj0tULb4qyAVSLnv8p2UU3Si?e=uktF2Z
        :return:
        """
        encoded_candidate = {}
        for feature_id,feature_values in candidate.items():
            # Filter out features that are not required to be indexed
            if feature_id in CANDIDATE_FEATURES.keys():
                if isinstance(CANDIDATE_FEATURES[feature_id], str):
                    encoded_candidate[feature_id] = str(candidate[feature_id])
                # When feature can contain multiple values, like a cnadidate can have more than one job experiences
                elif isinstance(CANDIDATE_FEATURES[feature_id], list):
                    encoded_candidate[feature_id] = ''
                    for feature_detail in feature_values:
                        for element_to_select in CANDIDATE_FEATURES[feature_id]:
                            if isinstance(CANDIDATE_FEATURES[feature_id][0],str):
                                encoded_candidate[feature_id] += ", "+str(feature_detail[element_to_select])
                            else:
                                for top_level_element,element_to_select in CANDIDATE_FEATURES[feature_id][0].items():
                                    for feature_detail_refined in feature_detail[top_level_element]:
                                        encoded_candidate[feature_id] += ", "+str(feature_detail_refined[element_to_select])
                elif isinstance(CANDIDATE_FEATURES[feature_id],dict): # Current company is a dictionary
                    element_to_select = list(CANDIDATE_FEATURES[feature_id].keys())[0]
                    encoded_candidate[feature_id] = feature_values[element_to_select]

        return encoded_candidate