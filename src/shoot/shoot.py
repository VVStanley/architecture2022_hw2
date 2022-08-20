from src.design_patterns.command import CommandInterface
from src.shoot.shooting import ShootingInterface


class ShootCommand(CommandInterface):
    """Команда для выстрела"""

    def __int__(self, shooting: ShootingInterface):
        self.shooting = shooting

    def execute(self) -> None:
        """Стреляем"""
        if self.shooting.check_bullets():
            self.shooting.shoot()
