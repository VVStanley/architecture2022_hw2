from typing import Any

from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str


class UserCreate(BaseUser):
    password: str


class Fighter(BaseUser):
    id: int
    ready_to_fight: bool

    class Config:
        orm_mode = True


class User(BaseUser):
    id: int
    fight: Any
    ready_to_fight: bool

    class Config:
        orm_mode = True
