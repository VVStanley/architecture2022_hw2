from src.commands.iterator import CommandCollection
from src.design_patterns.command import CommandInterface
from src.exceptions.command import (
    BaseCommandExceptionError,
    MoveBurnFuelCommandError, RotateBurnFuelCommandError,
    ShootCheckBulletCommandError,
)
from src.injector import container


class ShootCheckBulletCommand(CommandInterface):
    """Макрокоманда для выстрела"""

    def __init__(self, fight_id: str, obj_id: int) -> None:
        """Инициализация"""
        self.collection = CommandCollection()
        self.collection.add_item(
            container.resolve("CheckBulletsCommand", fight_id, obj_id)
        )
        self.collection.add_item(
            container.resolve("ShootCommand", fight_id, obj_id)
        )

    def execute(self) -> None:
        """Выполняем движение с расходом топлива"""
        for command in self.collection:
            try:
                command.execute()
            except BaseCommandExceptionError as e:
                break
                # raise ShootCheckBulletCommandError(str(e))


class MoveBurnFuelCommand(CommandInterface):
    """Макрокоманда движения с расходом топлива"""

    def __init__(self, fight_id: str, obj_id: int) -> None:
        """Инициализация"""
        self.collection = CommandCollection()
        self.collection.add_item(
            container.resolve("CheckFuelCommand", fight_id, obj_id)
        )
        self.collection.add_item(
            container.resolve("MoveCommand", fight_id, obj_id)
        )
        self.collection.add_item(
            container.resolve("BurnFuelCommand", fight_id, obj_id)
        )

    def execute(self) -> None:
        """Выполняем движение с расходом топлива"""
        for command in self.collection:
            try:
                command.execute()
            except BaseCommandExceptionError as e:
                break
                # raise MoveBurnFuelCommandError(str(e))


class RotateBurnFuelCommand(CommandInterface):
    """Макрокоманда для поворота с расходом топлива"""

    def __init__(self, fight_id: str, obj_id: int) -> None:
        """Инициализация"""
        self.collection = CommandCollection()
        self.collection.add_item(
            container.resolve("CheckFuelCommand", fight_id, obj_id)
        )
        self.collection.add_item(
            container.resolve("RotateCommand", fight_id, obj_id)
        )
        self.collection.add_item(
            container.resolve("BurnFuelCommand", fight_id, obj_id)
        )

    def execute(self) -> None:
        """Выполняем поворот с расходом топлива"""
        for command in self.collection:
            try:
                command.execute()
            except BaseCommandExceptionError as e:
                break
                # raise RotateBurnFuelCommandError(str(e))


act = {
    "RotateBurnFuelCommand": RotateBurnFuelCommand,
    "MoveBurnFuelCommand": MoveBurnFuelCommand,
    "ShootCheckBulletCommand": ShootCheckBulletCommand,
}
