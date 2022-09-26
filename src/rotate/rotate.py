from design_patterns.command import CommandInterface
from exceptions.command import RotateCommandError
from rotate.rotable import RotableInterface


class RotateCommand(CommandInterface):
    """Команда для поворота объекта"""

    def __init__(self, rotable: RotableInterface) -> None:
        self.rotable = rotable

    def execute(self) -> None:
        """Поворачиваем объект"""
        try:
            direction = (
                (
                    self.rotable.get_direction() +  # noqa W503
                    self.rotable.get_angular_velocity()
                ) / self.rotable.get_direction_number()
            )
        except AttributeError:
            raise RotateCommandError
        self.rotable.set_direction(direction)
