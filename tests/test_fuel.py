from unittest.mock import MagicMock, Mock

import pytest

from src.exceptions import CommandExceptionError
from src.fuel import BurnFuel, CheckFuel


class TestFueled:
    """Тестирование объектов с жиганием топлива"""

    def test_burn_fuel(self) -> None:
        """Тестируем команду сжигания топлива"""
        fueled = Mock()

        fueled.get_remaining_fuel = MagicMock(return_value=300)
        fueled.get_fuel_consumption = MagicMock(return_value=2)

        burn_fuel = BurnFuel(fueled)

        burn_fuel.execute()

        assert fueled.set_fuel.called is True

        args, kwargs = fueled.set_fuel.call_args_list[0]

        assert args[0] == 298

    def test_check_fuel(self) -> None:
        """Тестируем команду проверки остатка топлива"""
        fueled = Mock()

        fueled.get_remaining_fuel = MagicMock(return_value=25)

        check_fuel = CheckFuel(fueled)

        check_fuel.execute()

        assert fueled.get_remaining_fuel.called is True

    def test_check_fuel_with_esception(self) -> None:
        """Если топлива меньше ноля инициируется исключение"""
        fueled = Mock()

        fueled.__str__ = MagicMock(return_value="Space ship 9")  # type: ignore
        fueled.get_remaining_fuel = MagicMock(return_value=0)

        check_fuel = CheckFuel(fueled)

        with pytest.raises(CommandExceptionError) as exc_info:
            check_fuel.execute()

        assert exc_info.typename == "CommandExceptionError"
        assert str(exc_info.value) == "Ran out of fuel for unit: Space ship 9"
