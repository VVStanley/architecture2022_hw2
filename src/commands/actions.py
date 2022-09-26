from commands.iterator import CommandCollection
from design_patterns.command import CommandInterface
from exceptions.command import (
    CheckBulletsCommandError, CheckFuelCommandError, MoveBurnFuelCommandError,
    MoveCommandError, RotateBurnFuelCommandError,
    RotateCommandError, ShootCheckBulletCommandError,
)
from injector import container


class ShootCheckBulletCommand(CommandInterface):
    """Макрокоманда для выстрела"""

    def __init__(self, fight_id: str, unit_id: int) -> None:
        """Инициализация"""
        self.unit_id = unit_id
        self.collection = CommandCollection()
        self.collection.add_item(
            container.resolve("CheckBulletsCommand", fight_id, unit_id)
        )
        self.collection.add_item(
            container.resolve("ShootCommand", fight_id, unit_id)
        )

    def execute(self) -> None:
        """Выполняем движение с расходом топлива"""
        for command in self.collection:
            try:
                command.execute()
            except CheckBulletsCommandError as e:
                raise ShootCheckBulletCommandError(
                    f"unit:{self.unit_id} {str(e)};"
                )


class MoveBurnFuelCommand(CommandInterface):
    """Макрокоманда движения с расходом топлива"""

    def __init__(self, fight_id: str, unit_id: int) -> None:
        """Инициализация"""
        self.unit_id = unit_id
        self.collection = CommandCollection()
        self.collection.add_item(
            container.resolve("CheckFuelCommand", fight_id, unit_id)
        )
        self.collection.add_item(
            container.resolve("MoveCommand", fight_id, unit_id)
        )
        self.collection.add_item(
            container.resolve("BurnFuelCommand", fight_id, unit_id)
        )

    def execute(self) -> None:
        """Выполняем движение с расходом топлива"""
        for command in self.collection:
            try:
                command.execute()
            except (CheckFuelCommandError, MoveCommandError) as e:
                raise MoveBurnFuelCommandError(
                    f"unit:{self.unit_id} {str(e)};"
                )


class RotateBurnFuelCommand(CommandInterface):
    """Макрокоманда для поворота с расходом топлива"""

    def __init__(self, fight_id: str, unit_id: int) -> None:
        """Инициализация"""
        self.unit_id = unit_id
        self.collection = CommandCollection()
        self.collection.add_item(
            container.resolve("CheckFuelCommand", fight_id, unit_id)
        )
        self.collection.add_item(
            container.resolve("RotateCommand", fight_id, unit_id)
        )
        self.collection.add_item(
            container.resolve("BurnFuelCommand", fight_id, unit_id)
        )

    def execute(self) -> None:
        """Выполняем поворот с расходом топлива"""
        for command in self.collection:
            try:
                command.execute()
            except (CheckFuelCommandError, RotateCommandError) as e:
                raise RotateBurnFuelCommandError(
                    f"unit:{self.unit_id} {str(e)};"
                )


act = {
    "RotateBurnFuelCommand": RotateBurnFuelCommand,
    "MoveBurnFuelCommand": MoveBurnFuelCommand,
    "ShootCheckBulletCommand": ShootCheckBulletCommand,
}
