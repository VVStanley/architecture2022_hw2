from src.commands.iterator import CommandCollection
from src.design_patterns.command import CommandInterface
from src.exceptions.command import (
    BaseCommandExceptionError,
    MoveBurnFuelCommandError, RotateBurnFuelCommandError,
)
from src.fuel.fuel import BurnFuelCommand, CheckFuelCommand
from src.fuel.fueled import Fueled
from src.move.movable import Movable
from src.move.move import MoveCommand
from src.rotate.rotable import Rotable
from src.rotate.rotate import RotateCommand
from src.units.unit import Unit


class MoveBurnFuelCommand(CommandInterface):
    """Команда движения с расходом топлива"""

    def __init__(self, unit: Unit) -> None:
        """Инициализация

        :param unit: объект для передвижения
        """
        self.collection = CommandCollection()
        self.collection.add_item(CheckFuelCommand(Fueled(unit=unit)))
        self.collection.add_item(MoveCommand(Movable(unit=unit)))
        self.collection.add_item(BurnFuelCommand(Fueled(unit=unit)))

    def execute(self) -> None:
        """Выполняем движение с расходом топлива"""
        for command in self.collection:
            try:
                command.execute()
            except BaseCommandExceptionError as e:
                raise MoveBurnFuelCommandError(str(e))


class RotateBurnFuelCommand(CommandInterface):
    """Поворот с расходом топлива"""

    def __init__(self, unit: Unit) -> None:
        """Инициализация

        :param unit: объект для поворота
        """
        self.collection = CommandCollection()
        self.collection.add_item(CheckFuelCommand(Fueled(unit=unit)))
        self.collection.add_item(RotateCommand(Rotable(unit=unit)))
        self.collection.add_item(BurnFuelCommand(Fueled(unit=unit)))

    def execute(self) -> None:
        """Выполняем поворот с расходом топлива"""
        for command in self.collection:
            try:
                command.execute()
            except BaseCommandExceptionError as e:
                raise RotateBurnFuelCommandError(str(e))
