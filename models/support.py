from sqlalchemy.orm import backref, relationship
from db import Base
from sqlalchemy import Column, String, Integer, and_, Boolean
from models.programming import Programming
from models.design import Design
from models.trading import Trading
from models.users import Users


class Support(Base):
    __tablename__ = 'support'
    id = Column(Integer, primary_key=True, autoincrement=True)
    file = Column(String(255), nullable=False)

