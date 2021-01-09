# -*- coding: utf-8 -*-

"""Component that manages images.
"""
import random
from dataclasses import dataclass
from functools import cached_property, partial
from typing import Optional, List

import numpy as np
from PIL import Image
from colorama import Fore

from identity_manager.image_match import ImageSignature, normalized_distance
from diamond_eye.utils import emit_and_save_event, MetaSingleton


@dataclass
class _Img:
    """Simple container for the image.
    """
    uuid: str
    filename: str
    path: str
    url: str
    path_thumb: str
    url_thumb: str
    duplicate: Optional[str]
    signature: np.array

    def __eq__(self, other) -> bool:
        """Return True if other is equal to this.
        """
        if isinstance(other, type(self)):
            return other.signature == self.signature
        return NotImplemented

    @cached_property
    def sig_tuple(self) -> tuple:
        """Return hashed signature.
        """
        return tuple(int(x) for x in self.signature)

    def __hash__(self) -> int:
        """Return hashed signature.
        """
        return hash(self.sig_tuple)


class ImageMaster(metaclass=MetaSingleton):
    """Component that manages images.
    """

    def __init__(self, images_at_once: int, threshold: float,
                 thumbnail_size: int):
        """Initialize component.
        """
        self.sig_gen = ImageSignature()
        self.images_at_once = images_at_once
        self.thumbnail_size = thumbnail_size
        self.threshold = threshold
        self._confirmation_required = []

    def get_random_image_uuids(self, state,
                               images_at_once: Optional[int] = None,
                               ) -> List[str]:
        """Get n random image urls from the state.
        """
        known_signatures = state.get_variable('app', 'known_signatures', {})
        print(f'{len(known_signatures)}, {known_signatures=}')
        images_at_once = images_at_once or self.images_at_once
        images_at_once = min(len(known_signatures), images_at_once)
        return random.sample(tuple(known_signatures.values()), images_at_once)

    def drop_all_unconfirmed(self, filesystem) -> None:
        """Delete all unconfirmed images.
        """
        for image in self._confirmation_required:
            print(Fore.RED + f'Removing: {image.filename}')
            filesystem.remove(image.path)

        self._confirmation_required.clear()

    def get_unconfirmed_images(self) -> list:
        """Get set of unconfirmed images.
        """
        return self._confirmation_required

    @staticmethod
    def compare(sig_a: tuple, sig_b: tuple) -> float:
        """Calculate distance for two signatures.
        """
        our_sig = np.array(sig_a, dtype=np.int8)
        oth_sig = np.array(sig_b, dtype=np.int8)
        return normalized_distance(our_sig, oth_sig)

    def add_to_unconfirmed(self, files: list, filesystem, state, app) -> None:
        """Add these files to list of unconfirmed temporary images.
        """
        image_data = None
        known_signatures = state.get_variable('app', 'known_signatures', {})
        print(f'p1, {len(known_signatures)}, {known_signatures=}')

        for file in files:
            path = filesystem.path('staging', 'unconfirmed', file.filename)
            url = f'/staging/unconfirmed/{file.filename}'
            file.save(path, overwrite=True)

            try:
                image_data = Image.open(path)
                new_image = _Img(
                    uuid=app.issue_and_save_new_uuid(state),
                    filename=file.filename,
                    path=path,
                    url=url,
                    path_thumb=path,
                    url_thumb=url,
                    duplicate=None,
                    signature=self.sig_gen.generate_signature(image_data),
                )
            finally:
                if image_data:
                    image_data.close()

            # FIXME - potentially slow, need full text search here
            for image in self._confirmation_required:
                distance = self.compare(image.sig_tuple, new_image.sig_tuple)

                if distance < self.threshold:
                    new_image.duplicate = image.url
                    break

            if not new_image.duplicate:
                for sig_tuple, uuid in known_signatures.items():
                    distance = self.compare(sig_tuple, new_image.sig_tuple)

                    if distance < self.threshold:
                        new_image.duplicate = state.get_variable(uuid, 'url')
                        break

            self._confirmation_required.append(new_image)

    def save_all_unconfirmed(self, filesystem, state) -> None:
        """Save all unconfirmed images.
        """
        user_id = state.get_variable('app', 'user_id')
        user_name = state.get_variable('app', 'user_name')
        version = state.get_variable('app', 'version')
        emit = partial(emit_and_save_event, state, filesystem,
                       user_id, user_name, version)

        for each in self._confirmation_required:
            if each.duplicate:
                continue

            uuid = each.uuid
            filename = each.filename
            url_thumb = self.make_thumbnail(uuid, filename, filesystem)
            url = self.confirm_image(uuid, filename, filesystem)
            sig = each.sig_tuple

            emit(branch=uuid, method='set', key='url', value=url)
            emit(branch=uuid, method='set', key='url_thumb', value=url_thumb)
            emit(branch=uuid, method='set', key='filename', value=filename)
            emit(branch=uuid, method='set', key='sig_tuple', value=sig)

            filesystem.save_metainfo(uuid, state.get_branch(uuid))
            state.set_variable('app', 'update', 'known_signatures',
                               {each.sig_tuple: uuid}, True)

        self._confirmation_required.clear()
        state.not_saved = True

    def make_thumbnail(self, uuid: str, filename: str, filesystem) -> str:
        """Make smaller version of the image and place it into thumbnails.
        """
        ext = filesystem.get_ext(filename)
        size = (self.thumbnail_size, self.thumbnail_size)

        path_from = filesystem.path('staging', 'unconfirmed', filename)
        path_thumb = filesystem.path('staging', 'thumbnails',
                                     f'{self.thumbnail_size}_{uuid}.{ext}')
        try:
            im = Image.open(path_from)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(path_thumb)
        except OSError:
            print(f'Cannot create thumbnail for {path_from}')

        url_thumb = f'/staging/thumbnails/{self.thumbnail_size}_{uuid}.{ext}'
        return url_thumb

    @staticmethod
    def confirm_image(uuid: str, filename: str, filesystem) -> str:
        """Move original image from unconfirmed to the staging.
        """
        ext = filename.rsplit('.')[-1]
        path_from = filesystem.path('staging', 'unconfirmed', filename)
        path_to = filesystem.path('staging', 'images', f'{uuid}.{ext}')
        filesystem.move(path_from, path_to)
        url = f'/staging/images/{uuid}.{ext}'
        return url
