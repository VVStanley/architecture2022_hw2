from collections import deque

from src.commands.loggers import LogCommand
from src.commands.moves import MoveBurnFuelCommand, RotateBurnFuelCommand
from src.design_patterns.command import CommandInterface
from src.exceptions.command import BaseCommandExceptionError
from src.exceptions.handler import ExceptionHandle
from src.exceptions.repeater import (
    BaseRepeaterExceptionError,
    OneRepeaterError,
)
from src.helpers import print_unit
from src.injector import container

queue: deque = deque()


def start() -> None:
    """Старт игры"""

    unit = container.resolve('Unit')

    print("START GAME\n")
    print_unit(unit)

    mcommand: CommandInterface = MoveBurnFuelCommand()
    rcommand: CommandInterface = RotateBurnFuelCommand()

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
        command: CommandInterface = queue.popleft()
        try:
            command.execute()
            print(f"Выполнена: {command}, команд осталось - {len(queue)}")

        except OneRepeaterError as e:
            print(f"Залогировано: {str(e)}")
            lcommand = LogCommand(str(e))
            queue.appendleft(lcommand)

        except BaseRepeaterExceptionError:
            pass

        except BaseCommandExceptionError:
            handler = ExceptionHandle(command, queue)
            handler.handle(2)

    print_unit(unit)
    print("STOP GAME")


start()
