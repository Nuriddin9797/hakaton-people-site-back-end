from pydantic import BaseModel


class Create_Application(BaseModel):
    phone_number: str
    gmail: str
    carts_id: int


class Update_Application(BaseModel):
    status: bool

