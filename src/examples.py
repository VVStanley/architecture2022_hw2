from src.commands.iterator import CommandCollection
from src.commands.macro_commands import MacroCommand
from src.fuel.fuel import BurnFuelCommand, CheckFuelCommand
from src.fuel.fueled import Fueled
from src.move.movable import Movable
from src.move.move import MoveCommand
from src.units.unit import Unit


def move_and_burn_fuel(unit: Unit) -> None:
    """Тест"""
    collection = CommandCollection()
    collection.add_item(CheckFuelCommand(Fueled(unit=unit)))
    collection.add_item(MoveCommand(Movable(unit=unit)))
    collection.add_item(BurnFuelCommand(Fueled(unit=unit)))
    command = MacroCommand(collection)
    command.execute()
