from src.design_patterns.command import CommandInterface
from src.exceptions.command import CheckBulletsCommandError
from src.shoot.shooting import ShootingInterface


class ShootCommand(CommandInterface):
    """Команда для выстрела"""

    def __init__(self, shooting: ShootingInterface):
        self.shooting = shooting

    def execute(self) -> None:
        """Стреляем"""
        self.shooting.shoot()


class CheckBulletsCommand(CommandInterface):
    """Проверяем наличие пуль перед выстрелом"""

    def __init__(self, shooting: ShootingInterface):
        self.shooting = shooting

    def execute(self) -> None:
        """Проверяем пули"""
        if not self.shooting.check_bullets():
            raise CheckBulletsCommandError
