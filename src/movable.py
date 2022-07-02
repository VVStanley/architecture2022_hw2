from abc import ABCMeta, abstractmethod

from src.units.unit import Unit
from src.vector import Vector


class MovableInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_position(self) -> Vector:
        """Возвращаем позицию объекта"""
        raise NotImplementedError

    @abstractmethod
    def get_velocity(self) -> Vector:
        """Возвращаем скорость объекта"""
        raise NotImplementedError

    @abstractmethod
    def set_position(self, vector: Vector) -> None:
        """Устанавливаем объекту новую позицию"""
        raise NotImplementedError


class Movable(MovableInterface):
    """Делаем объект подвижным"""

    def __init__(self, unit: Unit) -> None:
        self.unit = unit

    def get_position(self) -> Vector:
        return self.unit.position

    def get_velocity(self) -> Vector:
        return self.unit.velocity

    def set_position(self, vector: Vector) -> None:
        self.unit.position = vector
