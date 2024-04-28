from pydantic import BaseModel, Field


class CreateJobs(BaseModel):
    name: str


class UpdateJobs(BaseModel):
    name: str
