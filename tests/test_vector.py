"""Тестирование модуля vector"""
import pytest

from src.exceptions import ObjectNotMovableError
from src.vector import Vector


class TestVector:
    """Тестируем действия с вектором"""

    def test_plus_no_vector(self) -> None:
        """Проверяем что векторы можно сложить"""
        a = Vector(12, 5)

        with pytest.raises(ObjectNotMovableError) as exc_info:
            Vector.plus(a, None)  # type: ignore

        assert exc_info.typename == "ObjectNotMovableError"
        assert str(exc_info.value) == "Этот объект не двигается"

        with pytest.raises(ObjectNotMovableError) as exc_info:
            Vector.plus(None, a)  # type: ignore

        assert exc_info.typename == "ObjectNotMovableError"
        assert str(exc_info.value) == "Этот объект не двигается"

    def test_plus(self) -> None:
        """Тестируем метод сложения векторов"""
        a = Vector(12, 5)
        b = Vector(-7, 3)

        c = Vector.plus(a, b)

        assert c.x == 5
        assert c.y == 8

    def test_add(self) -> None:
        """Складываем два вектора"""
        a = Vector(12, 5)
        b = Vector(-7, 3)

        c = a + b

        assert c.x == 5
        assert c.y == 8

    def test_add_no_vector_type(self) -> None:
        """Проверяем что вызывается исключение если сложение не с вектором"""
        a = Vector(12, 5)

        with pytest.raises(ObjectNotMovableError) as exc_info:
            a + None  # type: ignore

        assert exc_info.typename == "ObjectNotMovableError"
        assert str(exc_info.value) == "Этот объект не двигается"
