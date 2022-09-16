from src.fuel.fuel import BurnFuelCommand, CheckFuelCommand
from src.fuel.fueled import FueledInterface
from src.injector.builder import ContainerBuilder
from src.move.movable import MovableInterface
from src.move.move import MoveCommand
from src.rotate.rotable import RotableInterface
from src.rotate.rotate import RotateCommand
from src.shoot.shoot import CheckBulletsCommand, ShootCommand
from src.shoot.shooting import ShootingInterface
from src.units.unit import Unit

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

container = builder.container
