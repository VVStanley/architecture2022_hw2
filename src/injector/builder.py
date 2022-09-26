from injector.constructor import Constructor
from injector.container import Container
from injector.generator import AdapterGenerator


class ContainerBuilder:
    """Регистрируем классы и создаем контейнер"""

    def __init__(self) -> None:
        self.container = Container()

    @staticmethod
    def generate_adapter(interface: 'type') -> 'type':
        """Генерируем и регистрируем адаптер по интерфейсу"""
        generator = AdapterGenerator(interface)
        return generator.resolve()

    def register_class(self, class_type: 'type') -> None:
        """Регистрация классов"""
        constructor = Constructor(class_type)
        self.container.storage[class_type.__name__] = constructor
