from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer, Numeric


class Income(Base):
    __tablename__ = 'income'
    id = Column(Integer, primary_key=True, autoincrement=True)
    total_price = Column(Numeric, nullable=False, default=0)
    programming_price = Column(Numeric, nullable=False, default=0)
    design_price = Column(Numeric, nullable=False, default=0)
    trading_price = Column(Numeric, nullable=False)
