from pydantic import BaseModel


class create_myanswer(BaseModel):
    answer: str
    t_javob: bool
    question_id: int


class update_myanswer(BaseModel):
    ident: int
    answer: str
    t_javob: bool
    question_id: int
