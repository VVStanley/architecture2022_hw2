class ObjectIsNotVectorTypeError(Exception):
    """Исключение возникающее при попытке сложить/сравнить
    вектор с другим объектом
    """

    def __init__(self) -> None:
        message = "Type must be Vector"
        super().__init__(message)


class CommandException(Exception):
    """Ошибка команды"""

    def __init__(self, message: str = None) -> None:
        message = message if message else "General command error"
        super(CommandException, self).__init__(message)
