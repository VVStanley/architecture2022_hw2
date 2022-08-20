from typing import Any, Dict

from src.injectorNEW.constructor import Constructor
from src.injectorNEW.container import Container


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
