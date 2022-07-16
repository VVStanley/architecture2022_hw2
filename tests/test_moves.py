import pytest

from src.commands.moves import MoveBurnFuelCommand
from src.exceptions import CommandExceptionError
from src.units.unit import Unit
from src.vector import Vector


class TestMoveBurnFuelCommand:
    """Тестируем команду движения по прямой с расходом топлива"""

    def test_exceptions_check_fuel(self, unit_space_ship: Unit) -> None:
        """Если топливо закончится, возникает исключение"""
        command = MoveBurnFuelCommand(unit=unit_space_ship)

        with pytest.raises(CommandExceptionError) as exc_info:
            command.execute()
            command.execute()
            command.execute()
            command.execute()

        assert exc_info.typename == "CommandExceptionError"
        assert str(exc_info.value) == (
            "Stop unit with error: Ran out of fuel for unit"
        )

    def test_collection(self, unit_space_ship: Unit) -> None:
        """Проверим коллекцию у команды"""
        command = MoveBurnFuelCommand(unit=unit_space_ship)

        assert 3 == len(command.collection)

    def test_ok(self, unit_space_ship: Unit) -> None:
        """Проверка команды на выполнение"""

        command = MoveBurnFuelCommand(unit=unit_space_ship)
        command.execute()

        assert getattr(unit_space_ship, "remaining_fuel") == 3
        assert getattr(unit_space_ship, "position") != Vector(1, 1)
