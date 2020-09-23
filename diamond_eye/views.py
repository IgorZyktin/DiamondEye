# -*- coding: utf-8 -*-

"""Web components here.
"""
import bottle

from diamond_eye import main, settings


def ensure_registered(func):
    """Send user to registration if needed.
    """
    # TODO
    # print('xxx', main.state.get_variable('app', 'user_name'))
    # def wrapper():
    #     return bottle.redirect('/register')
    #
    # if main.state.get_variable('app', 'user_name'):
    #     return func

    return func


def _base_context() -> dict:
    """Get common context for every view.
    """
    default_at_once = str(settings.IMAGES_AT_ONCE)

    return {
        'title': "Nicord's catalogue",
        'user_name': main.state.get_variable('app', 'user_name'),
        'version': main.state.get_variable('app', 'version') or 'Empty',
        'not_saved': main.state.not_saved,
        'at_once': main.state.get_variable('app', 'at_once', default_at_once),
    }


@ensure_registered
def index() -> bottle.Response:
    """Actual starting page.
    """
    return bottle.template('index', **_base_context())


@ensure_registered
def search() -> bottle.Response:
    """Search and browse images here.
    """
    old_at_once = main.state.get_variable('app', 'at_once',
                                          settings.IMAGES_AT_ONCE)
    at_once = bottle.request.query.at_once

    if at_once != old_at_once:
        main.state.set_variable('app', 'set', 'at_once', at_once)
    else:
        at_once = old_at_once

    random_uuids = main.master.get_random_image_uuids(main.state, int(at_once))

    random_images = []
    for uuid in random_uuids:
        url_thumb = main.state.get_variable(uuid, 'url_thumb')
        if url_thumb:
            random_images.append((uuid, url_thumb))

    context = {
        **_base_context(),
        'images': random_images,
        'at_once': at_once,
    }
    return bottle.template('search', **context)


def start() -> bottle.Response:
    """Starting page.
    """
    if main.state.get_variable('app', 'user_name'):
        return bottle.redirect('/index')

    user_key = main.filesystem.load_user_key()

    if not user_key:
        return bottle.redirect('/register')

    main.state.set_variable('app', 'set', 'user_name', user_key['user_name'])
    main.state.set_variable('app', 'set', 'user_id', user_key['user_id'])

    return bottle.redirect('/index')


def register() -> bottle.Response:
    """Registration page.
    """
    if main.state.get_variable('app', 'user_name'):
        return bottle.redirect('/index')

    error = ''

    if bottle.request.method == 'POST':
        user_name = bottle.request.forms.get('user_name')

        if not user_name:
            error = 'Please enter your name!'

        elif user_name in main.state.get_variable('app', 'known_users', set()):
            error = f'Name "{user_name}" is already taken. ' \
                    f'Please choose something different'
        else:
            main.app.register_new_user(user_name, main.state, main.filesystem)
            return bottle.redirect('/index')

    context = {
        **_base_context(),
        'error': error,
    }
    return bottle.template('register', **context)


@ensure_registered
def upload() -> bottle.Response:
    """Uploading page.
    """
    if bottle.request.method == 'POST':
        uploaded_objects = bottle.request.files.getall('upload')
        main.master.add_to_unconfirmed(
            files=uploaded_objects,
            filesystem=main.filesystem,
            state=main.state,
            app=main.app,
        )
        return bottle.redirect('/confirm')

    context = {
        **_base_context(),
    }
    return bottle.template('upload', **context)


@ensure_registered
def confirm() -> bottle.Response:
    """Confirmation of image saving after upload.
    """
    context = {
        **_base_context(),
        'images': main.master.get_unconfirmed_images(),
    }
    return bottle.template('confirm', **context)


def browse(uuid: str) -> bottle.Response:
    """Show details of a single image.
    """
    image_url = main.state.get_variable(uuid, 'url')
    image_tags = main.state.get_branch(uuid)

    context = {
        **_base_context(),
        'uuid': uuid,
        'image_url': image_url,
        'image_tags': image_tags,
    }
    return bottle.template('browse', **context)


def post_ajax_save_state():
    """Force server to save current state into JSON file.
    """
    state_snapshot = main.state.extract_state()
    main.filesystem.save_state(state_snapshot)
    main.state.not_saved = False
    return 'ok'


def post_ajax_refresh_state():
    """Force server to rebuild whole state from log.
    """
    main.state.make_full_refresh(main.filesystem)
    main.master.drop_all_unconfirmed(main.filesystem)
    return 'ok'


def post_ajax_drop_all():
    """Delete all unconfirmed images.
    """
    main.master.drop_all_unconfirmed(main.filesystem)
    return 'ok'


def post_ajax_save_all():
    """Save all unconfirmed images.
    """
    main.master.save_all_unconfirmed(main.filesystem, main.state)
    return 'ok'


def static(filepath: str):
    """Serve static.
    """
    return common_static('static', filepath)


def staging(filepath: str):
    """Serve main content (local user).
    """
    return common_static('staging', filepath)


def images(filepath: str):
    """Serve main content (global storage).
    """
    return common_static('images', filepath)


def common_static(root: str, filepath: str):
    """Common view for static files.
    """
    return bottle.static_file(filepath, root=main.filesystem.path(root))
