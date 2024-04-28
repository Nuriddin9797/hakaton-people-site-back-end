from db import Base
from sqlalchemy import Column, String, Integer


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    skills = Column(String(255))
    level = Column(String(255))
    role = Column(String(255))
    token = Column(String(255), nullable=True)
