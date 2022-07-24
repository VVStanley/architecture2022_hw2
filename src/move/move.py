from src.design_patterns.command import CommandInterface
from src.exceptions.command import MoveCommandError
from src.exceptions.vector import ObjectIsNotVectorTypeError
from src.move.movable import MovableInterface
from src.utils.vector import Vector


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
