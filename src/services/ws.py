from typing import Dict, List

from fastapi import WebSocket


class ConnectionManager:
    """Менеджер для работы с вебсокетами"""

    def __init__(self) -> None:
        self.active_connections: Dict[int, WebSocket] = {}

    async def connect(self, user_id: int, websocket: WebSocket) -> None:
        """Создаем соединение с новым вебсокетом.
        :param user_id: Ид пользователя для которого создано соединение.
        :param websocket: websocket.
        """
        await websocket.accept()
        self.active_connections.update({user_id: websocket})

    async def disconnect(self, user_id: int) -> None:
        """Закрываем соединение"""
        websocket = self.active_connections.pop(user_id, None)
        if websocket:
            await websocket.close()

    @staticmethod
    async def send_personal_message(
        message: str, websocket: WebSocket
    ) -> None:
        """Отправка сообщения на конкретный сокет"""
        await websocket.send_json(message)

    async def broadcast(self, users_id: List[int], message: Dict) -> None:
        """ Отправка сообщений на несколько вебсокетов.
        :param users_id: ИД пользователей, которым будет отправлено сообщение.
        :param message: Сообщение.
        """
        for user_id in users_id:
            connection = self.active_connections.get(int(user_id))
            if connection:
                await connection.send_json(message)


ws_manager = ConnectionManager()
