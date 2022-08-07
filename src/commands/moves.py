from src.commands.iterator import CommandCollection
from src.design_patterns.command import CommandInterface
from src.exceptions.command import (
    BaseCommandExceptionError,
    MoveBurnFuelCommandError, RotateBurnFuelCommandError,
)
from src.injector import container


class MoveBurnFuelCommand(CommandInterface):
    """Команда движения с расходом топлива"""

    def __init__(self) -> None:
        """Инициализация"""
        self.collection = CommandCollection()
        self.collection.add_item(container.resolve("CheckFuelCommand"))
        self.collection.add_item(container.resolve("MoveCommand"))
        self.collection.add_item(container.resolve("BurnFuelCommand"))

    def execute(self) -> None:
        """Выполняем движение с расходом топлива"""
        for command in self.collection:
            try:
                command.execute()
            except BaseCommandExceptionError as e:
                raise MoveBurnFuelCommandError(str(e))


class RotateBurnFuelCommand(CommandInterface):
    """Поворот с расходом топлива"""

    def __init__(self) -> None:
        """Инициализация"""
        self.collection = CommandCollection()
        self.collection.add_item(container.resolve("CheckFuelCommand"))
        self.collection.add_item(container.resolve("RotateCommand"))
        self.collection.add_item(container.resolve("BurnFuelCommand"))

    def execute(self) -> None:
        """Выполняем поворот с расходом топлива"""
        for command in self.collection:
            try:
                command.execute()
            except BaseCommandExceptionError as e:
                raise RotateBurnFuelCommandError(str(e))
