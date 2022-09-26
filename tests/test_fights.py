""" Tests fight """
import random
import threading
from typing import List

from jose import jwt

from project.settings import settings


class TestFight:
    """ Тесты для боя """

    def test_create_fight(self, client, test_db_session, create_users):
        """ Тест, который проверяет, что после команды старт поток запущен """

        users_id = [user.id for user in create_users]
        response = client.get(
            f'fights/add/?ids={",".join(map(str, users_id))}'
        )

        payload = self._decode_token(token=response.json()['token'])
        fight_thread = self._get_thread(fight_id=payload['sub'])

        assert fight_thread.is_alive() is True

    def test_hard_stop(self, client, test_db_session, create_users):
        """ Тест, который проверяет, что после команды hard stop,
        поток завершается
        """
        users_id = [user.id for user in create_users]
        response = client.get(
            f'fights/add/?ids={",".join(map(str, users_id))}'
        )
        content = response.json()

        payload = self._decode_token(token=content['token'])
        fight_thread = self._get_thread(fight_id=payload['sub'])

        ships_id = [
            unit['id'] for unit in content['data'] if unit['name'] == 'ship'
        ]
        commands = self._get_commands(ships_id, "hard_stop", 12)

        for command in commands:
            fight_thread.queue.put(command)

        fight_thread.join()

        assert fight_thread.is_alive() is False
        assert fight_thread.queue.qsize() == 12

    def test_soft_stop(self, client, test_db_session, create_users):
        """ Тест, который проверяет, что после команды soft stop,
        поток завершается только после того, как все задачи закончились
        """
        users_id = [user.id for user in create_users]
        response = client.get(
            f'fights/add/?ids={",".join(map(str, users_id))}'
        )
        content = response.json()

        payload = self._decode_token(token=response.json()['token'])
        fight_thread = self._get_thread(fight_id=payload['sub'])

        ships_id = [
            unit['id'] for unit in content['data'] if unit['name'] == 'ship'
        ]
        commands = self._get_commands(ships_id, "soft_stop", 12)

        for command in commands:
            fight_thread.queue.put(command)

        fight_thread.join()

        assert fight_thread.is_alive() is False
        assert fight_thread.queue.qsize() == 0

    @staticmethod
    def _get_commands(
        users_id: List[int], state: str, len_tail: int
    ) -> List[dict]:
        commands = [
            {
                "id": random.choice(users_id),
                "command": "MoveBurnFuelCommand",
                "state": "read_command"
            } for _ in range(9)
        ]
        commands.append(
            {
                "id": random.choice(users_id),
                "command": "MoveBurnFuelCommand",
                "state": state,
            }
        )
        commands_tail = [
            {
                "id": random.choice(users_id),
                "command": "RotateBurnFuelCommand",
                "state": "read_command"
            } for _ in range(len_tail)
        ]
        commands.extend(commands_tail)
        return commands

    @staticmethod
    def _decode_token(token: str):
        return jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=[settings.jwt_algorithm],
        )

    @staticmethod
    def _get_thread(fight_id: str):
        return [
            thread for thread in threading.enumerate()
            if thread.name == fight_id
        ][0]
