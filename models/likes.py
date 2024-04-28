from sqlalchemy.orm import backref, relationship
from db import Base
from sqlalchemy import Column, String, Integer, and_, Boolean
from models.programming import Programming
from models.design import Design
from models.trading import Trading
from models.users import Users


class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    source = Column(String(255), nullable=False)
    source_id = Column(Integer, nullable=False)

    user = relationship("Users", foreign_keys=[user_id],
                        primaryjoin=lambda: Users.id == Likes.user_id)

    programming = relationship("Programming", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Programming.id == Likes.source_id, Likes.source == "programming"),
                          backref=backref("likes"))

    trading = relationship("Trading", foreign_keys=[source_id],
                             primaryjoin=lambda: and_(Trading.id == Likes.source_id, Likes.source == "trading"),
                             backref=backref("likes"))

    design = relationship("Design", foreign_keys=[source_id],
                             primaryjoin=lambda: and_(Design.id == Likes.source_id, Likes.source == "design"),
                             backref=backref("likes"))
