from typing import Any, Dict, List, Union

from exceptions.injector import DependencyResolutionExceptionError
from injector.constructor import Constructor
from injector.fields import Field
from injector.scope import TechnicalArguments


class Container:
    """IoC container"""

    _constructor: Constructor
    _scope: List[Dict[Union[str, TechnicalArguments], Any]]
    _fight_id: str  # ИД игры
    storage: Dict[str, Any] = {}

    def register(
        self, scope: List[dict], fight_id: str, name_class: str
    ) -> None:
        """
        :param scope:
        :param fight_id:
        :param constructor: Конструктор класса для инициализации объектов
        """
        self._constructor = self.storage.get(name_class)
        self._scope = scope
        self._fight_id = fight_id
        self.storage[fight_id] = {}
        self._initialization_types()

    def _check_arguments(self, argument_map: dict) -> None:
        """Проверяем аргументы в scope """
        for arg_name, arg_type in self._constructor.argument_types.items():
            if arg_name == 'kwargs':
                return
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

    @staticmethod
    def _prepare_arguments(argument_map: dict) -> dict:
        """Подготавливаем аргументы для инициализации"""
        return {
            key: value.value() if isinstance(value, Field) else value
            for key, value in argument_map.items()
        }

    def _initialization_types(self) -> None:
        """Стратегия инициализации объектов из scope"""
        class_type = self._constructor.class_type

        for arguments_map in self._scope:

            filter_arguments = {
                key: value for key, value in arguments_map.items()
                if not isinstance(key, TechnicalArguments)
            }

            self._check_arguments(argument_map=filter_arguments)

            # Создаем объекты из scope необходимое количество AMOUNT
            for _ in range(
                    arguments_map.get(TechnicalArguments.AMOUNT.name, 0)
            ):
                arguments = self._prepare_arguments(
                    argument_map=filter_arguments
                )

                self.storage[self._fight_id][arguments.get("id")] = (
                    class_type(**arguments)
                )

    def _resolve_type(self, constructor: Constructor, obj: 'type') -> Any:
        """Получаем необходимые аргументы рекурсивно и инициализируем класс"""
        arguments = {}
        for arg_name, arg_type in constructor.argument_types.items():
            if arg_type == type(obj):
                arguments.update({arg_name: obj})
            else:
                arguments.update(
                    {
                        arg_name: self._resolve_type(
                            constructor=self.storage[arg_name.title()], obj=obj
                        )
                    }
                )
        return constructor.class_type(**arguments)

    def resolve(
        self, class_name: str, name_scope: str, obj_id: int
    ) -> Any:
        """Возвращаем созданный класс

        :param class_name: Имя класса для инициализации
        :param name_scope: Имя scope для поиска объекта
        :param obj_id: ИД объекта из scope
        """
        if name_scope not in self.storage:
            raise DependencyResolutionExceptionError(
                f"Scope name {name_scope} not register in container"
            )
        if obj_id not in self.storage[name_scope]:
            raise DependencyResolutionExceptionError(
                f"Object with id:{obj_id} not found in scope:{name_scope}"
            )

        return self._resolve_type(
            constructor=self.storage[class_name],
            obj=self.storage[name_scope][obj_id]
        )
