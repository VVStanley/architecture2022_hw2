from src.design_patterns.command import CommandInterface
from src.exceptions.command import CheckFuelCommandError
from src.fuel.fueled import FueledInterface
from src.injector import inject


class BurnFuelCommand(CommandInterface):
    """Команда сжигания топлива"""

    def __init__(self, fueled: FueledInterface) -> None:
        self.fueled = fueled

    def execute(self) -> None:
        """Уменьшаем топливо"""
        self.fueled.set_fuel(
            self.fueled.get_remaining_fuel() -  # noqa W503
            self.fueled.get_consumption_fuel()
        )


class CheckFuelCommand(CommandInterface):
    """Команда проверки остатка топлива"""

    @inject
    def __init__(self, fueled: FueledInterface) -> None:
        self.fueled = fueled

    def execute(self) -> None:
        """Проверка осталось ли топливо"""
        remaining_fuel = self.fueled.get_remaining_fuel()
        consumption_fuel = self.fueled.get_consumption_fuel()

        if remaining_fuel <= consumption_fuel:
            raise CheckFuelCommandError
