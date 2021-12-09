from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .helpers.get_object import GetObject
from .helpers.posts_manage import (
    GetPost,
    Serializer,
    CreatePost
)


class PostsListAPIView(APIView, GetPost, CreatePost):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response(self.get_posts)

    def post(self, request):
        data = self.set_post(request)
        if not data['post'] is None: return Response(data['post'], status=data['status'])
        return Response({'failure': 'can not create post!'}, status=data['status'])


class PostDetailsAPIView(APIView, GetObject, Serializer):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = self.get_serializer(post)
        return Response(serializer.data)
