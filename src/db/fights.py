from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.database import Base


class Fight(Base):
    __tablename__ = 'fights'

    id = Column(String(32), primary_key=True, index=True)
    start = Column(DateTime(timezone=False), server_default=func.now())
    token = Column(String(500), server_default="")


class FightHistory(Base):
    __tablename__ = 'fight_history'

    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime(timezone=False), server_default=func.now())

    fight_id = Column(String, ForeignKey('fights.id'), index=True)
    fight = relationship('Fight', backref='get_history')
