import pytest

from src.commands.actions import MoveBurnFuelCommand
from src.exceptions.command import BaseCommandExceptionError
from src.injector import container
from src.injector.register import builder
from src.injector.scope import get_scope
from src.units.unit import Unit


class TestMoveBurnFuelCommand:
    """Тестируем команду движения по прямой с расходом топлива"""

    fight_id: str
    ship: Unit

    @classmethod
    def setup_class(cls) -> None:
        cls.fight_id = '123123213'
        scope = get_scope(amount_ship=2)
        builder.register_scope(scope, cls.fight_id, name_class="Unit")
        cls.ship = [
            i for i in container.storage.get(cls.fight_id).values()
            if i.name == 'ship'
        ][0]

    def test_ok(self) -> None:
        """Проверка команды на выполнение"""

        save_position = self.ship.position  # type: ignore
        calc_remaining_fuel = (
                self.ship.remaining_fuel - self.ship.consumption_fuel
        )

        command = MoveBurnFuelCommand(self.fight_id, self.ship.id)
        command.execute()

        assert getattr(self.ship, "remaining_fuel") == calc_remaining_fuel
        assert getattr(self.ship, "position") != save_position

    def test_exceptions_check_fuel(self) -> None:
        """Если топливо закончится, возникает исключение"""

        command = MoveBurnFuelCommand(self.fight_id, self.ship.id)

        with pytest.raises(BaseCommandExceptionError) as exc_info:
            command.execute()
            command.execute()
            command.execute()
            command.execute()
            command.execute()

        assert exc_info.typename == "MoveBurnFuelCommandError"
        assert str(exc_info.value) == (
            f"unit:{self.ship.id} Ran out of fuel for unit;"  # type: ignore
        )

    def test_collection(self) -> None:
        """Проверим коллекцию у команды"""
        command = MoveBurnFuelCommand(self.fight_id, self.ship.id)

        assert 3 == len(command.collection)
