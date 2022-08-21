import pytest

from src.commands.moves import MoveBurnFuelCommand
from src.exceptions.command import BaseCommandExceptionError
from src.injectorOLD import container


class TestMoveBurnFuelCommand:
    """Тестируем команду движения по прямой с расходом топлива"""

    def test_ok(self) -> None:
        """Проверка команды на выполнение"""

        unit = container.resolve('Unit')
        save_position = unit.position
        calc_remaining_fuel = unit.remaining_fuel - unit.consumption_fuel

        command = MoveBurnFuelCommand()
        command.execute()

        assert getattr(unit, "remaining_fuel") == calc_remaining_fuel
        assert getattr(unit, "position") != save_position

    def test_exceptions_check_fuel(self) -> None:
        """Если топливо закончится, возникает исключение"""
        command = MoveBurnFuelCommand()

        with pytest.raises(BaseCommandExceptionError) as exc_info:
            command.execute()
            command.execute()
            command.execute()
            command.execute()
            command.execute()

        assert exc_info.typename == "MoveBurnFuelCommandError"
        assert str(exc_info.value) == "Ran out of fuel for unit"

    def test_collection(self) -> None:
        """Проверим коллекцию у команды"""
        command = MoveBurnFuelCommand()

        assert 3 == len(command.collection)
