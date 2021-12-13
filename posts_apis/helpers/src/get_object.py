"""
Get objects from database manage
"""
from posts_apis.models import Posts
from .typing import Empty

class GetObject:
    @staticmethod
    def get_object(self, pk=Empty, slug=Empty):
        try:
            if slug is not Empty:
                return Posts.objects.get(Q(pk=pk) & Q(slug=slug))
        except Posts.DoesNotExist:
            raise Http404
