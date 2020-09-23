# -*- coding: utf-8 -*-

"""Various tools.
"""
import json
from typing import Union

import ujson
from colorama import Fore

from diamond_eye.action import make_action


class MetaSingleton(type):
    """Singleton metaclass.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Class creation.
        """
        instance = cls._instances.get(cls)
        if instance is None:
            instance = cls._instances[cls] = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return instance


class OSErrorCatcher:
    """Context manager for OSError.
    """

    def __enter__(self):
        """Does nothing.
        """

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Print error if raised.
        """
        if exc_val:
            print(f'{exc_type}: {exc_val}')
            print(f'Traceback: {exc_tb}')


def load_json(path: str) -> dict:
    """Generic JSON loader func.
    """
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            contents = ujson.loads(file.read())
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        contents = {}
    return contents


def save_json(path: str, **kwargs) -> None:
    """Generic JSON saver func.
    """
    with open(path, mode='w', encoding='utf-8') as file:
        ujson.dump(kwargs, file, ensure_ascii=False, indent=4)
    print(Fore.LIGHTGREEN_EX + f'Saved file {path}')


def emit_and_save_event(state, filesystem, user_id: str, user_name: str,
                        version: str, branch: str, method: str, key: str,
                        value: Union[int, str, tuple]) -> None:
    """Create new event, save it to HDD and alter state.
    """
    action = make_action(
        user_id=user_id,
        user_name=user_name,
        version=version,
        action={
            'branch': branch,
            'method': method,
            'key': key,
            'value': value,
        }
    )
    state.set_variable(branch, method, key, value)
    filesystem.append_to_log(action)
