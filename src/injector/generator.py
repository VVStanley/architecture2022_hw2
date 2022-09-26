import inspect
from typing import Callable

from injector.strategies import *  # noqa


class AdapterGenerator:
    """Генератор адаптеров по интерфейсу"""

    _prefix = "Interface"

    def __init__(self, interface: 'type') -> None:
        """

        :param interface: интерфейс для которого необходимо сгенерировать
        адаптер
        """
        self.interface = interface
        self._get_all_interface_methods()
        self._get_name_adapter()

    def _get_name_adapter(self) -> None:
        """Получаем имя адаптера"""
        index_prefix = self.interface.__name__.find(self._prefix)
        self.name = self.interface.__name__[:index_prefix]

    def _get_all_interface_methods(self) -> None:
        """Получаем ве методы для интерфейса"""
        self._methods = [
            name_method for name_method, _ in inspect.getmembers(
                self.interface, predicate=inspect.isfunction
            )
        ]

    @staticmethod
    def _get_constructor() -> Callable:
        """Возвращаем конструктор для адаптеров"""
        constructor.__name__ = '__init__'  # type: ignore # noqa: F405
        constructor.__qualname__ = '__init__'  # type: ignore # noqa: F405
        return constructor  # type: ignore # noqa: F405

    def resolve(self) -> type:
        return type(self.name, (object,), {
            "__init__": self._get_constructor(),
            **{name: eval(name) for name in self._methods}
        })
