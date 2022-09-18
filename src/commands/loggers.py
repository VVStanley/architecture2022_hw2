from src.design_patterns.command import CommandInterface
from src.logconf import logger


class LogCommand(CommandInterface):
    """Команда логирует сообщения об ошибке"""

    def __init__(self, message: str) -> None:
        """Инициализация

        :param message: сообщение для логирования
        """
        self.message = message

    def execute(self) -> None:
        """Выполняем логирование"""
        logger.error(self.message)
