from unittest.mock import MagicMock, Mock

import pytest

from src.exceptions import CheckFuelCommandError
from src.fuel.fuel import BurnFuelCommand, CheckFuelCommand


class TestFueled:
    """Тестирование объектов с жиганием топлива"""

    def test_burn_fuel(self) -> None:
        """Тестируем команду сжигания топлива"""
        fueled = Mock()

        fueled.get_remaining_fuel = MagicMock(return_value=300)
        fueled.get_consumption_fuel = MagicMock(return_value=2)

        burn_fuel = BurnFuelCommand(fueled)

        burn_fuel.execute()

        assert fueled.set_fuel.called is True

        args, kwargs = fueled.set_fuel.call_args_list[0]

        assert args[0] == 298

    def test_check_fuel(self) -> None:
        """Тестируем команду проверки остатка топлива"""
        fueled = Mock()

        fueled.get_remaining_fuel = MagicMock(return_value=25)
        fueled.get_consumption_fuel = MagicMock(return_value=2)

        check_fuel = CheckFuelCommand(fueled)

        check_fuel.execute()

        assert fueled.get_remaining_fuel.called is True

    def test_check_fuel_with_esception(self) -> None:
        """Если топлива меньше ноля инициируется исключение"""
        fueled = Mock()

        fueled.get_remaining_fuel = MagicMock(return_value=0)
        fueled.get_consumption_fuel = MagicMock(return_value=2)

        check_fuel = CheckFuelCommand(fueled)

        with pytest.raises(CheckFuelCommandError) as exc_info:
            check_fuel.execute()

        assert exc_info.typename == "CheckFuelCommandError"
        assert str(exc_info.value) == "Ran out of fuel for unit"
