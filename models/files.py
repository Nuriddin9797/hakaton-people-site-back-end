from db import Base
from sqlalchemy import Column, String, Integer, and_, Text
from sqlalchemy.orm import relationship, backref

from models.application import Application
from models.design import Design
from models.programming import Programming
from models.support import Support
from models.trading import Trading
from models.users import Users


class Files(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(255), nullable=False)
    source_id = Column(Integer, nullable=False)
    file = Column(String(255), nullable=False)

    users = relationship("Users", foreign_keys=[source_id],
                               primaryjoin=lambda: and_(Users.id == Files.source_id, Files.source == "users"),
                               backref=backref("files"))

    programming = relationship("Programming", foreign_keys=[source_id],
                               primaryjoin=lambda: and_(Programming.id == Files.source_id, Files.source == "programming"),
                               backref=backref("files"))

    trading = relationship("Trading", foreign_keys=[source_id],
                           primaryjoin=lambda: and_(Trading.id == Files.source_id, Files.source == "trading"),
                           backref=backref("files"))

    design = relationship("Design", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Design.id == Files.source_id, Files.source == "design"),
                          backref=backref("files"))

    support = relationship("Support", foreign_keys=[source_id],
                          primaryjoin=lambda: and_(Support.id == Files.source_id, Files.source == "support"),
                          backref=backref("files"))
    application = relationship("Application", foreign_keys=[source_id],
                         primaryjoin=lambda: and_(Application.id == Files.source_id, Files.source == "application"),
                         backref=backref("files"))
