from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base


class Fight(Base):
    __tablename__ = 'fights'

    id = Column(Integer, primary_key=True, index=True)
    start = Column(DateTime(timezone=False), server_default=func.now())


class FightHistory(Base):
    __tablename__ = 'fight_history'

    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime(timezone=False), server_default=func.now())

    fight_id = Column(Integer, ForeignKey('fights.id'), index=True)
    fight = relationship('Fight', backref='users')
