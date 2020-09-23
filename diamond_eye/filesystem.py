# -*- coding: utf-8 -*-

"""Component that manages actual work with files.
"""
import os
import pickle
import shutil
from pathlib import Path
from typing import Dict, List

import ujson
from colorama import Fore

from diamond_eye.utils import (
    OSErrorCatcher, load_json, save_json, MetaSingleton
)


class FileSystem(metaclass=MetaSingleton):
    """Component that manages actual work with files.
    """

    def __init__(self,
                 state_filename: str,
                 key_filename: str,
                 log_filename: str):
        """Initialize component.
        """
        self.base_folder = Path()
        self.state_filename = state_filename
        self.key_filename = key_filename
        self.log_filename = log_filename
        self.log = open(self.log_path, mode='a', encoding='utf-8')

    def path(self, *args) -> str:
        """Return absolute path built from arguments.
        """
        path = self.base_folder
        for arg in args:
            path = path / arg
        return str(path.absolute())

    @staticmethod
    def exists(path: str) -> bool:
        """Return true if path exists.
        """
        return os.path.exists(path)

    @staticmethod
    def mkdir(path: str) -> None:
        """Create new directory.
        """
        with OSErrorCatcher():
            os.mkdir(path)

    @staticmethod
    def remove(path: str) -> None:
        """Delete file.
        """
        with OSErrorCatcher():
            os.remove(path)

    @staticmethod
    def move(path_from: str, path_to: str) -> None:
        """Move file.
        """
        print('Moving')
        print(f'    from: {path_from}')
        print(f'      to: {path_to}')
        with OSErrorCatcher():
            shutil.move(path_from, path_to)

    @property
    def root_path(self) -> str:
        """Shorthand for base folder.
        """
        return self.path()

    @property
    def key_path(self) -> str:
        """Shorthand for key file path.
        """
        return self.path(self.key_filename)

    @property
    def log_path(self) -> str:
        """Shorthand for log file path.
        """
        return self.path('staging', self.log_filename)

    @property
    def state_path(self) -> str:
        """Shorthand for state file path.
        """
        return self.path(self.state_filename)

    def load_user_key(self) -> Dict[str, str]:
        """Load user identity from file.
        """
        return load_json(self.key_path)

    def save_user_key(self, user_name: str, user_id: str) -> None:
        """Save file for user identity.
        """
        return save_json(self.key_path, user_name=user_name, user_id=user_id)

    def load_log(self) -> List[dict]:
        """Load and parse all the history from hard drive.
        """
        try:
            with open(self.log_path, mode='r', encoding='utf-8') as file:
                # this place can potentially cause problems
                # you have a few spare gbs of memory aren't you?
                contents = file.readlines()
                log = [
                    ujson.loads(x) for x in contents
                ]
        except FileNotFoundError:
            log = []
        return log

    def append_to_log(self, payload: str) -> None:
        """Add string to the program log.

        Note that log file is just lines of JSON instances.
        But it is not JSON, nor CSV.
        """
        self.log.write(payload + '\n')
        print(Fore.LIGHTGREEN_EX + f'Added to log {payload}')

    def load_state(self) -> dict:
        """Load previously saved state from hard drive.
        """
        try:
            with open(self.state_path, mode='rb') as file:
                state = pickle.load(file)
        except FileNotFoundError:
            state = {}
        return state

    def save_state(self, state_snapshot: dict) -> None:
        """Save current state to the hard drive.
        """
        with open(self.state_path, 'wb') as file:
            pickle.dump(state_snapshot, file)
        print(Fore.LIGHTGREEN_EX + f'Saved file {self.state_path}')

    def get_version(self) -> str:
        """Scan through folders and decide which version we're on.
        """
        version = 'Empty'
        images_dir = self.path('images')

        if not os.path.exists(images_dir):
            os.mkdir(images_dir)

        else:
            folders = sorted(
                x for x in os.listdir(images_dir)
                if os.path.isdir(x)
            )
            if folders:
                version = folders[-1]

        return version

    def __del__(self) -> None:
        """Close log on exit.
        """
        self.log.close()

    def create_folders_if_need_to(self):
        """Ensure that all required folders exist. Create if not.
        """
        expected = [
            self.path('images'),
            self.path('meta'),
            self.path('thumbnails'),
            self.path('staging'),
            self.path('staging', 'images'),
            self.path('staging', 'meta'),
            self.path('staging', 'thumbnails'),
            self.path('staging', 'unconfirmed'),
        ]
        for each in expected:
            if not self.exists(each):
                self.mkdir(each)
                print(f'New folder created: {each}')

    @staticmethod
    def get_ext(filename: str) -> str:
        """Get extension of the filename.
        """
        return filename.rsplit('.')[-1]

    def save_metainfo(self, uuid: str, info: dict) -> None:
        """Create personal JSON for the image.
        """
        filename = self.path('staging', 'meta', f'{uuid}.json')
        save_json(filename, **info)
