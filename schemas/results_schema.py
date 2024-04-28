from pydantic import BaseModel


class create_myresult(BaseModel):
    question_id: int
    category_id: int
    answer_id: int


class update_myresult(BaseModel):
    ident: int
    question_id: int
    category_id: int
    answer_id: int
