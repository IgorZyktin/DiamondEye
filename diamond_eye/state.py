# -*- coding: utf-8 -*-

"""Component that manages application state.
"""
import copy
from collections import defaultdict
from typing import Optional, Literal, TypeVar, Union

from colorama import Fore

from diamond_eye.utils import MetaSingleton

T = TypeVar('T')


class State(metaclass=MetaSingleton):
    """Component that manages application state.
    """

    def __init__(self, saved_state: dict):
        """Initialize component.
        """
        self._state = {}
        self.not_saved = False

        self._state.update(saved_state)

    def __bool__(self) -> bool:
        """Return True if something is stored in _state.
        """
        return bool(self._state)

    def set_variable(self,
                     branch: str,
                     method: Literal['set', 'add', 'update'],
                     key: str, value: Union[int, str, tuple, dict],
                     verbose: bool = True) -> None:
        """Set some variable to some value. That simple.
        """
        if branch not in self._state:
            self._state[branch] = {}

        if method == 'set':
            self._state[branch][key] = value

        elif method == 'add':
            if key not in self._state[branch]:
                self._state[branch][key] = set()

            self._state[branch][key].add(value)

        elif method == 'update':
            if key not in self._state[branch]:
                self._state[branch][key] = value

            self._state[branch][key].update(value)

        self.not_saved = True

        if verbose:
            print(Fore.MAGENTA + f'Set variable [{branch}, '
                                 f'{key}] <{method}> {value!r}')

    def get_variable(self, branch: str, key: str,
                     default: T = None) -> Optional[T]:
        """Get variable from memory. That simple.
        """
        if branch not in self._state:
            return default
        return self._state[branch].get(key, default)

    def get_branch(self, branch: str) -> dict:
        """Get while branch.
        """
        return self._state.get(branch, {})

    def extract_state(self) -> dict:
        """Export internal data as dict.
        """
        state_snapshot = copy.deepcopy(self._state)
        print(Fore.GREEN + f'Extracted {len(state_snapshot)} '
                           'records from state')
        return state_snapshot

    def make_full_refresh(self, filesystem) -> None:
        """Restore state from log.
        """
        print(Fore.YELLOW + 'Refreshing state')
        self._state.clear()

        log = filesystem.load_log()
        print(Fore.YELLOW + f'Found {len(log)} historical records.')
        for line in log:
            action = line['action']
            self.set_variable(**action)

        if not self.get_variable('app', 'version', ''):
            version = filesystem.get_version()
            self.set_variable('app', 'set', 'version', version)

        user_key = filesystem.load_user_key()

        if user_key:
            self.set_variable('app', 'set', 'user_name', user_key['user_name'])
            self.set_variable('app', 'set', 'user_id', user_key['user_id'])

        self.not_saved = True
