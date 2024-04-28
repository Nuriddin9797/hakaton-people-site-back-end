from sqlalchemy.orm import relationship
from models.categories_model import Categories
from db import Base
from sqlalchemy import Column, String, Integer


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String(255), nullable=False)
    categoriya_id = Column(Integer, nullable=False)

    categories = relationship("Categories", foreign_keys=[categoriya_id],
                              primaryjoin=lambda: Categories.id == Question.categoriya_id)
