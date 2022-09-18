from datetime import datetime, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from db import db_User
from db.database import get_session
from exceptions.auth import (
    CouldNotValidateCredantialError, IncorrectCredantialError,
    UserValidationError,
)
from models import Token, User, UserCreate
from project.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in/')


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Возвращаем текущего пользователя"""
    return AuthService.verify_token(token)


class AuthService:
    """Сервис аутентификации"""

    @classmethod
    def verify_password(cls, raw_password: str, hashed_password: str) -> bool:
        """Валидация пароля

        :param raw_password: пароль с формы
        :param hashed_password: хеш пароля с БД
        """
        return bcrypt.verify(raw_password, hashed_password)

    @classmethod
    def hash_password(cls, raw_password: str) -> str:
        """Хеширование пароля

        :param raw_password: пароль с формы
        """
        return bcrypt.hash(raw_password)

    @classmethod
    def verify_token(cls, token: str) -> User:
        """Валидация токена

        :param token: токен с клиента
        """
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            raise CouldNotValidateCredantialError

        user_data = payload.get('user')

        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise CouldNotValidateCredantialError

        return user

    @classmethod
    def create_token(cls, db_user: db_User) -> Token:
        """Создание токена

        :param db_user: пользователь из БД
        """
        db_user_data = User.from_orm(db_user)
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expires_s),
            'sub': str(db_user_data.id),
            'user': db_user_data.dict(exclude={'fight'}),
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        return Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session: Session = session

    def get_user_by_username(self, username: str) -> db_User:
        """Получить пользователя по username"""
        return (
            self.session.query(db_User)
            .filter(db_User.username == username).first()
        )

    def register_new_user(self, user_data: UserCreate) -> Token:
        """Регистрируем нового пользователя"""
        user = self.get_user_by_username(user_data.username)
        if user:
            raise UserValidationError(
                'Пользователь с таким username уже существует'
            )

        user = db_User(
            username=user_data.username,
            password_hash=self.hash_password(user_data.password),
        )
        self.session.add(user)
        self.session.commit()
        return self.create_token(user)

    def authenticate_user(self, username: str, password: str, ) -> Token:
        """Аутентификация пользователя"""
        user = self.get_user_by_username(username)

        if not user:
            raise IncorrectCredantialError

        if not self.verify_password(password, user.password_hash):
            raise IncorrectCredantialError

        return self.create_token(user)
