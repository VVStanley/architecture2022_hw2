from abc import ABCMeta

from src.vector import Vector


class UnitInterface(metaclass=ABCMeta):

    @property
    def position(self) -> Vector:
        return NotImplemented

    @property
    def velocity(self) -> Vector:
        return NotImplemented
