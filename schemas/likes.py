from enum import Enum
from pydantic import BaseModel, Field


class Source_type(str, Enum):
    programming = "programming"
    design = "design"
    trading = "trading"


class CreateLikes(BaseModel):
    source: Source_type
    source_id: int = Field(..., gt=0)
