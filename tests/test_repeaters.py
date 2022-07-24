from unittest.mock import MagicMock

from src.commands.repeater import (
    OneRepeatCommand, ThreeRepeatCommand, TwoRepeatCommand,
)


class TestRepeaters:
    """Тестируем команды повторители"""

    def test_repeaters(self) -> None:
        """Тестируем команды повторители команд"""
        command = MagicMock()

        one_repeater_command = OneRepeatCommand(command=command)
        one_repeater_command.execute()

        two_repeater_command = TwoRepeatCommand(command=command)
        two_repeater_command.execute()

        three_repeater_command = ThreeRepeatCommand(command=command)
        three_repeater_command.execute()

        assert command.execute.called is True
        assert command.execute.call_count == 3
        assert len(command.method_calls) == 3
