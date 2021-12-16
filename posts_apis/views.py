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
from django.db.models import Q
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS,
    DjangoModelPermissionsOrAnonReadOnly, IsAdminUser
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, \
    HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from posts_apis.models import Posts
from posts_apis.serializer import PostSerializer
from user.models import User
from posts_apis.helpers.src.image_file import ImageManage


def is_writer(request, method, obj):
    if request.method == method and request.user.pk is not None:
        return obj.create_by_id == request.user.pk


class PostsListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @property
    def get_queryset(self):
        return Posts.objects.all()

    def get(self, request):
        post = PostSerializer(self.get_queryset, many=True)
        return Response(data=post.data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(create_by=request.user)
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data=Response.errors, status=HTTP_400_BAD_REQUEST)


class PostDetailsAPIView(APIView, ImageManage):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @property
    def get_queryset(self):
        return Posts.objects.all()

    def get(self, request, **kwargs):
        post = get_object_or_404(self.get_queryset, Q(pk=kwargs['pk']) & Q(
            slug=kwargs['slug']))
        post = PostSerializer(post)
        return Response(post.data, status=HTTP_200_OK)

    def put(self, request, **kwargs):
        posts = self.get_queryset
        post = get_object_or_404(
            posts, Q(pk=kwargs['pk']) & Q(slug=kwargs['slug']))
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid() and is_writer(request, 'PUT', post):
            serializer.save(create_by=request.user)
            return Response(data=serializer.data, status=HTTP_200_OK)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        post = self.get_queryset
        post = get_object_or_404(post, Q(pk=kwargs['pk']) & Q(slug=kwargs[
            'slug']))
        if is_writer(request, 'DELETE', post):
            if post.image:
                self.remove_image(url=post.image)
            post.delete()
            return Response(data='deleted', status=HTTP_200_OK)
        return Response(data='Method NoAllowed', status=HTTP_400_BAD_REQUEST)

    # permission_classes = [IsAuthenticatedOrReadOnly]
    #
    # def get(self, request, slug, pk):
    #     return Response(self.get_post.data)
    #
    # def put(self, request, **kwargs):
    #     if self.is_writer(request, method='PUT'):
    #         data = self.update(request)
    #         return Response(data.pop('data'), data.pop('status'))
    #     return Response(response['errors'], response['status'])
    #
    # def delete(self, request, **kwargs):
    #     if self.is_writer(request, 'DELETE'):
    #         data = self.delete_post()
    #         return Response(data['errors'], data['status'])
    #     response = self.response_handel('Method Not Allowed', 'errors')
    #     return Response(response['errors'], status=response['status'])
