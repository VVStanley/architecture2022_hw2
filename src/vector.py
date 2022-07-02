from abc import ABCMeta, abstractmethod

from src.exceptions import ObjectNotMovableError


class VectorInterface(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, x: float, y: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def __add__(self, other: 'VectorInterface') -> 'VectorInterface':
        return NotImplemented


class Vector(VectorInterface):
    """Вектор"""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: 'VectorInterface') -> 'Vector':
        """Операция сложения"""
        if isinstance(other, self.__class__):
            return Vector(self.x + other.x, self.y + other.y)
        raise ObjectNotMovableError

    @classmethod
    def plus(cls, vector1: 'Vector', vector2: 'Vector') -> 'Vector':
        """Проверка векторов перед сложением"""
        if isinstance(vector1, cls) and isinstance(vector2, cls):
            return vector1 + vector2
        raise ObjectNotMovableError
