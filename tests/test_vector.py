"""Тестирование вектора"""
import pytest

from src.exceptions import OtherMustByVectorInterfaceError
from src.vector import Vector


class TestVector:
    """Тестируем действия с вектором"""

    def test_add(self) -> None:
        """Проверяем что векторы можнро сложить"""
        a = Vector(12, 5)
        b = Vector(-7, 3)

        c = a + b

        assert c.x == 5
        assert c.y == 8

    def test_add_no_vector_type(self) -> None:
        """Проверяем что вызывается исключение если сложение не с вектором"""
        a = Vector(12, 5)

        with pytest.raises(OtherMustByVectorInterfaceError) as exc_info:
            a + 10  # type: ignore

        assert exc_info.typename == "OtherMustByVectorInterfaceError"
        assert str(exc_info.value) == "Складывать можно только векторы"
