from abc import ABCMeta, abstractmethod

from units.unit import Unit


class FueledInterface(metaclass=ABCMeta):
    """Интерфейс для расхода топлива"""

    @abstractmethod
    def get_remaining_fuel(self) -> int:
        """Получить остаток топлива"""
        raise NotImplementedError

    @abstractmethod
    def get_consumption_fuel(self) -> int:
        """Получить расход топлива"""
        raise NotImplementedError

    @abstractmethod
    def set_fuel(self, consumption: int) -> None:
        """Устанавливаем топливо"""
        raise NotImplementedError


class Fueled(FueledInterface):
    """Добавляем объекту топливо"""

    def __init__(self, unit: Unit) -> None:
        self.unit = unit

    def get_remaining_fuel(self) -> int:
        return getattr(self.unit, "remaining_fuel")  # noqa: B009

    def get_consumption_fuel(self) -> int:
        return getattr(self.unit, "consumption_fuel")  # noqa: B009

    def set_fuel(self, consumption: int) -> None:
        self.unit.remaining_fuel = consumption
