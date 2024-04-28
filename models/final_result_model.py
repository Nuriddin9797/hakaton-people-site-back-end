from sqlalchemy.orm import relationship
from db import Base
from models.users import Users
from sqlalchemy import Column, Integer


class Final_Result(Base):
    __tablename__ = 'final_result'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hamma_savollar = Column(Integer, nullable=False)
    t_javoblar = Column(Integer, nullable=False)
    foiz = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    user = relationship('Users', foreign_keys=[user_id],
                              primaryjoin=lambda: Users.id == Final_Result.user_id)

