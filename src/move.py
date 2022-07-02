from src.movable import MovableInterface


class Move:
    """Команда движения объекта"""

    def __init__(self, movable: MovableInterface) -> None:
        self.movable = movable

    def execute(self) -> None:
        """Перемещаем объект"""
        self.movable.set_position(
            self.movable.get_position() + self.movable.get_velocity()
        )
