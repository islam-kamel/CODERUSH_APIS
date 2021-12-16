"""
Manage all posts here.
PostManage, GetPost, PostDetails
"""

from abc import ABC, abstractmethod

from django.contrib.auth import get_user_model
#  MIT License
#
#  Copyright (c) 2021 islam kamel
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
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
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
from rest_framework.status import *

from posts_apis.models import Posts
from .src.get_object import GetObject
from .src.image_file import ImageManage
from .src.serializer_manage import Serializer
from .src.typing import Empty


class Manage(Serializer, GetObject, ImageManage):
    try:
        status = HTTP_200_OK
    except NameError as e:
        raise "Please install rest_framework"

    @staticmethod
    def response_handel(response=None, status_code: str = status):
        STATUS = {
            'errors': HTTP_400_BAD_REQUEST,
            'deleted': HTTP_204_NO_CONTENT,
        }
        try:
            return {"data": response.data, "status": status_code}
        except AttributeError:
            return {"errors": response, "status": STATUS[status_code]}

    # @staticmethod
    # def _set_slug__(request):
    #     try:
    #         request.data["slug"] = request.data["title"].replace(" ",
    #                                                              "-").lowr()
    #     except AttributeError:
    #         pass


class AbstractSaveDB(ABC, Manage):
    __STATUS_CODE = Empty
    __SERIALIZER = Empty

    @abstractmethod
    def __save_post__(self, **kwargs):
        raise NotImplementedError


class AbstractCreatePostManager(ABC):
    @abstractmethod
    def set_post(self):
        raise NotImplementedError

    # @abstractmethod
    # def __save_post__(self):
    #     raise NotImplementedError


class AbstractGetPostManager(ABC, Manage):
    @abstractmethod
    def get_posts(self):
        raise NotImplementedError


class AbstractGetPostDetailsManger(ABC, Manage):
    @abstractmethod
    def get_object(self, **kwargs):
        raise NotImplementedError


class AbstractUpdatePost(ABC):
    @abstractmethod
    def edit(self):
        raise NotImplementedError

    @staticmethod
    def is_writer(request, pk, method):
        USER = get_user_model()
        if request.method == method and request.user.pk is not None:
            user_id = USER.objects.get(pk=request.user.pk)
            if user_id is not None:
                try:
                    post = Posts.objects.get(pk=pk)
                    try:
                        user = USER.objects.get(pk=post.create_by_id)
                    except User.DoesNotExist:
                        return False

                    if post.create_by_id == user.pk:
                        if request.user.pk == user.pk:
                            return True
                except Posts.DoesNotExist:
                    return False


class AbstractDeletePost(ABC, Manage):
    @abstractmethod
    def del_handle(self):
        raise NotImplementedError
