from typing import List
from unittest.mock import MagicMock, Mock

import pytest

from src.design_patterns.command import CommandInterface
from src.fuel import BurnFuel, CheckFuel
from src.move import Move
from src.rotate import Rotate
from src.vector import Vector


@pytest.fixture
def rotate_command() -> CommandInterface:
    rotable = Mock()
    rotable.get_direction = MagicMock(return_value=3)
    rotable.get_angular_velocity = MagicMock(return_value=2)
    rotable.get_direction_number = MagicMock(return_value=8)
    return Rotate(rotable)


@pytest.fixture
def move_command() -> CommandInterface:
    movable = Mock()
    movable.get_position = MagicMock(return_value=Vector(12, 5))
    movable.get_velocity = MagicMock(return_value=Vector(-7, 3))
    return Move(movable)


@pytest.fixture
def burn_fuel_command() -> CommandInterface:
    fueled = Mock()
    fueled.get_remaining_fuel = MagicMock(return_value=300)
    fueled.get_fuel_consumption = MagicMock(return_value=2)
    return BurnFuel(fueled)


@pytest.fixture
def check_fuel_command() -> CommandInterface:
    fueled = Mock()
    fueled.get_remaining_fuel = MagicMock(return_value=25)
    return CheckFuel(fueled)


@pytest.fixture
def check_fuel_command_with_exception() -> CommandInterface:
    fueled = Mock()
    fueled.get_remaining_fuel = MagicMock(return_value=0)
    return CheckFuel(fueled)


@pytest.fixture
def get_exception_commands(
    rotate_command: Mock,
    move_command: Mock,
    burn_fuel_command: Mock,
    check_fuel_command_with_exception: Mock
) -> List[CommandInterface]:
    return [
        move_command, burn_fuel_command, check_fuel_command_with_exception,
        rotate_command, burn_fuel_command, check_fuel_command_with_exception,
    ]


@pytest.fixture
def get_execute_commands(
    rotate_command: Mock,
    move_command: Mock,
    burn_fuel_command: Mock,
    check_fuel_command: Mock
) -> List[CommandInterface]:
    return [
        move_command, burn_fuel_command, check_fuel_command,
        rotate_command, burn_fuel_command, check_fuel_command,
        move_command, burn_fuel_command, check_fuel_command,
        move_command, burn_fuel_command, check_fuel_command,
        move_command, burn_fuel_command, check_fuel_command,
        rotate_command, burn_fuel_command, check_fuel_command,
        move_command, burn_fuel_command, check_fuel_command,
    ]
