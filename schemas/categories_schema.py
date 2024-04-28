from pydantic import BaseModel


class create_mycategories(BaseModel):
    name: str


class update_mycategories(BaseModel):
    ident: int
    name: str
