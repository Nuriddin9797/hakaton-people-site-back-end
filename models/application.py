from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, String, Integer, Boolean
from models.cart import Carts
from models.users import Users


class Application(Base):
    __tablename__ = 'application'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    phone_number = Column(String(255), nullable=False)
    gmail = Column(String(255), nullable=False)
    status = Column(Boolean, nullable=False)
    carts_id = Column(Integer, nullable=False)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Application.user_id)

    carts = relationship("Carts", foreign_keys=[carts_id],
                         primaryjoin=lambda: Carts.id == Application.carts_id)