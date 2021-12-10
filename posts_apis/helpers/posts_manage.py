"""
Manage all posts here.
PostManage, GetPost, PostDetails
"""

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
#

from rest_framework import status

from posts_apis.models import Posts
from .src.get_object import GetObject
from .src.image_file import ImageManage
from .src.serializer_manage import Serializer


class Manage(Serializer, GetObject, ImageManage):
    @staticmethod
    def response_handel(response=None, status_code=status.HTTP_200_OK):
        try:
            return {"data": response.data, "status": status_code}
        except AttributeError:
            return {"errors": response, "status": status_code}


class PostManage(Manage):

    def set_post(self, request):
        self.__set_slug__(request)
        serializer = self.get_serializer(data=request.data)
        return self.__save_post__(serializer)

    def get_posts(self):
        posts = Posts.objects.all()
        serializer = self.get_serializer(posts, many=True)
        return self.response_handel(serializer)

    def __save_post__(self, serializer, status_code=status.HTTP_201_CREATED):
        if not serializer.is_valid():
            return self.response_handel(
                serializer.errors, status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return self.response_handel(serializer, status_code)

    @staticmethod
    def __set_slug__(request):
        request.data["slug"] = request.data["title"].replace(" ", "-")

    def edit(self, instance, request):
        self.__set_slug__(request)
        serializer = self.get_serializer(instance, data=request.data)
        return self.__save_post__(serializer, status.HTTP_202_ACCEPTED)

    def del_handle(self, request, pk):
        post = self.get_object(pk)
        self.remove_image(post.image)
        post.delete()
        return self.response_handel(status_code=status.HTTP_204_NO_CONTENT)

# class UpdatePost(GetObject):
#     def get_object(self, pk):
#         try:
#             return Posts.objects.get(pk=pk)
#         except Posts.DoesNotExist:
#             raise Http404
#
#     def Update(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if not serializer.is_valid(): return {'post': None, 'status': status.HTTP_400_BAD_REQUEST}
#         return PostManage.save_post(serializer)
