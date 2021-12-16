"""
Manage all posts here.
PostManage, GetPost, PostDetails
"""

from django.db.models import Q
from django.shortcuts import get_object_or_404
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
from rest_framework import status
from posts_apis.models import Posts
from .manager import (
    AbstractDeletePost,
    AbstractSaveDB,
    AbstractUpdatePost,
    AbstractGetPostManager,
    AbstractGetPostDetailsManger,
    AbstractCreatePostManager
)


class DBManager(AbstractSaveDB):
    __STATUS_CODE = status.HTTP_200_OK
    __SERIALIZER = None

    def __save_post__(self, request):
        if self.__SERIALIZER.is_valid():
            self.__SERIALIZER.save(create_by=request.user)
            return self.response_handel(self.__SERIALIZER.data)

        return self.response_handel(self.__SERIALIZER.errors,
                                    status_code='errors')

    def set_data(self, serializer, request):
        self.__SERIALIZER = serializer
        return self.__save_post__(request)


class GetPost(AbstractGetPostManager):
    def get_object(self):
        return Posts.objects.all()

    def get_posts(self):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, many=True)
        return self.response_handel(serializer.data)


class CreatePost(AbstractCreatePostManager, DBManager):

    def set_post(self, request=None):
        serializer = self.get_serializer(data=request.data)
        return self.set_data(serializer, request)


class GetPostDetails(AbstractGetPostDetailsManger):
    @property
    def __get_queryset__(self):
        return Posts.objects.all()

    def get_object(self):
        return get_object_or_404(self.__get_queryset__,
                                 Q(pk=self.kwargs['pk']) &
                                 Q(slug=self.kwargs['slug']))


class UpdatePost(AbstractUpdatePost, DBManager):

    def edit(self, request=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, new_data=request)
        return self.set_data(serializer, request)


class DeletePost(AbstractDeletePost):

    def del_handle(self):
        post = self.get_object()
        self.remove_image(post.image)
        post.delete()
        return self.response_handel(status_code='deleted')
