from src.exceptions import CommandExceptionError
from src.fueled import FueledInterface


class BurnFuel:
    """Команда сжигания топлива"""

    def __init__(self, fueled: FueledInterface) -> None:
        self.fueled = fueled

    def execute(self) -> None:
        """Уменьшаем топливо"""
        self.fueled.set_fuel(
            self.fueled.get_remaining_fuel() -  # noqa W503
            self.fueled.get_fuel_consumption()
        )


class CheckFuel:
    """Команда проверки остатка топлива"""

    def __init__(self, fueled: FueledInterface) -> None:
        self.fueled = fueled

    def execute(self) -> None:
        """Проверка осталось ли топливо"""
        if self.fueled.get_remaining_fuel() <= 0:
            raise CommandExceptionError(
                f"Ran out of fuel for unit: {self.fueled}"
            )
