class Singleton(type):
    """Метакласс для реализации паттерна Singleton."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Переопределенный вызов функции."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
