class DependencyResolutionExceptionError(Exception):
    """Ошибка разрешения зависимостей"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Dependency resolution error"
        super().__init__(message)
