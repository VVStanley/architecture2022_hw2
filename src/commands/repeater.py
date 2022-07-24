from src.design_patterns.command import CommandInterface
from src.exceptions.command import BaseCommandExceptionError
from src.exceptions.repeater import (
    OneRepeaterError, ThreeRepeaterError,
    TwoRepeaterError,
)


class OneRepeatCommand(CommandInterface):
    """Команда выполняет комманду"""

    def __init__(self, command: CommandInterface) -> None:
        self.command = command

    def execute(self) -> None:
        """Выполняем команду"""
        try:
            self.command.execute()
        except BaseCommandExceptionError as e:
            raise OneRepeaterError(str(e))


class TwoRepeatCommand(CommandInterface):
    """Команда выполняет комманду"""

    def __init__(self, command: CommandInterface) -> None:
        self.command = command

    def execute(self) -> None:
        """Выполняем команду"""
        try:
            self.command.execute()
        except BaseCommandExceptionError as e:
            raise TwoRepeaterError(str(e))


class ThreeRepeatCommand(CommandInterface):
    """Команда выполняет комманду"""

    def __init__(self, command: CommandInterface) -> None:
        self.command = command

    def execute(self) -> None:
        """Выполняем команду"""
        try:
            self.command.execute()
        except BaseCommandExceptionError as e:
            raise ThreeRepeaterError(str(e))
