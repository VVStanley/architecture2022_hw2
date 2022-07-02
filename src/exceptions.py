class ObjectNotMovableError(Exception):
    """Исключение возникающее если сдвигают неподвижный объект"""

    def __init__(self) -> None:
        message = "Этот объект не двигается"
        super().__init__(message)
