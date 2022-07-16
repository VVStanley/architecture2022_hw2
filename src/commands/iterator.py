from collections.abc import Iterable, Iterator
from typing import List

from src.design_patterns.command import CommandInterface


class CommandIterator(Iterator):
    """Итератор для команд"""

    """Атрибут _position хранит текущее положение обхода"""
    _position: int

    """Этот атрибут указывает направление обхода"""
    _reverse: bool = False

    def __init__(
        self, commands: List[CommandInterface], reverse: bool = False
    ) -> None:
        self._commands = commands
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> CommandInterface:
        """ Метод __next __() должен вернуть следующий
        элемент в последовательности
        """
        try:
            value = self._commands[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class CommandCollection(Iterable):
    """Коллекция для итератора"""

    def __init__(self) -> None:
        self._commands: List[CommandInterface] = []

    def __len__(self) -> int:
        """Возвращаем количество элементов"""
        return len(self._commands)

    def __iter__(self) -> CommandIterator:
        """
        Возвращает объект итератора, с прямой сортировкой
        """
        return CommandIterator(self._commands)

    def reverse(self) -> CommandIterator:
        """
        Возвращает объект итератора, с обратной сортировкой
        """
        return CommandIterator(self._commands, True)

    def add_item(self, command: CommandInterface) -> None:
        """Добавление элемента в коллекцию"""
        self._commands.append(command)
