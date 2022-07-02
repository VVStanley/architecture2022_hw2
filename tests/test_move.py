"""Тесты для модуля move"""
from unittest.mock import MagicMock

from src.movable import Movable
from src.move import Move
from src.vector import Vector


class TestMoveObject:
    """Тестируем объект на передвижение"""

    def test_move(self):
        """Успешное передвижение"""
        movable = Movable()
        movable.get_position = MagicMock(return_value=Vector(12, 5))
        movable.get_velocity = MagicMock(return_value=Vector(-7, 3))

        move = Move(movable)
        move.execute()

        a = 1
