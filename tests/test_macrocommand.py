from typing import List
from unittest.mock import Mock

import pytest

from src.design_patterns.command import CommandInterface
from src.exceptions import CommandExceptionError
from src.macro_command import MacroCommand


class TestMacroCommand:
    """Тестируем макрокоманду"""

    def test_command_with_exception(
        self,
        move_command: Mock,
        burn_fuel_command: Mock,
        get_exception_commands: List[CommandInterface]
    ) -> None:
        """Тестируем макрокоманду с инициализацией исключения"""
        macro_command = MacroCommand(commands=get_exception_commands)

        with pytest.raises(CommandExceptionError) as exc_info:
            macro_command.execute()

        assert move_command.movable.set_position.called is True
        assert move_command.movable.set_position.call_count == 1
        assert burn_fuel_command.fueled.set_fuel.called is True
        assert burn_fuel_command.fueled.set_fuel.call_count == 1
        assert exc_info.typename == "CommandExceptionError"
        assert str(exc_info.value) == "Stop macro command"

    def test_command_ok(
        self,
        move_command: Mock,
        rotate_command: Mock,
        burn_fuel_command: Mock,
        check_fuel_command: Mock,
        get_execute_commands: List[CommandInterface]
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
