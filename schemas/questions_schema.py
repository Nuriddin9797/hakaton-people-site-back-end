from pydantic import BaseModel

class create_myquestion(BaseModel):
    question: str
    categoriya_id: int
class update_myquestion(BaseModel):
    ident: int
    question: str
    categoriya_id: int