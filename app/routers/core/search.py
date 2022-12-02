from fastapi import APIRouter
from sympy.physics.quantum import operator

from app.core.adapters.weaiate import Weaviate
from app.configs.constants import CANDIDATE_FEATURES

search_router = APIRouter()

@search_router.post("/search", response_model=dict)
def search_db(query: dict):
    client = Weaviate().connect_weaviate()
    #.with_near_text(near_text_filter)
    client = client.query.get("candidate", list(CANDIDATE_FEATURES))
    for key, value in query.items():
        filter = {
            "path": key,
            "operator": "Like",
            "valueString": value
        }
        print(filter)
        client=client.with_where(filter)
    results = client.do()
    return results
