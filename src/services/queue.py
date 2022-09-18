from queue import Queue
from typing import Dict


class QueueManager:
    """ Менеджер очередей для распределения команд по играм """

    def __init__(self) -> None:
        """Инициализация"""
        self.queues: Dict[str, Queue] = {}

    def create_queue(self, fight_id: str) -> Queue:  # type: ignore
        """Создаем очередь для игры.
        :param fight_id: ИД битвы.
        """
        self.queues.update({fight_id: Queue()})
        return self.queues.get(fight_id)  # type: ignore

    def get_queue(self, fight_id: str) -> Queue:  # type: ignore
        """Возвращаем очередь по ИД боя.
        :param fight_id: ИД битвы.
        """
        return self.queues.get(fight_id)  # type: ignore


q_manager = QueueManager()
