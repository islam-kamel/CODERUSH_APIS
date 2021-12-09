# from posts_apis.helpers.posts_manage import Manage
#
#
# class empty:
#     pass
#
#
# class CreatePost(Manage):
#     def __init__(self):
#         self.request = empty
#
#     @property
#     def get_post(self):
#         self.__set_slug__(self.request)
#         serializer = self.get_serializer(data=self.request.data)
#         if not serializer.is_valid(): return {'post': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST}
#         return self.__save_post__(serializer)
#
#     @set_post.setter
#     def set_post(self, request):
#         self.request = request
