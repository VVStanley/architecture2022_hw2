from units.unit import Unit


def print_unit(unit: Unit) -> None:
    """Показать в консоле юнита"""
    print(unit)
    [print(attr, value) for attr, value in vars(unit).items()]
    print("--------------\n")
