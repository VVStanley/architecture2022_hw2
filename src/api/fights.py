from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db import db_Fight, db_User
from db.database import get_session
from models import Fighter
from models.tokens import GameToken
from services.fights import FightService
from services.ws import ws_manager

router = APIRouter(prefix='/fights', tags=['fights'])


@router.post("/ready/", status_code=status.HTTP_204_NO_CONTENT)
async def ready_to_fight(
    user: Fighter,
    session: Session = Depends(get_session),
    fight_service: FightService = Depends()
):
    """Меняем статус игрока и отправляем активных игроков всем участникам"""
    db_user = (
        session.query(db_User)
        .filter(db_User.id == user.id).first()
    )
    setattr(db_user, 'ready_to_fight', user.ready_to_fight)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    await ws_manager.broadcast(message=fight_service.get_fighters_message())
    return {"ok": True}


@router.get("", status_code=status.HTTP_200_OK)
def get_fights(session: Session = Depends(get_session)):
    """Получаем все текущие битвы"""
    fights = session.query(db_Fight).all()
    return {"fights": fights}


@router.get(
    "/add/", response_model=GameToken, status_code=status.HTTP_201_CREATED
)
def create_fight(ids: str, fight_service: FightService = Depends()):
    """Создание новой битвы.
    :param ids: ИД пользователей для создания игры.
    :param fight_service: Сервис для обработки битвы.
    """
    ids = ids.split(',')
    token: GameToken = fight_service.create_fight(ids)
    return token
