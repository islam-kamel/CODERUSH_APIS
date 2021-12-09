"""
Manage all posts here.
PostManage, GetPost, PostDetails
"""
from rest_framework import status

from posts_apis.models import Posts
from .serializer_manage import Serializer


class GetPost(Serializer):
    def get_posts(self):
        posts = Posts.objects.all()
        serializer = self.get_serializer(posts, many=True)
        return serializer.data


class PostManage(Serializer):
    def set_post(self, request):
        self.__set_slug__(request)
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(): return {'post': None, 'status': status.HTTP_400_BAD_REQUEST}
        return self.__save_post__(serializer)

    @staticmethod
    def __save_post__(serializer, status_code=status.HTTP_201_CREATED):
        serializer.save()
        return {'data': serializer.data, 'status': status_code}

    @staticmethod
    def __set_slug__(request):
        try:
            request.data['slug'] = request.data['title'].replace(' ', '-')
        except KeyError:
            return False

    @staticmethod
    def __errors__(error, status_code=status.HTTP_400_BAD_REQUEST):
        return {'data': error, 'status': status_code}

    def edit(self, instance, request):
        self.__set_slug__(request)
        serializer = self.get_serializer(instance, data=request.data)

        if not serializer.is_valid(): return self.__errors__(serializer.errors)
        return self.__save_post__(serializer, status_code=status.HTTP_202_ACCEPTED)


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
