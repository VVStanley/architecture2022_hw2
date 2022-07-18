# https://pypi.org/project/injector/
from typing import Any, TypeVar, cast

libs = dict()


def inject(constructor_or_class: TypeVar) -> TypeVar:
    a = 1
    if (
        isinstance(constructor_or_class, type) and
        hasattr(constructor_or_class, '__init__')
    ):
        inject(cast(Any, constructor_or_class).__init__)
    a = 1
