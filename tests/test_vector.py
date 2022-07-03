"""Тестирование модуля vector"""
import pytest

from src.exceptions import ObjectIsNotVectorTypeError
from src.vector import Vector


class TestVector:
    """Тестируем действия с вектором"""

    def test_plus_no_vector(self) -> None:
        """Проверяем что векторы можно сложить"""
        a = Vector(12, 5)

        with pytest.raises(ObjectIsNotVectorTypeError) as exc_info:
            Vector.plus(a, None)  # type: ignore

        assert exc_info.typename == "ObjectIsNotVectorTypeError"
        assert str(exc_info.value) == "Type must be Vector"

        with pytest.raises(ObjectIsNotVectorTypeError) as exc_info:
            Vector.plus(None, a)  # type: ignore

        assert exc_info.typename == "ObjectIsNotVectorTypeError"
        assert str(exc_info.value) == "Type must be Vector"

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

    def test_not_eq(self) -> None:
        """Проверяем что векторы не равны"""
        a = Vector(1, 1)
        b = Vector(2, 2)

        eq_vectors = a == b

        assert eq_vectors is False

    def test_eq(self) -> None:
        """Проверяем сравнение векторов"""
        a = Vector(123, 555)
        b = Vector(123, 555)

        assert a == b

    def test_add_no_vector_type(self) -> None:
        """Проверяем что вызывается исключение если сложение не с вектором"""
        a = Vector(12, 5)

        with pytest.raises(ObjectIsNotVectorTypeError) as exc_info:
            a + None  # type: ignore

        assert exc_info.typename == "ObjectIsNotVectorTypeError"
        assert str(exc_info.value) == "Type must be Vector"
