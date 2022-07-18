class ObjectIsNotVectorTypeError(Exception):
    """Исключение возникающее при попытке сложить/сравнить
    вектор с другим объектом
    """

    def __init__(self) -> None:
        message = "Type must be Vector"
        super().__init__(message)


class CommandExceptionError(Exception):
    """Ошибка команды"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "General command error"
        super().__init__(message)


class RotateCommandError(CommandExceptionError):
    """Поворот объекта"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Unit cannot be rotated"
        super().__init__(message)


class MoveCommandError(CommandExceptionError):
    """Передвижение объекта"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Unit cannot move"
        super().__init__(message)


class CheckFuelCommandError(CommandExceptionError):
    """Проверка топлива"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Ran out of fuel for unit"
        super().__init__(message)


class TwoRepeaterCommandError(CommandExceptionError):
    """Повторное выполнение"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Command repeat with error"
        super().__init__(message)


class ThreeRepeaterCommandError(CommandExceptionError):
    """Повторное выполнение"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Command repeat with error"
        super().__init__(message)


class OneRepeaterCommandError(CommandExceptionError):
    """Повторное выполнение"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Command repeat with error"
        super().__init__(message)


class MoveBurnFuelCommandError(CommandExceptionError):
    """Движение с расходом топлива"""
    pass


class RotateBurnFuelCommandError(CommandExceptionError):
    """Поворот с расходом топлива"""
    pass
