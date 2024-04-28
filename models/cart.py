from sqlalchemy.orm import relationship, backref
from db import Base
from sqlalchemy import Column, String, Integer, and_, Boolean
from models.design import Design
from models.programming import Programming
from models.trading import Trading


class Carts(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    source = Column(String(255), nullable=False)
    source_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=True)

    programming = relationship("Programming", foreign_keys=[source_id],
                               primaryjoin=lambda: and_(Programming.id == Carts.source_id,
                                                        Carts.source == "programming"),
                               backref=backref("carts"))

    trading = relationship("Trading", foreign_keys=[source_id],
                           primaryjoin=lambda: and_(Trading.id == Carts.source_id, Carts.source == "trading"),
                           backref=backref("carts"))

    design = relationship("Design", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Design.id == Carts.source_id, Carts.source == "design"),
                          backref=backref("carts"))