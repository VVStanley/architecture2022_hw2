import inspect
from typing import Any, Dict, TypeVar

from src.exceptions.injector import DependencyResolutionExceptionError


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

        def isconstructor(obj: 'type') -> bool:
            return inspect.isfunction(obj) and obj.__name__ == '__init__'

        constructors = inspect.getmembers(
            self.class_type, predicate=isconstructor
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


class Container:
    """IoC container"""

    def __init__(self, registry_map: dict, scope: dict) -> None:
        """

        :param registry_map: Словарь с конструкторами классов
        :param scope: Словарь с аргументами для классов

        storage - Хранилище для инициализированных классов
        """
        self.registry_map = registry_map
        self.scope = scope
        self.storage: Dict[str, Any] = {}
        self._initialization_types()

    @staticmethod
    def _check_arguments(argument_map: dict, argument_types: dict) -> None:
        """Проверям аргументы в scope с аргументами в __init__ class_type"""
        for arg_name, arg_type in argument_types.items():
            if arg_name not in argument_map:
                raise DependencyResolutionExceptionError(
                    f"Not found argument {arg_name} in scope"
                )
            if type(argument_map[arg_name]) != arg_type:
                raise DependencyResolutionExceptionError(
                    f"Wrong type argument"
                    f" {arg_name}:{type(argument_map[arg_name])}"
                    f" must be {arg_type}"
                )

    def _get_arguments_type(self, argument_types: dict) -> dict:
        """Получаем аргументы из контейнера"""
        try:
            argument_map = {
                arg_name: self.storage[arg_name.title()] for arg_name in
                argument_types.keys()
            }
        except Exception as e:
            raise DependencyResolutionExceptionError(str(e))
        return argument_map

    def _create(self, class_name: str, argument_types: dict) -> None:
        """Создаем объекты"""
        argument_map: dict = {}

        # Если есть инструкции в scope
        if self.scope.get(class_name):
            argument_map = self.scope.get(class_name, {})
            self._check_arguments(argument_map, argument_types)

        # Если есть у класса аргументы
        elif argument_types:
            argument_map = self._get_arguments_type(argument_types)

        class_type = self.registry_map[class_name].class_type
        self.storage[class_name] = class_type(**argument_map)

    def _initialization_types(self) -> None:
        """Инициализируем все зарегестрированные классы"""
        for class_name, constructor in self.registry_map.items():
            self._create(class_name, constructor.argument_types)

    def resolve(self, class_name: str) -> Any:
        """Возвращаем созданный класс"""

        if class_name not in self.storage:
            raise DependencyResolutionExceptionError(
                f"Class {class_name} not found in container"
            )
        return self.storage[class_name]


class ContainerBuilder:
    """Регистрируем классы и создаем контейнер"""

    def __init__(self) -> None:
        self.registry: Dict[str, Any] = {}

    def register_class(self, class_type: 'type') -> None:
        """Регистрация классов"""
        constructor = Constructor(class_type)
        self.registry[class_type.__name__] = constructor

    def build(self, scope: dict) -> Container:
        """Создаем контейнер"""
        return Container(self.registry, scope)
