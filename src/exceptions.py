class OtherMustByVectorInterfaceError(Exception):
    """Исключение возникающее если вектор складывают не с другим объектом"""

    def __init__(self) -> None:
        message = "Складывать можно только векторы"
        super().__init__(message)
