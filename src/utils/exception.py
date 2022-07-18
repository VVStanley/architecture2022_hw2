from src.commands.moves import MoveBurnFuelCommand, RotateBurnFuelCommand
from src.fuel.fuel import CheckFuelCommand
from src.move.move import MoveCommand
from src.rotate.rotate import RotateCommand

handle_exception = {
    'RotateCommandError': RotateCommand,
    'MoveCommandError': MoveCommand,
    'CheckFuelCommandError': CheckFuelCommand,
    'MoveBurnFuelCommandError': MoveBurnFuelCommand,
    'RotateBurnFuelCommandError': RotateBurnFuelCommand,
}


def can_handle(exception_name: str) -> bool:
    """Проверяем есть ли исключенрие в хеш таблице handle_exception"""
    return True if exception_name in handle_exception else False
