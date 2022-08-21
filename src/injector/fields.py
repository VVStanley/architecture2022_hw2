from abc import abstractmethod
from random import randint
from typing import Any

from src.design_patterns.singleton import Singleton
from src.utils.vector import Vector


class Field(metaclass=Singleton):
    """Поле для заполнения объектов"""

    @abstractmethod
    def value(self) -> Any:
        """Вернуть значение"""
        raise NotImplementedError


class AutoIncrementField(Field):
    """Поле возвращает последовательно уникальный идентификатор"""

    def __init__(self):
        self.increment = 0

    def __next__(self):
        self.increment += 1
        return self.increment

    def value(self) -> Any:
        return next(self)


class AutoVectorField(Field):
    """Поле возвращает случайное положение в пространстве"""

    @property
    def random_x(self):
        return randint(1, 9)

    @property
    def random_y(self):
        return randint(1, 9)

    def value(self) -> Any:
        return Vector(self.random_x, self.random_y)
