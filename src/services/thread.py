import threading
from enum import Enum, auto
from queue import Queue

from commands import act
from logconf import logger


class State(Enum):
    READ_COMMAND = auto()
    HARD_STOP = auto()
    SOFT_STOP = auto()
    MOVE_TO = auto()


get_state = {
    "read_command": State.READ_COMMAND,
    "hard_stop": State.HARD_STOP,
    "soft_stop": State.SOFT_STOP,
    "move_to": State.MOVE_TO,
}


class FightThread(threading.Thread):
    """Поток для битвы"""

    event = threading.Event()
    lock = threading.Lock()

    def __init__(self, queue: Queue, fight_id: str) -> None:
        """Инициализация
        :param queue: Очередь для конкретной битвы.
        :param fight_id: ИД битвы.
        """
        threading.Thread.__init__(self, daemon=True)
        self.queue = queue
        self.name = fight_id

    def _execute_command(self, api_command: dict) -> None:
        """ Выполнение команды игры """
        command = act.get(api_command.get("command"))
        command = command(self.name, api_command.get("id"))
        try:
            command.execute()
        except Exception as e:
            logger.error(
                f"Game:{self.name} thread:{self.name} message:{str(e)}"
            )

    def run(self) -> None:
        """Обработка команды из очереди"""
        state = State.READ_COMMAND

        # Если состояние HARD_STOP заканчиваем обработку
        while state != State.HARD_STOP:

            api_command = self.queue.get()

            api_state = api_command.get('state', 'read_command')
            state = get_state.get(api_state, State.READ_COMMAND)

            # Режим игры
            if state == State.READ_COMMAND:
                self._execute_command(api_command)

            # Soft stop
            elif state == State.SOFT_STOP:
                while not self.queue.empty():
                    api_command = self.queue.get()
                    self._execute_command(api_command)
                    self.queue.task_done()
                state = State.HARD_STOP
                logger.error("Game soft stop")

            # Hard stop
            elif state == State.HARD_STOP:
                logger.error("Game hard stop")

            self.queue.task_done()
