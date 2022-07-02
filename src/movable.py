from abc import ABCMeta, abstractmethod

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

    def get_position(self) -> Vector:
        pass
