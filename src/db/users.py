from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, index=True, nullable=True)
    password_hash = Column(String, nullable=False)

    ready_to_fight = Column(Boolean, default=False)

    fight_id = Column(Integer, ForeignKey('fights.id'), index=True)
    fight = relationship('Fight', backref='users')
