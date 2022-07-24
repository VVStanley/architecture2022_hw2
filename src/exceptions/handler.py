from collections import deque

from src.commands.repeater import (
    OneRepeatCommand, ThreeRepeatCommand,
    TwoRepeatCommand,
)
from src.design_patterns.command import CommandInterface


class ExceptionHandle:
    """Обработки исключений вручную"""

    """Хеш таблица с обработчиками"""
    handle_exception: dict = {
        3: ThreeRepeatCommand,
        2: TwoRepeatCommand,
        1: OneRepeatCommand,
    }

    def __init__(self, command: CommandInterface, queue: deque) -> None:
        """Инициализация

        :param command: команда для посторной обработки
        :param queue: очередь команд
        """
        self.queue = queue
        self.command = command

    def handle(self, repeats: int) -> None:
        """По количеству посторений выбираем обработчики
        и добавляем их в очередь

        :param repeats: кол-во необходимых обработок
        """
        [
            self.add_to_queue(index)  # type: ignore
            for index in range(1, repeats + 1)
            if index in self.handle_exception
        ]

    def add_to_queue(self, index: int) -> None:
        """Добавляем обработчик с командой в очередь

        :param index: индекс обработчика
        """
        repeat_command = self.handle_exception.get(index)
        self.queue.appendleft(repeat_command(self.command))  # type: ignore
