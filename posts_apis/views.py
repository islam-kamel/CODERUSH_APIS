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
