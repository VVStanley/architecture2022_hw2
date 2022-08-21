from src.injector.constructor import Constructor
from src.injector.container import Container


class ContainerBuilder:
    """Регистрируем классы и создаем контейнер"""

    def __init__(self) -> None:
        self.container = Container()

    def register_class(self, class_type: 'type') -> None:
        """Регистрация классов"""
        constructor = Constructor(class_type)
        self.container.storage[class_type.__name__] = constructor

    def register_scope(self, name_scope: str, name_class: str) -> None:
        """Создаем Новые объекты в контейнере"""
        self.container.register(
            name_scope, self.container.storage.get(name_class)  # type: ignore
        )
