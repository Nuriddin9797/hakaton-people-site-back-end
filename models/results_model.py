from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from models.answers_model import Answers
from models.categories_model import Categories
from models.questions_model import Question


class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)
    answer_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    questions = relationship("Question", foreign_keys=[question_id],
                            primaryjoin=lambda: Question.id == Result.question_id)

    categories = relationship('Categories', foreign_keys=[category_id],
                              primaryjoin=lambda: Categories.id == Result.category_id)

    answers = relationship("Answers", foreign_keys=[answer_id],
                            primaryjoin=lambda: Answers.id == Result.answer_id)