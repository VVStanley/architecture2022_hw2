import threading

from commands import act
from src.logconf import logger


class FightThread(threading.Thread):
    """Поток для битвы"""

    event = threading.Event()
    lock = threading.Lock()

    def __init__(self, queue, fight_id) -> None:
        """Инициализация
        :param queue: Очередь для конкретной битвы.
        :param fight_id: ИД битвы.
        """
        threading.Thread.__init__(self, daemon=True)
        self.queue = queue
        self.name = fight_id

    def run(self):
        """Обработка команды из очереди"""
        while True:
            api_command = self.queue.get()
            command = act.get(api_command.get("command"))
            command = command(self.name, api_command.get("id"))

            try:
                command.execute()
            except Exception as e:
                logger.error(
                    f"Game:{self.name} thread:{self.name} message:{str(e)}"
                )

            self.queue.task_done()
