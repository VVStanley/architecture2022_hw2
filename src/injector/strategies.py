import math

from units.unit import Unit
from utils.vector import Vector


def constructor(self, unit: Unit) -> None:  # type: ignore
    """Конструктор для адаптеров"""
    self.unit = unit


# Fueled

def get_remaining_fuel(self) -> int:  # type: ignore
    """Получить остаток топлива"""
    return getattr(self.unit, "remaining_fuel")


def get_consumption_fuel(self) -> int:  # type: ignore
    """Получить расход топлива"""
    return getattr(self.unit, "consumption_fuel")


def set_fuel(self, consumption: int) -> None:  # type: ignore
    """Устанавливаем топливо"""
    self.unit.remaining_fuel = consumption


# Movable

def get_position(self) -> Vector:  # type: ignore
    """Возвращаем позицию объекта"""
    return getattr(self.unit, "position")


def get_velocity(self) -> Vector:  # type: ignore
    """Возвращаем скорость объекта"""
    d: int = getattr(self.unit, "direction")
    n: int = getattr(self.unit, "direction_numbers")
    v: int = getattr(self.unit, "velocity")
    return Vector(
        round(v * math.cos(d / 360 * n)), round(v * math.sin(d / 360 * n))
    )


def set_position(self, vector: Vector) -> None:  # type: ignore
    """Устанавливаем объекту новую позицию"""
    self.unit.position = vector


# Rotable


def get_direction(self) -> int:  # type: ignore
    """Возвращает направление объекта"""
    return getattr(self.unit, 'direction')


def get_direction_number(self) -> int:  # type: ignore
    """Возвращает угловую скорость объекта"""
    return getattr(self.unit, 'direction_numbers')


def get_angular_velocity(self) -> int:  # type: ignore
    """Возвращает угловую скорость"""
    return getattr(self.unit, 'angular_velocity')


def set_direction(self, direction: float) -> None:  # type: ignore
    """Устанавливаем поворот"""
    self.unit.direction = direction


# Shooting


def check_bullets(self) -> bool:  # type: ignore
    """Проверяем наличие пуль"""
    return getattr(self.unit, 'bullets') > 0


def shoot(self) -> None:  # type: ignore
    """Выстрел"""
    getattr(self.unit, 'bullets') - 1
