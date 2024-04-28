from pydantic import BaseModel, Field


class CreateDesign(BaseModel):
    experience: str
    skills: str
    level: str
    jobs_id: int = Field(..., gt=0)


class UpdateDesign(BaseModel):
    experience: str
    skills: str
    level: str
