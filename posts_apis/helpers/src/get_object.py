"""
Get objects from database manage
"""
from posts_apis.models import Posts


class GetObject:
    @staticmethod
    def get_object(pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404
