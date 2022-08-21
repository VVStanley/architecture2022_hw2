class BaseCommandExceptionError(Exception):
    """Ошибка команды"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "General command error"
        super().__init__(message)


class RotateCommandError(BaseCommandExceptionError):
    """Поворот объекта"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Unit cannot be rotated"
        super().__init__(message)


class MoveCommandError(BaseCommandExceptionError):
    """Передвижение объекта"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Unit cannot move"
        super().__init__(message)


class CheckFuelCommandError(BaseCommandExceptionError):
    """Проверка топлива"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Ran out of fuel for unit"
        super().__init__(message)


class CheckBulletsCommandError(BaseCommandExceptionError):
    """Проверка наличия пуль"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Bullets ran out for unit"
        super().__init__(message)


class ShootCheckBulletCommandError(BaseCommandExceptionError):
    """Проверка пуль и выстрел"""
    pass


class MoveBurnFuelCommandError(BaseCommandExceptionError):
    """Движение с расходом топлива"""
    pass


class RotateBurnFuelCommandError(BaseCommandExceptionError):
    """Поворот с расходом топлива"""
    pass
