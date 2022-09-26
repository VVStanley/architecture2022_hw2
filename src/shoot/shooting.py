from abc import ABCMeta, abstractmethod

from units.unit import Unit


class ShootingInterface(metaclass=ABCMeta):

    @abstractmethod
    def check_bullets(self) -> bool:
        """Проверяем наличие пуль"""
        raise NotImplementedError

    @abstractmethod
    def shoot(self) -> None:
        """Выстрел"""
        raise NotImplementedError


class Shooting(ShootingInterface):

    def __init__(self, unit: Unit) -> None:
        self.unit = unit

    def check_bullets(self) -> bool:
        return getattr(self.unit, 'bullets') > 0

    def shoot(self) -> None:
        getattr(self.unit, 'bullets') - 1
