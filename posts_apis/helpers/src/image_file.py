"""
Image Manage File
rename image to uuid
and return path to save image in media dir
"""

#  MIT License
#
#  Copyright (c) 2021 islam kamel
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"),to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY,WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

import os
import uuid

from django.conf import settings


class ImageManage:
    """
    this class to use to rename image to uuid5.ext
    """
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
        except FileNotFoundError or PermissionError:
            raise ValueError('can not found image')
