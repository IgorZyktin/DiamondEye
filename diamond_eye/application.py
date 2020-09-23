# -*- coding: utf-8 -*-

"""Main component of the system.
"""
import uuid
from typing import Set

from diamond_eye.action import make_action
from diamond_eye.utils import MetaSingleton


class Application(metaclass=MetaSingleton):
    """Main component of the system.
    """

    @staticmethod
    def issue_new_uuid(known_uuids: Set[str]) -> str:
        """Generate new unique id that do not interfere with existing ones.
        """
        new_uuid = str(uuid.uuid4())

        while new_uuid in known_uuids:
            new_uuid = str(uuid.uuid4())

        return new_uuid

    def issue_and_save_new_uuid(self, state) -> str:
        """Generate and save the new id.
        """
        known_uuids = state.get_variable('app', 'known_uuids', set())
        new_uuid = self.issue_new_uuid(known_uuids)
        state.set_variable('app', 'add', 'known_uuids', new_uuid)
        return new_uuid

    def register_new_user(self, user_name: str, state, filesystem) -> None:
        """Issue new id, save it to the state and filesystem.
        """
        user_id = self.issue_and_save_new_uuid(state)

        filesystem.save_user_key(user_name, user_id)

        state.set_variable('app', 'set', 'user_id', user_id)
        state.set_variable('app', 'set', 'user_name', user_name)

        action = make_action(
            user_id=user_id,
            user_name=user_name,
            version=state.get_variable('app', 'version'),
            action={
                'branch': 'app',
                'method': 'add',
                'key': 'known_users',
                'value': user_name
            }
        )
        filesystem.append_to_log(action)
