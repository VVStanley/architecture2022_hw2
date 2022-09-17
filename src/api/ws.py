import json
from loguru import logger
from fastapi import (
    APIRouter, Depends, WebSocket,
)
from starlette.websockets import WebSocketDisconnect

from injector.register import builder
from models.units import get_model_by_name
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
    await ws_manager.connect(user_id, websocket)
    try:

        await ws_manager.send_personal_message(
            message=fight_service.get_fighters_message(),
            websocket=websocket
        )
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            fight_id = fight_service.decode_token(data.get('token', ''))
            queue = q_manager.get_queue(fight_id)

            logger.info('ws --- ', data.get('step'))
            queue.put(data.get('step'))

            queue.join()

            container = builder.container
            logger.info(
                json.dumps(
                    [
                        get_model_by_name(unit.name).from_orm(unit).dict()
                        for unit in container.storage.get(fight_id).values()
                    ]
                )
            )
    #         TODO: Отправить измененые данные на фронт

    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
