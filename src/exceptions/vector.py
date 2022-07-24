class ObjectIsNotVectorTypeError(Exception):
    """Исключение возникающее при попытке сложить/сравнить
    вектор с другим объектом
    """

    def __init__(self) -> None:
        message = "Type must be Vector"
        super().__init__(message)
