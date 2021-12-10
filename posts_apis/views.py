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
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .helpers.posts_manage import PostManage


class PostsListAPIView(APIView, PostManage):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        response = self.get_posts()
        return Response(response["data"], status=response["status"])

    def post(self, request):
        data = self.set_post(request)
        try:
            if not data["data"] is None:
                return Response(data["data"], status=data["status"])
        except KeyError:
            return Response(data["errors"], status=data["status"])


class PostDetailsAPIView(APIView, PostManage):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        new = self.edit(post, request)
        try:
            if not new["data"] is None:
                return Response(new["data"], status=new["status"])
        except KeyError:
            return Response(new["errors"], status=new["status"])

    def delete(self, request, pk):
        return Response(self.del_handle(request, pk))
