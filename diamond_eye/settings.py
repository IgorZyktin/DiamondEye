# -*- coding: utf-8 -*-

"""Project parameters.
"""

import pytz

# image master
IMAGES_AT_ONCE = '10'
THRESHOLD = 0.4  # minimal level of similarity, below this pictures are same
THUMBNAIL_SIZE = 256  # thumbnail width in pixels

# state
TIMEZONE = pytz.timezone('Europe/Moscow')

# filesystem
STATE_FILENAME = 'state.pickle'
KEY_FILENAME = 'key.json'
LOG_FILENAME = 'everything.log'
KNOWN_TYPES = ['jpg', 'jpeg', 'png']

# server
HOST = 'localhost'
PORT = 8080
URL = f'http://{HOST}:{PORT}/'
