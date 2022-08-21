from src.fuel.fuel import BurnFuelCommand, CheckFuelCommand
from src.fuel.fueled import Fueled
from src.injectorOLD.container import Container, ContainerBuilder
from src.injectorOLD.scope import get_actual_scope
from src.move.movable import Movable
from src.move.move import MoveCommand
from src.rotate.rotable import Rotable
from src.rotate.rotate import RotateCommand
from src.units.unit import Unit

builder = ContainerBuilder()

builder.register_class(Unit)
builder.register_class(Fueled)
builder.register_class(Movable)
builder.register_class(Rotable)
builder.register_class(CheckFuelCommand)
builder.register_class(MoveCommand)
builder.register_class(RotateCommand)
builder.register_class(BurnFuelCommand)

scope = get_actual_scope()

container: Container = builder.build(scope=scope)
