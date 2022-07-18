import logging

from src.start import start


class TestLoggers:
    """Тест команды записываэщей ошибку в лог"""

    def test_logging_to_execute_start_command(self, caplog) -> None:
        """Тестируем логирование при старте макрокоманды"""

        with caplog.at_level(logging.ERROR):
            start()

        assert caplog.messages[0] == 'Ran out of fuel for unit'
