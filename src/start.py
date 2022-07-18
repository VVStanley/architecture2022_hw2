from collections import deque

from src.commands.loggers import LogCommand
from src.commands.moves import MoveBurnFuelCommand, RotateBurnFuelCommand
from src.commands.repeater import OneRepeatCommand, TwoRepeatCommand
from src.exceptions import (
    OneRepeaterCommandError, TwoRepeaterCommandError,
)
from src.helpers import create_unit, print_unit
from src.utils.exception import can_handle, handle_exception
from src.vector import Vector

queue: deque = deque()


def start() -> None:
    """Старт игры"""
    unit = create_unit(
        remaining_fuel=10,
        consumption_fuel=3,
        position=Vector(1, 2),
        direction=7,
        angular_velocity=1,
        direction_numbers=8,
        velocity=9
    )

    print("START GAME\n")
    print_unit(unit)

    mcommand = MoveBurnFuelCommand(unit=unit)
    rcommand = RotateBurnFuelCommand(unit=unit)

    queue.append(mcommand)
    queue.append(mcommand)
    queue.append(mcommand)
    queue.append(mcommand)
    queue.append(rcommand)
    queue.append(rcommand)
    queue.append(rcommand)
    queue.append(rcommand)
    queue.append(rcommand)

    while queue:
        command = queue.popleft()
        try:
            command.execute()

        except OneRepeaterCommandError as e:
            # TODO: Когда отрабатывает OneRepeatCommand
            #  мы не хнаем какая команда исполнялась
            if can_handle(e.__class__.__name__):
                repeatcommand = handle_exception.get(e.__class__.__name__)
                repeater = TwoRepeatCommand(repeatcommand(unit=unit))
                queue.appendleft(repeater)

        except TwoRepeaterCommandError as e:
            lcommand = LogCommand(str(e))
            queue.appendleft(lcommand)

        except Exception as e:
            if can_handle(e.__class__.__name__):
                repeatcommand = handle_exception.get(e.__class__.__name__)
                repeater = OneRepeatCommand(repeatcommand(unit=unit))
                queue.appendleft(repeater)

    print_unit(unit)
    print("STOP GAME")


start()
