from src.utils.vector import Vector

# TODO: Доработать IoC
scope = {
    "full": {
        "Unit": {
            "fields": {
                "remaining_fuel": 15,
                "consumption_fuel": 3,
                "position": Vector(1, 2),
                "direction": 7,
                "angular_velocity": 1,
                "direction_numbers": 8,
                "velocity": 9
            }
        }
    },
    "not_rotable": {
        "Unit": {
            "fields": {
                "remaining_fuel": 10,
                "consumption_fuel": 3,
                "position": Vector(1, 2),
                "velocity": 9
            }
        }
    }
}


def get_actual_scope(name_scope: str = "full") -> dict:
    """Возвращаем настройки для игры"""
    return scope.get(name_scope, {})
