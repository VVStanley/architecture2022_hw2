from src.commands.iterator import CommandCollection
from src.design_patterns.command import CommandInterface
from src.exceptions.command import BaseCommandExceptionError


class MacroCommand(CommandInterface):
    """Простейшая макрокоманда"""

    def __init__(self, commands: CommandCollection) -> None:
        """Инициализация

        :param commands: коллекция команд для выполнения
        """
        self.commands = commands

    def execute(self) -> None:
        """Последовательное выполнение команд"""
        for command in self.commands:
            try:
                command.execute()
            except BaseCommandExceptionError as e:
                raise type(e)()
