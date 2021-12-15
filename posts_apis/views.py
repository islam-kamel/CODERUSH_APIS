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

from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from rest_framework.views import APIView

from posts_apis.helpers.models import ListAllPosts, PostsDetails


class PostsListAPIView(APIView, ListAllPosts):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        response = self.posts_list
        return Response(response["data"], status=response["status"])

    def post(self, request):
        self.posts_list = request
        data = self.posts_list
        try:
            if not data["data"] is None:
                return Response(data["data"], status=data["status"])
        except KeyError:
            return Response(data["errors"], status=data["status"])


class PostDetailsAPIView(APIView, PostsDetails):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, slug, pk):
        self.get_post = {'slug': slug, 'pk': pk}
        return Response(self.get_post.data)

    def put(self, request, slug, pk):
        if self.is_writer(request, pk, 'PUT'):
            data = self.update(request, slug, pk)
            return Response(data.pop('data'), data.pop('status'))
        response = self.response_handel('Method Not Allowed', 'errors')
        return Response(response['errors'], response['status'])

    def delete(self, request, slug, pk):
        if self.is_writer(request, pk, 'DELETE'):
            data = self.delete_post(request, pk, slug)
            return Response(data['errors'], data['status'])
        response = self.response_handel('Method Not Allowed', 'errors')
        return Response(response['errors'], status=response['status'])
