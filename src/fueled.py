from abc import ABCMeta, abstractmethod


class FueledInterface(metaclass=ABCMeta):
    """Интерфейс для расхода топлива"""

    @abstractmethod
    def get_remaining_fuel(self) -> int:
        """Получить остаток топлива"""
        raise NotImplementedError

    @abstractmethod
    def get_fuel_consumption(self) -> int:
        """Получить расход топлива"""
        raise NotImplementedError

    @abstractmethod
    def set_fuel(self, consumption: int) -> None:
        """Устанавливаем топливо"""
        raise NotImplementedError
