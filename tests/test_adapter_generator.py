import inspect

import pytest

from src.fuel.fueled import FueledInterface
from src.injector.builder import ContainerBuilder


@pytest.fixture
def adapter() -> type:
    """Возвращаем адаптер"""
    builder = ContainerBuilder()
    return builder.generate_adapter(interface=FueledInterface)


class TestAdapterGenerator:
    """Тестирование генератора адаптеров"""

    def test_check_name_adapter(self, adapter: type) -> None:
        """Тестируем имя адаптера"""
        assert adapter.__name__ == 'Fueled'

    def test_methods(self, adapter: type) -> None:
        """Проверяем методы в сгенерированном адаптере"""
        methods = [
            name_method for name_method, _ in inspect.getmembers(
                adapter, predicate=inspect.isfunction
            )
        ]
        assert methods == [
            '__init__',
            'get_consumption_fuel',
            'get_remaining_fuel',
            'set_fuel'
        ]
