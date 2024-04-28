from pydantic import BaseModel, Field


class CreateProgramming(BaseModel):
    name: str
    experience: str
    skills: str
    level: str
    jobs_id: int = Field(..., gt=0)


class UpdateProgramming(BaseModel):
    ident: int
    name: str
    experience: str
    skills: str
    level: str