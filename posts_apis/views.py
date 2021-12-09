from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .helpers.get_object import GetObject
from .helpers.posts_manage import (
    GetPost,
    Serializer,
    PostManage
)


class PostsListAPIView(APIView, GetPost, PostManage):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response(self.get_posts())

    def post(self, request):
        data = self.set_post(request)
        if not data['post'] is None: return Response(data['post'], status=data['status'])
        return Response({'failure': 'can not create post!'}, status=data['status'])


class PostDetailsAPIView(APIView, GetObject, PostManage):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        new = self.edit(post, request)
        return Response(new.pop('data'), status=new.pop('status'))

