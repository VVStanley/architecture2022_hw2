from src.design_patterns.command import CommandInterface
from src.move.movable import MovableInterface
from src.vector import Vector


class MoveCommand(CommandInterface):
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


"""
ДЗ по командам:

5.Реализовать команду для модификации вектора мгновенной скорости при повороте
Необходимо учесть, что не каждый разворачивающийся объект движется.
6.Реализовать команду поворота, которая еще и меняет вектор мгновенной скорости
если есть.
"""
# TODO: 5 и 6 пункты не понятны совсем, уточнить
