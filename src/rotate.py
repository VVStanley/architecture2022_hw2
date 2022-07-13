from src.design_patterns.command import CommandInterface
from src.rotable import RotableInterface


class Rotate(CommandInterface):
    """Команда для поворота объекта"""

    def __init__(self, rotable: RotableInterface) -> None:
        self.rotable = rotable

    def execute(self) -> None:
        """Поворачиваем объект"""
        self.rotable.set_direction(
            (
                self.rotable.get_direction() +  # noqa W503
                self.rotable.get_angular_velocity()
            ) / self.rotable.get_direction_number()
        )
