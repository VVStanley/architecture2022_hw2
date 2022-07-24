from src.units.unit import Unit


def create_unit(**kwargs) -> Unit:  # type: ignore
    """Создание юнита"""
    unit = Unit()
    unit.name = kwargs.get("name", "Warship hero")

    for key, value in kwargs.items():
        setattr(unit, key, value)

    return unit


def print_unit(unit: Unit) -> None:
    """Показать в консоле юнита"""
    print(unit)
    [print(attr, value) for attr, value in vars(unit).items()]
    print("--------------\n")
