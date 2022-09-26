from fuel.fuel import BurnFuelCommand, CheckFuelCommand
from fuel.fueled import FueledInterface
from injector.builder import ContainerBuilder
from injector.container import Container
from move.movable import MovableInterface
from move.move import MoveCommand
from rotate.rotable import RotableInterface
from rotate.rotate import RotateCommand
from shoot.shoot import CheckBulletsCommand, ShootCommand
from shoot.shooting import ShootingInterface
from units.unit import Unit


def get_container() -> Container:
    """ Building IoC container """
    builder = ContainerBuilder()

    builder.register_class(Unit)

    adapter = builder.generate_adapter(interface=FueledInterface)
    builder.register_class(adapter)
    adapter = builder.generate_adapter(interface=MovableInterface)
    builder.register_class(adapter)
    adapter = builder.generate_adapter(interface=RotableInterface)
    builder.register_class(adapter)
    adapter = builder.generate_adapter(interface=ShootingInterface)
    builder.register_class(adapter)

    builder.register_class(CheckFuelCommand)
    builder.register_class(MoveCommand)
    builder.register_class(RotateCommand)
    builder.register_class(BurnFuelCommand)
    builder.register_class(CheckBulletsCommand)
    builder.register_class(ShootCommand)

    return builder.container


container = get_container()
