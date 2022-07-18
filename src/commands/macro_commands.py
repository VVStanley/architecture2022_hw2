from src.commands.iterator import CommandCollection
from src.design_patterns.command import CommandInterface
from src.exceptions import CommandExceptionError


class MacroCommand(CommandInterface):
    """Простейшая макрокоманда"""

    def __init__(self, commands: CommandCollection) -> None:
        self.commands = commands

    def execute(self) -> None:
        """Последовательное выполнение комманд"""
        for command in self.commands:
            try:
                command.execute()
            except CommandExceptionError as e:
                raise type(e)()
