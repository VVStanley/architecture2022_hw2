# https://pypi.org/project/injector/

from typing import Any, TypeVar

from src.fuel.fuel import CheckFuelCommand

classes = {
    "CheckFuelCommand": CheckFuelCommand
}


class IoC:

    def resolve(self, name: str, func: Any):
        self.func = func
        self.name = name


ioc = IoC()
