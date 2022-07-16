from typing import List
from unittest.mock import MagicMock, Mock

import pytest

from src.commands.iterator import CommandCollection
from src.design_patterns.command import CommandInterface
from src.fuel.fuel import BurnFuelCommand, CheckFuelCommand
from src.move.move import MoveCommand
from src.rotate.rotate import RotateCommand
from src.start import create_unit
from src.units.unit import Unit
from src.vector import Vector


@pytest.fixture
def unit_space_ship() -> Unit:
    """Возвращаем боевой корабль"""
    return create_unit(
        remaining_fuel=5,
        consumption_fuel=2,
        position=Vector(1, 1),
        direction=1,
        directions_number=1,
        velocity=1,
    )


@pytest.fixture
def rotate_command() -> CommandInterface:
    rotable = Mock()
    rotable.get_direction = MagicMock(return_value=3)
    rotable.get_angular_velocity = MagicMock(return_value=2)
    rotable.get_direction_number = MagicMock(return_value=8)
    return RotateCommand(rotable)


@pytest.fixture
def move_command() -> CommandInterface:
    movable = Mock()
    movable.get_position = MagicMock(return_value=Vector(12, 5))
    movable.get_velocity = MagicMock(return_value=Vector(-7, 3))
    return MoveCommand(movable)


@pytest.fixture
def burn_fuel_command() -> CommandInterface:
    fueled = Mock()
    fueled.get_remaining_fuel = MagicMock(return_value=300)
    fueled.get_consumption_fuel = MagicMock(return_value=2)
    return BurnFuelCommand(fueled)


@pytest.fixture
def check_fuel_command() -> CommandInterface:
    fueled = Mock()
    fueled.get_remaining_fuel = MagicMock(return_value=25)
    return CheckFuelCommand(fueled)


@pytest.fixture
def check_fuel_command_with_exception() -> CommandInterface:
    fueled = Mock()
    fueled.get_remaining_fuel = MagicMock(return_value=0)
    return CheckFuelCommand(fueled)


@pytest.fixture
def get_exception_commands(
    rotate_command: Mock,
    check_fuel_command: Mock,
    move_command: Mock,
    burn_fuel_command: Mock,
    check_fuel_command_with_exception: Mock
) -> CommandCollection:
    collection = CommandCollection()
    collection.add_item(check_fuel_command)
    collection.add_item(move_command)
    collection.add_item(burn_fuel_command)
    collection.add_item(check_fuel_command_with_exception)
    collection.add_item(move_command)
    collection.add_item(burn_fuel_command)
    return collection


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
