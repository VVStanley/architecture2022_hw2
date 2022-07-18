from src.design_patterns.command import CommandInterface
from src.exceptions import CommandExceptionError
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
        if self.fueled.get_remaining_fuel() <= 0:
            raise CommandExceptionError("Ran out of fuel for unit")
