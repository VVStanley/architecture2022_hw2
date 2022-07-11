from abc import ABCMeta, abstractmethod


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
