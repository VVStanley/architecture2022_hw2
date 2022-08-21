from typing import Dict


class Singleton(type):
    """Метакласс для реализации паттерна Singleton."""
    _instances: Dict['type', 'type'] = {}

    def __call__(cls, *args, **kwargs) -> type:  # type: ignore
        """Переопределенный вызов функции."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
