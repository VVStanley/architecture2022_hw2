from collections import deque

from src.client import api_commands
from src.commands import act
from src.commands.loggers import LogCommand
from src.design_patterns.command import CommandInterface
from src.exceptions.command import BaseCommandExceptionError
from src.exceptions.handler import ExceptionHandle
from src.exceptions.repeater import (
    BaseRepeaterExceptionError,
    OneRepeaterError,
)

queue: deque = deque()


def start() -> None:
    """Старт игры"""

    print("START GAME\n")

    for api_command in api_commands:
        command: CommandInterface = act.get(api_command.get("command"))
        queue.append(command(api_command.get("id")))

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

    print("STOP GAME")


start()
