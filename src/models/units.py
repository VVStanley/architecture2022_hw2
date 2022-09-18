from typing import Any

from pydantic import BaseModel


class Vector(BaseModel):
    x: int
    y: int

    class Config:
        orm_mode = True


class Unit(BaseModel):
    id: int
    AMOUNT: int
    name: str

    class Config:
        orm_mode = True


class Wall(Unit):
    position: Vector


class Tower(Unit):
    position: Vector
    direction: int
    angular_velocity: int
    direction_numbers: int
    bullets: int


class Ship(Unit):
    position: Vector
    remaining_fuel: int
    consumption_fuel: int
    direction: int
    angular_velocity: int
    direction_numbers: int
    velocity: int
    bullets: int


def get_model_by_name(name: str) -> Any:
    models = {
        'wall': Wall,
        'tower': Tower,
        'ship': Ship,
    }
    return models.get(name, Unit)
