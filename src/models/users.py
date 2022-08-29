from typing import Any

from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int
    fight: Any

    class Config:
        orm_mode = True
