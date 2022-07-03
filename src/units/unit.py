from abc import ABCMeta

from src.vector import Vector


class UnitInterface(metaclass=ABCMeta):

    @property
    def position(self) -> Vector:
        return NotImplemented

    @position.setter
    def position(self, vector: Vector) -> None:
        raise NotImplementedError

    @property
    def velocity(self) -> Vector:
        return NotImplemented
