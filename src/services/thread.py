import threading

from commands import act
from injector.register import builder


class FightThread(threading.Thread):
    """Поток для битвы"""

    container = threading.local()
    fight_id = None
    name_thread = threading.current_thread().name

    def __init__(self, queue, fight_id) -> None:
        """Инициализация
        :param queue: Очередь для конкретной битвы.
        :param fight_id: ИД битвы.
        """
        self.queue = queue
        self.fight_id = fight_id
        threading.Thread.__init__(self, daemon=True)
        self.container = builder.container

    def run(self):
        """Обработка команды из очереди"""
        while True:
            api_command = self.queue.get()
            command = act.get(api_command.get("command"))
            command = command(self.fight_id, api_command.get("id"))
            command.execute()
            self.queue.task_done()
