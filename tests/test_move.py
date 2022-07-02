"""Тесты для модуля move"""
import pytest

from src.movable import Movable
from src.move import Move
from src.units.unit import Unit
from src.vector import Vector


class TestMoveObject:
    """Тестируем объект на передвижение"""

    def test_move_without_velocity(self):
        """Попытка сдвинуть объект, у которого невозможно прочитать
        значение мгновенной скорости
        """
        tower = Unit()
        tower.position = Vector(12, 5)
        tower.velocity = None

        movable = Movable(unit=tower)

        move = Move(movable)
        with pytest.raises(Exception) as exc_info:
            move.execute()

        assert exc_info.typename == "OtherMustByVectorInterfaceError"

    def test_move_without_position(self):
        """Попытка сдвинуть объект, у которого невозможно прочитать
        положение в пространстве
        """
        swarm = Unit()
        swarm.position = None
        swarm.velocity = Vector(-7, 3)

        movable = Movable(unit=swarm)

        move = Move(movable)
        with pytest.raises(Exception) as exc_info:
            move.execute()

        assert exc_info.typename == "OtherMustByVectorInterfaceError"

    def test_move(self):
        """Успешное передвижение"""
        ship = Unit()
        ship.position = Vector(12, 5)
        ship.velocity = Vector(-7, 3)

        movable = Movable(unit=ship)

        move = Move(movable)
        move.execute()

        assert ship.position.x == 5
        assert ship.position.y == 8
