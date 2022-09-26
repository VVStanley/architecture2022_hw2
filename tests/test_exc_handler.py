from collections import deque
from unittest.mock import Mock

from exceptions.handler import ExceptionHandle


class TestExceptionHandle:
    """Тестируес обработчик исключений"""

    def test_handle(self) -> None:
        """Тестируем добавление обработчиков команд в очередь"""

        command = Mock()
        command_exception = Mock()
        amount_handlers = 3

        queue: deque = deque()
        queue.append(command)
        queue.append(command)
        amount_commands = len(queue)

        handler = ExceptionHandle(command=command_exception, queue=queue)
        handler.handle(amount_handlers)

        assert len(queue) == amount_commands + amount_handlers
