from unittest.mock import Mock

import pytest

from src.commands.iterator import CommandCollection
from src.commands.macro_commands import MacroCommand
from src.exceptions import CommandExceptionError


class TestMacroCommand:
    """Тестируем макрокоманду"""

    def test_command_with_exception(
        self,
        move_command: Mock,
        check_fuel_command: Mock,
        burn_fuel_command: Mock,
        get_exception_commands: CommandCollection
    ) -> None:
        """Тестируем макрокоманду с инициализацией исключения"""
        macro_command = MacroCommand(commands=get_exception_commands)

        with pytest.raises(CommandExceptionError) as exc_info:
            macro_command.execute()

        assert check_fuel_command.fueled.get_remaining_fuel.called is True
        assert check_fuel_command.fueled.get_remaining_fuel.call_count == 1

        assert move_command.movable.set_position.called is True
        assert move_command.movable.set_position.call_count == 1

        assert burn_fuel_command.fueled.set_fuel.called is True
        assert burn_fuel_command.fueled.set_fuel.call_count == 1

        assert exc_info.typename == "CheckFuelCommandError"
        assert str(exc_info.value) == ("Ran out of fuel for unit")

    def test_command_ok(
        self,
        move_command: Mock,
        rotate_command: Mock,
        burn_fuel_command: Mock,
        check_fuel_command: Mock,
        get_execute_commands: CommandCollection
    ) -> None:
        """Запуск макрокоманды"""

        macro_command = MacroCommand(commands=get_execute_commands)

        macro_command.execute()

        assert move_command.movable.set_position.called is True
        assert move_command.movable.set_position.call_count == 5

        assert burn_fuel_command.fueled.set_fuel.called is True
        assert burn_fuel_command.fueled.set_fuel.call_count == 7

        assert check_fuel_command.fueled.get_remaining_fuel.called is True
        assert check_fuel_command.fueled.get_remaining_fuel.call_count == 7

        assert rotate_command.rotable.set_direction.called is True
        assert rotate_command.rotable.set_direction.call_count == 2
