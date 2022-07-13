from src.design_patterns.command import CommandInterface
from src.movable import MovableInterface
from src.vector import Vector


class Move(CommandInterface):
    """Команда движения объекта"""

    def __init__(self, movable: MovableInterface) -> None:
        self.movable = movable

    def execute(self) -> None:
        """Перемещаем объект"""
        self.movable.set_position(
            Vector.plus(
                self.movable.get_position(), self.movable.get_velocity()
            )
        )
