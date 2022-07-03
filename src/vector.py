from abc import ABCMeta, abstractmethod

from src.exceptions import ObjectIsNotVectorTypeError


class VectorInterface(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, x: float, y: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def __add__(self, other: 'VectorInterface') -> 'VectorInterface':
        return NotImplemented

    @abstractmethod
    def __eq__(self, other: 'VectorInterface') -> bool:  # type: ignore
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
        raise ObjectIsNotVectorTypeError

    def __eq__(self, other: 'VectorInterface') -> bool:  # type: ignore
        """Операция сравнения на равенство"""
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        raise ObjectIsNotVectorTypeError

    @classmethod
    def plus(cls, vector1: 'Vector', vector2: 'Vector') -> 'Vector':
        """Проверка векторов перед сложением"""
        if isinstance(vector1, cls) and isinstance(vector2, cls):
            return vector1 + vector2
        raise ObjectIsNotVectorTypeError
