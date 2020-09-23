# -*- coding: utf-8 -*-

"""Main module.
"""

import webbrowser

import bottle
from colorama import init

from diamond_eye import settings
from diamond_eye import views
from diamond_eye.application import Application
from diamond_eye.filesystem import FileSystem
from diamond_eye.image_master import ImageMaster
from diamond_eye.state import State

init(autoreset=True)

bottle.TEMPLATE_PATH.append('./templates')

filesystem = FileSystem(
    state_filename=settings.STATE_FILENAME,
    key_filename=settings.KEY_FILENAME,
    log_filename=settings.LOG_FILENAME,
)

state = State(
    saved_state=filesystem.load_state(),
)

app = Application()

master = ImageMaster(
    images_at_once=settings.IMAGES_AT_ONCE,
    threshold=settings.THRESHOLD,
    thumbnail_size=settings.THUMBNAIL_SIZE,
)

server = bottle.Bottle()


def setup_routes(server_instance: bottle.Bottle) -> None:
    """Setup all the routes for the server.

    Usually routing is done using:

        @app.route('/index')
        def index():
            ...

    But we're using lots of global objects, so we would face problems with
    cyclic imports here. Also, depending on the import way, we could face
    identity problems. For example, it is possible to get two instances
    of <filesystem>.

    I dont want to make actual singletones,
    so I just will route everything manually.
    """
    # main views
    server_instance.route('/index', 'GET', views.index)
    server_instance.route('/upload', ['GET', 'POST'], views.upload)
    server_instance.route('/confirm', ['GET', 'POST'], views.confirm)
    server_instance.route('/search', 'GET', views.search)
    server_instance.route('/browse/<uuid>', 'GET', views.browse)

    # support views
    server_instance.route('/', 'GET', views.start)
    server_instance.route('/register', ['GET', 'POST'], views.register)

    # ajax requests
    server_instance.route('/save_state', 'POST', views.post_ajax_save_state)
    server_instance.route('/refresh_state', 'POST',
                          views.post_ajax_refresh_state)
    server_instance.route('/drop_all_unconfirmed', 'POST',
                          views.post_ajax_drop_all)
    server_instance.route('/save_all_unconfirmed', 'POST',
                          views.post_ajax_save_all)

    # static and media resources
    server_instance.route('/static/<filepath:path>', 'GET', views.static)
    server_instance.route('/images/<filepath:path>', 'GET', views.images)
    server_instance.route('/staging/<filepath:path>', 'GET', views.staging)


def main():
    """Entry point.
    """
    filesystem.create_folders_if_need_to()
    setup_routes(server)

    if not bool(state):
        state.make_full_refresh(filesystem)

    print('Starting server...')

    webbrowser.open_new_tab(settings.URL)
    bottle.run(
        app=server,
        host=settings.HOST,
        port=settings.PORT,
        debug=True,
    )

    print('...server stopped.')


if __name__ == '__main__':
    main()
