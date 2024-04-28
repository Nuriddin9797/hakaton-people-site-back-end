from sqlalchemy.orm import relationship, joinedload
from models.questions_model import Question
from db import Base
from sqlalchemy import Column, String, Integer, Boolean


class Answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    answer = Column(String(255), nullable=False)
    t_javob = Column(Boolean, nullable=False)
    question_id = Column(Integer, nullable=False)

    question = relationship("Question", foreign_keys=[question_id],
                              primaryjoin=lambda: Question.id == Answers.question_id)