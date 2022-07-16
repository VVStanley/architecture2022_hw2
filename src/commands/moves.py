from src.commands.iterator import CommandCollection
from src.design_patterns.command import CommandInterface
from src.exceptions import CommandExceptionError
from src.fuel.fuel import BurnFuelCommand, CheckFuelCommand
from src.fuel.fueled import Fueled
from src.move.movable import Movable
from src.move.move import MoveCommand
from src.units.unit import Unit


class MoveBurnFuelCommand(CommandInterface):
    """Команда движения с расходом топлива"""

    def __init__(self, unit: Unit) -> None:
        self.collection = CommandCollection()
        self.collection.add_item(CheckFuelCommand(Fueled(unit=unit)))
        self.collection.add_item(MoveCommand(Movable(unit=unit)))
        self.collection.add_item(BurnFuelCommand(Fueled(unit=unit)))

    def execute(self) -> None:
        """Выполняем движение с расходом топлива"""
        for command in self.collection:
            try:
                command.execute()
            except Exception as e:
                raise CommandExceptionError(f"Stop unit with error: {e}")
