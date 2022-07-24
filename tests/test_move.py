"""Тесты для модуля move"""
from unittest.mock import MagicMock, Mock

import pytest

from src.exceptions.command import MoveCommandError
from src.move.move import MoveCommand
from src.utils.vector import Vector


class TestMoveObject:
    """Тестируем объект на передвижение"""

    def test_move_position_none(self) -> None:
        """Попытка сдвинуть объект, у которого невозможно прочитать
        положение в пространстве, приводит к ошибке
        """
        movable = Mock()
        movable.get_position = MagicMock(return_value=None)
        movable.get_velocity = MagicMock(return_value=Vector(-7, 3))

        move = MoveCommand(movable)

        with pytest.raises(MoveCommandError) as exc_info:
            move.execute()

        assert exc_info.typename == "MoveCommandError"
        assert str(exc_info.value) == "Unit cannot move"

    def test_move_velocity_none(self) -> None:
        """Попытка сдвинуть объект, у которого невозможно изменить
        положение в пространстве, приводит к ошибке
        """
        movable = Mock()
        movable.get_position = MagicMock(return_value=Vector(12, 5))
        movable.get_velocity = MagicMock(return_value=None)

        move = MoveCommand(movable)

        with pytest.raises(MoveCommandError) as exc_info:
            move.execute()

        assert exc_info.typename == "MoveCommandError"
        assert str(exc_info.value) == "Unit cannot move"

    def test_move_object(self) -> None:
        """Тестируем команду движения
        Для объекта, находящегося в точке (12, 5) и движущегося
        со скоростью (-7, 3) движение меняет положение объекта на (5, 8)
        """
        movable = Mock()
        movable.get_position = MagicMock(return_value=Vector(12, 5))
        movable.get_velocity = MagicMock(return_value=Vector(-7, 3))

        move = MoveCommand(movable)
        move.execute()

        # Проверяем что set_position был вызван
        assert movable.set_position.called is True

        args, kwargs = movable.set_position.call_args_list[0]

        # Проверяем что set_position вызван с правильным аргументом
        assert kwargs.get('vector') == Vector(5, 8)
