from src.rotable import RotableInterface


class Potate:
    """Команда для поворота объекта"""

    def __init__(self, rotable: RotableInterface) -> None:
        self.rotable = rotable

    def execute(self) -> None:
        """Поворачиваем объект"""
        self.rotable.set_direction(
            int(
                (
                    self.rotable.get_direction() +
                    self.rotable.get_angular_velocity()
                ) / self.rotable.get_direction_number()
            )
        )
