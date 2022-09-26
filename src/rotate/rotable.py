from abc import ABCMeta, abstractmethod

from units.unit import Unit


class RotableInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_direction(self) -> int:
        """Возвращает направление объекта"""
        raise NotImplementedError

    @abstractmethod
    def get_direction_number(self) -> int:
        """Возвращает угловую скорость объекта"""
        raise NotImplementedError

    @abstractmethod
    def get_angular_velocity(self) -> int:
        """Возвращает угловую скорость"""
        raise NotImplementedError

    @abstractmethod
    def set_direction(self, direction: float) -> None:
        """Устанавливаем поворот"""
        raise NotImplementedError


class Rotable(RotableInterface):

    def __init__(self, unit: Unit) -> None:
        self.unit = unit

    def get_direction(self) -> int:
        return getattr(self.unit, 'direction')

    def get_direction_number(self) -> int:
        return getattr(self.unit, 'direction_numbers')

    def get_angular_velocity(self) -> int:
        return getattr(self.unit, 'angular_velocity')

    def set_direction(self, direction: float) -> None:
        self.unit.direction = direction
