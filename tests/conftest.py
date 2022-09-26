import uuid
from typing import List
from unittest.mock import MagicMock, Mock

import pytest
from passlib.hash import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database
from starlette.testclient import TestClient

from app import app
from commands.iterator import CommandCollection
from db import db_User
from db.database import Base, SQLALCHEMY_DATABASE_URL, get_session
from design_patterns.command import CommandInterface
from fuel.fuel import BurnFuelCommand, CheckFuelCommand
from move.move import MoveCommand
from project.settings import settings
from rotate.rotate import RotateCommand
from utils.vector import Vector

if settings.TESTING:
    SQLALCHEMY_DATABASE_URL_TEST = SQLALCHEMY_DATABASE_URL + '_test'
else:
    SQLALCHEMY_DATABASE_URL_TEST = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL_TEST, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


def get_test_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    if database_exists(SQLALCHEMY_DATABASE_URL_TEST):
        drop_database(SQLALCHEMY_DATABASE_URL_TEST)
    create_database(SQLALCHEMY_DATABASE_URL_TEST)
    Base.metadata.create_all(engine)
    app.dependency_overrides[get_session] = get_test_db
    yield
    drop_database(SQLALCHEMY_DATABASE_URL_TEST)


@pytest.fixture(scope="session")
def test_db_session():
    session_local = sessionmaker(bind=engine)
    session = session_local()
    yield session
    session.close()


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="class")
def create_users(test_db_session):
    user1 = db_User(
        username=uuid.uuid4().hex[:7],
        password_hash=bcrypt.hash("11111"),
    )
    user2 = db_User(
        username=uuid.uuid4().hex[:7],
        password_hash=bcrypt.hash("11111"),
    )
    test_db_session.add(user1)
    test_db_session.add(user2)
    test_db_session.commit()
    return user1, user2


@pytest.fixture
def rotate_command() -> CommandInterface:
    rotable = Mock()
    rotable.get_direction = MagicMock(return_value=3)
    rotable.get_angular_velocity = MagicMock(return_value=2)
    rotable.get_direction_number = MagicMock(return_value=8)
    return RotateCommand(rotable)


@pytest.fixture
def move_command() -> CommandInterface:
    movable = Mock()
    movable.get_position = MagicMock(return_value=Vector(12, 5))
    movable.get_velocity = MagicMock(return_value=Vector(-7, 3))
    return MoveCommand(movable)


@pytest.fixture
def burn_fuel_command() -> CommandInterface:
    fueled = Mock()
    fueled.get_remaining_fuel = MagicMock(return_value=300)
    fueled.get_consumption_fuel = MagicMock(return_value=2)
    return BurnFuelCommand(fueled)


@pytest.fixture
def check_fuel_command() -> CommandInterface:
    fueled = Mock()
    fueled.get_remaining_fuel = MagicMock(return_value=25)
    fueled.get_consumption_fuel = MagicMock(return_value=2)
    return CheckFuelCommand(fueled)


@pytest.fixture
def check_fuel_command_with_exception() -> CommandInterface:
    fueled = Mock()
    fueled.get_remaining_fuel = MagicMock(return_value=0)
    fueled.get_consumption_fuel = MagicMock(return_value=2)
    return CheckFuelCommand(fueled)


@pytest.fixture
def get_exception_commands(
    rotate_command: Mock,
    check_fuel_command: Mock,
    move_command: Mock,
    burn_fuel_command: Mock,
    check_fuel_command_with_exception: Mock
) -> CommandCollection:
    collection = CommandCollection()
    collection.add_item(check_fuel_command)
    collection.add_item(move_command)
    collection.add_item(burn_fuel_command)
    collection.add_item(check_fuel_command_with_exception)
    collection.add_item(move_command)
    collection.add_item(burn_fuel_command)
    return collection


@pytest.fixture
def get_execute_commands(
    rotate_command: Mock,
    move_command: Mock,
    burn_fuel_command: Mock,
    check_fuel_command: Mock
) -> List[CommandInterface]:
    return [
        move_command, burn_fuel_command, check_fuel_command,
        rotate_command, burn_fuel_command, check_fuel_command,
        move_command, burn_fuel_command, check_fuel_command,
        move_command, burn_fuel_command, check_fuel_command,
        move_command, burn_fuel_command, check_fuel_command,
        rotate_command, burn_fuel_command, check_fuel_command,
        move_command, burn_fuel_command, check_fuel_command,
    ]
