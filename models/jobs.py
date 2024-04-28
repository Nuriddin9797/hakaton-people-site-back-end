from db import Base
from sqlalchemy import Column, String, Integer


class Jobs(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
