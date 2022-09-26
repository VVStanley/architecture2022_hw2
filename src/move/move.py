from design_patterns.command import CommandInterface
from exceptions.command import MoveCommandError
from exceptions.vector import ObjectIsNotVectorTypeError
from move.movable import MovableInterface
from utils.vector import Vector


class MoveCommand(CommandInterface):
    """Команда движения объекта"""

    def __init__(self, movable: MovableInterface) -> None:
        self.movable = movable

    def execute(self) -> None:
        """Перемещаем объект"""
        try:
            vector = Vector.plus(
                self.movable.get_position(), self.movable.get_velocity()
            )
        except ObjectIsNotVectorTypeError:
            raise MoveCommandError
        self.movable.set_position(vector=vector)
