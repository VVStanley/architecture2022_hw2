class BaseRepeaterExceptionError(Exception):
    """Ошибка команды"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "General repeater error"
        super().__init__(message)


class TwoRepeaterError(BaseRepeaterExceptionError):
    """Повторное выполнение"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Command repeat with error"
        super().__init__(message)


class ThreeRepeaterError(BaseRepeaterExceptionError):
    """Повторное выполнение"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Command repeat with error"
        super().__init__(message)


class OneRepeaterError(BaseRepeaterExceptionError):
    """Повторное выполнение"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "Command repeat with error"
        super().__init__(message)
