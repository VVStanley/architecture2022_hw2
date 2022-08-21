from enum import Enum
from typing import List

from src.injector.fields import AutoIncrementField, AutoVectorField


class TechnicalArguments(Enum):
    AMOUNT = "amount"


scope = {
    "units": [
        {
            TechnicalArguments.AMOUNT: 3,
            "id": AutoIncrementField(),
            "name": "wall",
            "position": AutoVectorField()
        },
        {
            TechnicalArguments.AMOUNT: 5,
            "id": AutoIncrementField(),
            "name": "tower",
            "position": AutoVectorField(),
            "direction": 7,
            "angular_velocity": 1,
            "direction_numbers": 8,
        },
        {
            TechnicalArguments.AMOUNT: 4,
            "id": AutoIncrementField(),
            "name": "ship",
            "remaining_fuel": 15,
            "consumption_fuel": 3,
            "position": AutoVectorField(),
            "direction": 7,
            "angular_velocity": 1,
            "direction_numbers": 8,
            "velocity": 9
        }
    ],
}


def get_scope(name_scope: str) -> List[dict]:
    """Возвращаем настройки для игры"""
    return scope.get(name_scope, {})
