import uuid
from datetime import datetime, timedelta
from typing import Any, Dict, List

from fastapi import Depends
from jose import JWTError, jwt
from loguru import logger
from sqlalchemy.orm import Session
from threading import Lock
from db import db_Fight, db_User
from db.database import get_session
from exceptions.auth import CouldNotValidateCredantialError
from injector.register import builder
from injector.scope import get_scope
from models import Fighter, User
from models.tokens import GameToken
from models.units import get_model_by_name
from project.settings import settings
from services.queue import q_manager
from services.thread import FightThread


class FightService:
    """Сервис для сражений"""

    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session: Session = session

    @staticmethod
    def _user_to_dict(user: db_User, db_fight: db_Fight) -> dict:
        user.fight = db_fight
        return User.from_orm(user).dict()

    @staticmethod
    def decode_token(token: str) -> str:
        """ Раскодируем токен и получим ИД боя """
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            raise CouldNotValidateCredantialError

        return payload.get('sub')

    @staticmethod
    def create_token(db_users: List[db_User], fight_id: str) -> str:
        """Токен для игры"""
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=86400),
            'sub': fight_id,
            'users': {
                user.id: Fighter.from_orm(user).dict() for user in db_users
            },
        }
        return jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )

    def create_fight(self, ids: List[str]) -> GameToken:
        """Создаем битву"""
        db_users = (
            self.session.query(db_User).filter(db_User.id.in_(ids)).all()
        )
        # Генерируем уникальный ИД для битвы
        fight_id = uuid.uuid4().hex

        # Создаем токен для битвы
        token = self.create_token(db_users, fight_id)

        # Сохраняем битву в БД
        db_fight = db_Fight(id=fight_id, token=token)
        self.session.bulk_update_mappings(
            db_User, [self._user_to_dict(user, db_fight) for user in db_users]
        )
        self.session.add(db_fight)
        self.session.commit()
        self.session.refresh(db_fight)

        # Регистрируем новый скоуп с юнитами
        self._register_scope(len(ids), fight_id)

        # Создаем очередь для новой битвы и поток лдя нее
        queue = q_manager.create_queue(fight_id=fight_id)
        thread = FightThread(queue=queue, fight_id=fight_id)
        thread.start()

        return GameToken(
            token=token,
            data=self.get_data_fight(fight_id)
        )

    @staticmethod
    def get_data_fight(fight_id: str) -> List[dict]:
        """Возвращаем данные игры по ИД"""
        container = builder.container
        return [
            get_model_by_name(unit.name).from_orm(unit).dict()
            for unit in container.storage.get(fight_id).values()
        ]

    @staticmethod
    def _register_scope(amount_users: int, fight_id: str):
        """Регистрируем scope для игры"""
        scope = get_scope(amount_ship=amount_users)
        builder.register_scope(scope, fight_id, name_class="Unit")

    def get_fighters_message(self) -> Dict[str, List[Any]]:
        """Возвращаем бойцов готовых к бою"""
        db_fighters = (
            self.session.query(db_User)
            .filter(db_User.ready_to_fight == True).all()
        )
        return {
            "fighters": [
                Fighter.from_orm(fighter).json()
                for fighter in db_fighters
            ]
        }
