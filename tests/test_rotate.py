from unittest.mock import MagicMock, Mock

from rotate.rotate import RotateCommand


class TestRotate:

    def test_rotate(self) -> None:
        """Тестируем команду поворота"""
        rotable = Mock()

        rotable.get_direction = MagicMock(return_value=3)
        rotable.get_angular_velocity = MagicMock(return_value=2)
        rotable.get_direction_number = MagicMock(return_value=8)

        rotate = RotateCommand(rotable)

        rotate.execute()

        # Проверяем что set_position был вызван
        assert rotable.set_direction.called is True

        args, kwargs = rotable.set_direction.call_args_list[0]

        # Проверяем что set_position вызван с правильным аргументом
        assert args[0] == 0.625
