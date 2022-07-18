from logconf import logger
from src.design_patterns.command import CommandInterface


class LogCommand(CommandInterface):
    """Команда логирует сообщения об ошибке"""

    def __init__(self, message: str) -> None:
        self.message = message

    def execute(self) -> None:
        logger.error(self.message)
