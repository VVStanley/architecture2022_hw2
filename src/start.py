from src.examples import move_and_burn_fuel
from src.units.unit import Unit
from src.vector import Vector


def create_unit(**kwargs) -> Unit:  # type: ignore
    """Создание юнита"""
    unit = Unit()
    unit.name = kwargs.get("name", "Warship hero")
    unit.remaining_fuel = kwargs.get("remaining_fuel")
    unit.consumption_fuel = kwargs.get("consumption_fuel")
    unit.position = kwargs.get("position")
    unit.direction = kwargs.get("direction")
    unit.directions_number = kwargs.get("directions_number")
    unit.velocity = kwargs.get("velocity")
    return unit


def print_unit(unit: Unit) -> None:
    """Показать в консоле юнита"""
    print(unit)
    [print(attr, value) for attr, value in vars(unit).items()]
    print("--------------")


def start() -> None:
    print("START GAME\n")

    unit = create_unit(
        remaining_fuel=400,
        consumption_fuel=1,
        position=Vector(1, 2),
        direction=1,
        directions_number=1,
        velocity=1,
    )

    print_unit(unit)

    move_and_burn_fuel(unit=unit)

    print_unit(unit)

    print("STOP GAME")


start()
