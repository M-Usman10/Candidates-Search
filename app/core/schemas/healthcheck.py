from datetime import datetime, timezone
from pydantic import Field, BaseModel


class HealthCheckResponse(BaseModel):
    status: str = Field(
        default="test-weaviate server is up",
        example="test-weaviate server is up",
    )
    timestamp: datetime

    class Config:
        json_encoders = {
            datetime: lambda dt: dt.replace(
                microsecond=0, tzinfo=timezone.utc
            ).isoformat()
        }
