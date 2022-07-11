"""Тесты для модуля move"""
from unittest.mock import MagicMock, Mock

import pytest

from src.exceptions import ObjectIsNotVectorTypeError
from src.movable import Movable
from src.move import Move
from src.vector import Vector


class TestMoveObject:
    """Тестируем объект на передвижение"""

    def test_move_position_none(self) -> None:
        """Попытка сдвинуть объект, у которого невозможно прочитать
        положение в пространстве, приводит к ошибке
        """
        movable = Mock()
        movable.get_position = MagicMock(return_value=None)
        movable.get_velocity = MagicMock(return_value=Vector(-7, 3))

        move = Move(movable)

        with pytest.raises(ObjectIsNotVectorTypeError) as exc_info:
            move.execute()

        assert exc_info.typename == "ObjectIsNotVectorTypeError"
        assert str(exc_info.value) == "Type must be Vector"

    def test_move_velocity_none(self) -> None:
        """Попытка сдвинуть объект, у которого невозможно изменить
        положение в пространстве, приводит к ошибке
        """
        movable = Mock()
        movable.get_position = MagicMock(return_value=Vector(12, 5))
        movable.get_velocity = MagicMock(return_value=None)

        move = Move(movable)

        with pytest.raises(ObjectIsNotVectorTypeError) as exc_info:
            move.execute()

        assert exc_info.typename == "ObjectIsNotVectorTypeError"
        assert str(exc_info.value) == "Type must be Vector"

    def test_move_object(self) -> None:
        """Тестируем команду движения
        Для объекта, находящегося в точке (12, 5) и движущегося
        со скоростью (-7, 3) движение меняет положение объекта на (5, 8)
        """
        movable = Mock()
        movable.get_position = MagicMock(return_value=Vector(12, 5))
        movable.get_velocity = MagicMock(return_value=Vector(-7, 3))

        move = Move(movable)
        move.execute()

        # Проверяем что set_position был вызван
        assert movable.set_position.called is True

        args, kwargs = movable.set_position.call_args_list[0]

        # Проверяем что set_position вызван с правильным аргументом
        assert args[0] == Vector(5, 8)

    def test_move(self) -> None:
        """Успешное передвижение объекта
        Для объекта, находящегося в точке (12, 5) и движущегося
        со скоростью (-7, 3) движение меняет положение объекта на (5, 8)
        """
        ship = Mock()
        ship.position = Vector(12, 5)
        ship.velocity = Vector(-7, 3)

        movable = Movable(unit=ship)

        move = Move(movable)
        move.execute()

        assert ship.position.x == 5
        assert ship.position.y == 8

    def test_velocity_not_read(self) -> None:
        """Попытка сдвинуть объект, у которого невозможно прочитать значение
        мгновенной скорости
        """
        ship = Mock()
        ship.position = Vector(12, 5)
        ship.velocity = None

        movable = Movable(unit=ship)

        move = Move(movable)

        with pytest.raises(Exception) as exc_info:
            move.execute()

        assert exc_info.typename == "ObjectIsNotVectorTypeError"
        assert str(exc_info.value) == "Type must be Vector"
