import json

from fastapi import (
    APIRouter, Depends, WebSocket,
)
from starlette.websockets import WebSocketDisconnect

from models.tokens import GameToken
from services.fights import FightService
from services.queue import q_manager
from services.ws import ws_manager

router = APIRouter(prefix="/ws", tags=["ws"])


@router.websocket("/{user_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    user_id: int,
    fight_service: FightService = Depends()
):
    """Точка для обмена данными с агентом
    :param websocket: Вебсокет соединения.
    :param user_id: ИД пользователя с кем создаем соединение.
    :param fight_service: Сервис для обработки битвы.
    """
    await ws_manager.connect(user_id, websocket)
    try:
        # При соединении отправляем информацию о всех активных игроках
        await ws_manager.send_personal_message(
            message=fight_service.get_fighters_message(),
            websocket=websocket
        )
        while True:
            # Ожидаем команды
            command = await websocket.receive_text()
            command = json.loads(command)

            # Проверяем токен битвы
            token = command.get('token', '')
            payload = fight_service.decode_token(token)
            fight_id = payload.get('sub')

            # Получаем очередь для битвы и добавляем в нее команду
            queue = q_manager.get_queue(fight_id)
            queue.put(command.get('step'))
            queue.join()

            # Отправляем данные битвы агенту
            users_id = payload.get('users', []).keys()
            await ws_manager.broadcast(
                users_id=users_id,
                message=GameToken(
                    token=token,
                    data=fight_service.get_data_fight(fight_id)
                ).dict()
            )

    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
