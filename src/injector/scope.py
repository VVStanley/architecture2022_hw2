from enum import Enum
from random import randint
from typing import Any, Dict, List, Union

from src.injector.fields import AutoIncrementField, AutoVectorField


class TechnicalArguments(Enum):
    AMOUNT = "amount"


def get_scope(
    amount_ship: int
) -> List[Dict[Union[str, TechnicalArguments], Any]]:
    """Возвращаем настройки для игры"""
    return [
        {
            TechnicalArguments.AMOUNT.name: randint(2, 6),
            "id": AutoIncrementField(),
            "name": "wall",
            "position": AutoVectorField()
        },
        {
            TechnicalArguments.AMOUNT.name: randint(1, 3),
            "id": AutoIncrementField(),
            "name": "tower",
            "position": AutoVectorField(),
            "direction": 7,
            "angular_velocity": 1,
            "direction_numbers": 8,
        },
        {
            TechnicalArguments.AMOUNT.name: amount_ship,
            "id": AutoIncrementField(),
            "name": "ship",
            "remaining_fuel": 500,
            "consumption_fuel": 2,
            "position": AutoVectorField(),
            "direction": 7,
            "angular_velocity": 1,
            "direction_numbers": 8,
            "velocity": 9,
            "bullets": 500
        }
    ]
