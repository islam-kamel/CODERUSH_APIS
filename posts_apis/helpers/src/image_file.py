"""
Image Manage File
rename image to uuid
and return path to save image in media dir
"""

import os
import uuid

from django.conf import settings


class ImageManage:
    MEDIA_URL = settings.MEDIA_URL[1:]

    @staticmethod
    def set_image_file(instance, filename):
        ext = filename.split(".")[-1]
        name = uuid.uuid5(uuid.NAMESPACE_OID, str(instance.create_by.id))
        filename = '%s.%s' % (name, ext)
        return os.path.join('posts', filename)

    def remove_image(self, url):
        try:
            os.remove('{}{}'.format(self.MEDIA_URL, url))
        except PermissionError:
            pass
