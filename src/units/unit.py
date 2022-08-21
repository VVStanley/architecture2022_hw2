from typing import Any


class Unit:
    """Боевая еденица"""

    def __init__(self, **kwargs: dict) -> None:
        """Создаем юнита"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """Строковое представление"""
        prefix = "Unit:"
        name = "unknown fighter"
        if hasattr(self, "name"):
            name = str(self.name)  # type: ignore
        return f"{prefix} {name}"

    def __setattr__(self, key: str, value: Any) -> None:
        """Устанавливаем атрибут при обращении"""
        self.__dict__[key] = value
