from pydantic import BaseModel

from models import User


class Fight(BaseModel):
    id: int
    token: str
    users: User
