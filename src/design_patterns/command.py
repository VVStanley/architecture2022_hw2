from abc import ABCMeta, abstractmethod


class CommandInterface(metaclass=ABCMeta):
    """Интерфейс паттерна Команда"""

    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError
