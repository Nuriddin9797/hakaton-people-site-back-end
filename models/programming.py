from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, String, Integer
from models.jobs import Jobs


class Programming(Base):
    __tablename__ = 'programming'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    experience = Column(String, nullable=False)
    skills = Column(String(255), nullable=False)
    level = Column(String(255), nullable=True)
    see_num = Column(Integer, nullable=False)
    jobs_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(String(255), nullable=False)

    jobs = relationship("Jobs", foreign_keys=[jobs_id],
                        primaryjoin=lambda: Jobs.id == Programming.jobs_id)