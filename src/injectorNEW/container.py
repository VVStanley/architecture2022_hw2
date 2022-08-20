from typing import Any, Dict, List

from src.exceptions.injector import DependencyResolutionExceptionError
from src.injectorNEW.constructor import Constructor
from src.injectorNEW.scope import TECHNICAL_ARGUMENTS


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
        """Проверяем аргументы в scope с аргументами в __init__ class_type"""
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

    def _check_arguments_for_types(
            self, class_name: str, argument_map: List[dict]
    ) -> None:
        """Проверяем аргументы для объекта объявленные в scope"""
        constructor: Constructor = self.registry_map.get(class_name)
        for arguments in argument_map:
            arguments_filter = {
                key: value for key, value in arguments.items()
                if key not in TECHNICAL_ARGUMENTS
            }
            self._check_arguments(
                argument_map=arguments_filter,
                argument_types=constructor.argument_types
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

        # Если есть у класса аргументы
        if argument_types:
            argument_map = self._get_arguments_type(argument_types)

        class_type = self.registry_map[class_name].class_type
        self.storage[class_name] = class_type(**argument_map)

    def _prepare_arguments(self, class_name: str, types_args: dict):
        """Подготавливаем все необходимые аргументы"""

    def _initialization_types(self) -> None:
        """Инициализируем все зарегистрированные классы"""

        # Сначала регистрируем классы из scope
        for class_name, argument_map in self.scope.items():
            self._check_arguments_for_types(class_name, argument_map)
            a = 1

        for class_name, constructor in self.registry_map.items():
            # Если есть инструкции в scope
            if self.scope.get(class_name):
                self._prepare_arguments(class_name, self.scope.get(class_name))
            else:
                self._create(class_name, constructor.argument_types)

    def resolve(self, class_name: str) -> Any:
        """Возвращаем созданный класс"""

        if class_name not in self.storage:
            raise DependencyResolutionExceptionError(
                f"Class {class_name} not found in container"
            )
        return self.storage[class_name]
