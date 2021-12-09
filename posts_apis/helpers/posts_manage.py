"""
Manage all posts here.
PostManage, GetPost, PostDetails
"""
from rest_framework import status

from posts_apis.models import Posts
from .src.get_object import GetObject
from .src.serializer_manage import Serializer


class Manage(Serializer, GetObject):
    @staticmethod
    def response_handel(response, status_code=status.HTTP_200_OK):
        try:
            return {'data': response.data, 'status': status_code}
        except AttributeError:
            return {'errors': response, 'status': status_code}


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
        if not serializer.is_valid(): return self.response_handel(serializer.errors,
                                                                  status_code=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return self.response_handel(serializer, status_code=status_code)

    @staticmethod
    def __set_slug__(request):
        request.data['slug'] = request.data['title'].replace(' ', '-')

    def edit(self, instance, request):
        self.__set_slug__(request)
        serializer = self.get_serializer(instance, data=request.data)
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
