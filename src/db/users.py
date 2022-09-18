from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, index=True, nullable=True)
    password_hash = Column(String, nullable=False)

    ready_to_fight = Column(Boolean, default=False)

    fight_id = Column(String, ForeignKey('fights.id'), index=True)
    fight = relationship('Fight', backref='get_users')
