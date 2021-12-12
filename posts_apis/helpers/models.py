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
    __DATA = Empty
    __SLUG = Empty
    __PK = Empty
    __SERIALIZER = Empty

    @property
    def get_post(self):
        return self.__SERIALIZER

    @get_post.setter
    def get_post(self, *args):
        try:
            self.__SLUG, self.__PK = args[0]['slug'], args[0]['pk']
        except KeyError:
            raise 'KeyError: You have to send such a pattern {slug: slug,pk: pk}.'
        self.__DATA = self.get_object(self.__PK, self.__SLUG)
        self.__SERIALIZER = self.get_serializer(self.__DATA)

    def update(self, request=Empty, slug=Empty, pk=Empty):
        instance = self.get_object(pk, slug)
        return self.edit(instance, request)

    def delete_post(self, request, pk, slug):
        return self.del_handle(request, pk, slug)
