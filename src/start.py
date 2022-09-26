from collections import deque

from client import api_commands
from commands import act
from commands.loggers import LogCommand
from exceptions.command import BaseCommandExceptionError
from exceptions.handler import ExceptionHandle
from exceptions.repeater import (
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
