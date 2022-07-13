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
        super(CommandExceptionError, self).__init__(message)
