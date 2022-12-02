from fastapi import FastAPI
from app.routers.core.healthcheck import healthcheck_router
from app.routers.core.insert_data import insert_data_router
from app.routers.core.search import search_router

app = FastAPI(title="Candidates Discovery")
app.include_router(insert_data_router)
app.include_router(healthcheck_router)
app.include_router(search_router)
