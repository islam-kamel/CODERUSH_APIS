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
from django.contrib.auth import get_user_model

from .posts_manage import CreatePost
from .posts_manage import DeletePost
from .posts_manage import GetPost
from .posts_manage import GetPostDetails
from .posts_manage import UpdatePost
from .src.typing import Empty


class ListAllPosts(GetPost, CreatePost):
    __REQUEST = Empty

    @property
    def posts_list(self) -> object:
        if self.__REQUEST is not Empty:
            return self.__REQUEST
        return self.get_posts()

    @posts_list.setter
    def posts_list(self, request=None):
        self.__REQUEST = self.set_post(request)


class PostsDetails(GetPostDetails, UpdatePost, DeletePost):

    @property
    def get_post(self):
        return self.get_serializer(instance=self.get_object())

    def update(self, request):
        if request.data:
            return self.edit(request)
        return self.response_handel(response='invalid content',
                                    status_code='errors')

    def delete_post(self):
        return self.del_handle()

    def is_writer(self, request, method):
        USER = get_user_model()
        if request.method == method and request.user.pk is not None:
            user_id = USER.objects.get(pk=request.user.pk)
            if user_id is not None:
                try:
                    post = self.get_object()
                    try:
                        user = USER.objects.get(pk=post.create_by_id)
                    except User.DoesNotExist:
                        return False

                    if post.create_by_id == user.pk:
                        if request.user.pk == user.pk:
                            return True
                except Posts.DoesNotExist:
                    return False
