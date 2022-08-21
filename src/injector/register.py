from src.fuel.fuel import BurnFuelCommand, CheckFuelCommand
from src.fuel.fueled import Fueled
from src.injector.builder import ContainerBuilder
from src.move.movable import Movable
from src.move.move import MoveCommand
from src.rotate.rotable import Rotable
from src.rotate.rotate import RotateCommand
from src.shoot.shoot import CheckBulletsCommand, ShootCommand
from src.shoot.shooting import Shooting
from src.units.unit import Unit

builder = ContainerBuilder()

builder.register_class(Unit)
builder.register_class(Fueled)
builder.register_class(Movable)
builder.register_class(Rotable)
builder.register_class(Shooting)
builder.register_class(CheckFuelCommand)
builder.register_class(MoveCommand)
builder.register_class(RotateCommand)
builder.register_class(BurnFuelCommand)
builder.register_class(CheckBulletsCommand)
builder.register_class(ShootCommand)

builder.register_scope(name_scope="units", name_class="Unit")

container = builder.container
