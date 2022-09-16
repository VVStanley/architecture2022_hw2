from collections import deque

from src.client import api_commands
from src.commands import act
from src.commands.loggers import LogCommand
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
        command = act.get(api_command.get("command"))  # type: ignore
        queue.append(command(api_command.get("id")))  # type: ignore

    while queue:
        command = queue.popleft()
        try:
            command.execute()
            print(f"Выполнена: {command}, команд осталось - {len(queue)}")

        except OneRepeaterError as e:
            print(f"Логирование: {str(e)}")
            log_command = LogCommand(str(e))
            queue.appendleft(log_command)

        except BaseRepeaterExceptionError:
            pass

        except BaseCommandExceptionError:
            handler = ExceptionHandle(command, queue)
            handler.handle(2)

    print("STOP GAME")


# /uri/id_game

# https://www.youtube.com/watch?v=mlDanE_-0mY&t=962s

start()
