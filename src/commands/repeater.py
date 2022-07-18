from src.design_patterns.command import CommandInterface
from src.exceptions import (
    CommandExceptionError, OneRepeaterCommandError, TwoRepeaterCommandError,
)


class OneRepeatCommand(CommandInterface):
    """Команда выполняет комманду"""

    def __init__(self, command: CommandInterface) -> None:
        self.command = command

    def execute(self) -> None:
        """Выполняем команду"""
        try:
            self.command.execute()
        except CommandExceptionError as e:
            raise OneRepeaterCommandError(str(e))


class TwoRepeatCommand(CommandInterface):
    """Команда выполняет комманду"""

    def __init__(self, command: CommandInterface) -> None:
        self.command = command

    def execute(self) -> None:
        """Выполняем команду"""
        try:
            self.command.execute()
        except CommandExceptionError as e:
            raise TwoRepeaterCommandError(str(e))
