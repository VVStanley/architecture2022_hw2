from src.utils.vector import Vector

TECHNICAL_ARGUMENTS = (
    "amount",  # Кол-во создаваемых объектов
)

scope = {
    "full": [
        {
            "amount": 3,
            "fields": {
                "id": Auto(int),
                "name": "wall",
                "position": Auto(Vector)
            }
        },
        ...  # другие юниты
    ],
}

# TODO: !!!!!!!!!!
"""
Создавать надо все юниты в отдельный контейнер,
ИД юнитов в доступе.
 
остальные классы просто регистрировать.

Очередь комманд
Читаем с очереди команду и инициализируем с юнитом по ИД
"""


def get_actual_scope(name_scope: str = "full") -> dict:
    """Возвращаем настройки для игры"""
    return scope.get(name_scope, {})
