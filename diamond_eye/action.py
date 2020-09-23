# -*- coding: utf-8 -*-

"""Atomic change that supposed to be persistent.
"""
from datetime import datetime
from typing import Dict, Union

import ujson

from diamond_eye import settings


def make_action(user_id: str, user_name: str, version: str,
                action: Dict[str, Union[int, str, dict, list]]) -> str:
    """Create string of atomic change that supposed to be persistent.
    """
    return ujson.dumps({
        'user_id': user_id,
        'user_name': user_name,
        'version': version,
        'moment': str(now()),
        'action': action,
    }, indent=0, ensure_ascii=False)


def now() -> datetime:
    """Wrapper around datetime.now().
    """
    return datetime.now().astimezone(settings.TIMEZONE)
