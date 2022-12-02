from fastapi import APIRouter
from app.core.schemas.healthcheck import HealthCheckResponse

from datetime import datetime

healthcheck_router = APIRouter()


@healthcheck_router.get("/healthcheck", response_model=HealthCheckResponse)
def check_health():
    return HealthCheckResponse(timestamp=datetime.now())
