import inspect
from typing import Dict, TypeVar

from exceptions.injector import DependencyResolutionExceptionError


class Constructor:
    """Конструктор для классов"""

    def __init__(self, class_type: 'type') -> None:
        """
        :param class_type: Регистрируемый класс

        argument_types - Аргументы регистрируемого класса
        """
        self.class_type = class_type
        self.argument_types: Dict[str, 'type'] = {}

        self.find_constructor()

    def _find_constructor(self) -> TypeVar:
        """Получение конструктора для класса"""

        def is_constructor(obj: 'type') -> bool:
            return inspect.isfunction(obj) and obj.__name__ == '__init__'

        constructors = inspect.getmembers(
            self.class_type, predicate=is_constructor
        )

        if constructors:
            name, constructor = constructors[0]
            return constructor

        raise DependencyResolutionExceptionError(
            f"The requested type {self.class_type.__name__}"
            f" no explicit __init__ method"
        )

    @staticmethod
    def _filter_annotations(annotations: dict) -> dict:
        """Фильтруем аргументы, удаляем return как аннатацию"""
        return {
            arg_name: arg_type
            for arg_name, arg_type in annotations.items()
            if arg_name != 'return'
        }

    def find_constructor(self) -> None:
        constructor = self._find_constructor()
        if constructor is not None:
            self.argument_types = self._filter_annotations(
                constructor.__annotations__
            )
