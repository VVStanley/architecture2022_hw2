from typing import List

from src.design_patterns.command import CommandInterface
from src.exceptions import CommandExceptionError


class MacroCommand(CommandInterface):

    def __init__(self, commands: List[CommandInterface]) -> None:
        self.commands = commands

    def execute(self) -> None:
        """Последовательное выполнение комманд"""
        for command in self.commands:
            try:
                command.execute()
            except Exception:
                raise CommandExceptionError("Stop macro command")
