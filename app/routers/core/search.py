from fastapi import APIRouter
from app.core.adapters.weaiate import Weaviate
from app.configs.constants import CANDIDATE_FEATURES

search_router = APIRouter()

@search_router.post("/search", response_model=dict)
def search_db(near_text_filter: dict):
    client = Weaviate().connect_weaviate()
    #.with_near_text(near_text_filter)
    results = client.query.get("candidate",list(CANDIDATE_FEATURES)).do()
    return results
