from app.configs.constants import CONFIG
import ndjson
import os

class Data:
    def __init__(self):
        self.path = CONFIG["DATA_PATH"]

    def load_json(self,filename):
        with open(os.path.join(self.path,filename)) as file:
            return ndjson.load(file)