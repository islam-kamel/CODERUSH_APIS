"""
Manage all posts here.
CreatePost, GetPost, PostDetails
"""
from django.http import Http404
from rest_framework import status
from posts_apis.models import Posts
from posts_apis.serializer import PostSerializer
from .serializer_manage import Serializer


class GetPost(Serializer):
    @property
    def get_posts(self):
        posts = Posts.objects.all()
        serializer = self.get_serializer(posts, many=True)
        return serializer.data


class CreatePost(Serializer):
    def set_post(self, request):
        self.__set_slug(request)
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(): return {'post': None, 'status': status.HTTP_400_BAD_REQUEST}
        return self.__save_post(serializer)

    @staticmethod
    def __save_post(serializer):
        serializer.save()
        return {'post': serializer.data, 'status': status.HTTP_201_CREATED}

    @staticmethod
    def __set_slug(request):
        try:
            request.data['slug'] = request.data['title'].replace(' ', '-')
        except KeyError:
            return False

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
#         return CreatePost.save_post(serializer)
