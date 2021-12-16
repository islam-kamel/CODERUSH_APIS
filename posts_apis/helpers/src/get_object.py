"""
Get objects from database manage
"""
from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from posts_apis.models import Posts
from .typing import Empty


class GetObject:
    @property
    def get_queryset(self):
        return Posts.objects.all()

    def get_object(self):
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']
        obj = get_object_or_404(self.get_object, Q(pk=pk) & Q(slug=slug))
        return obj
        # try:
        #     if slug is not Empty:
        #         return Posts.objects.get(Q(pk=pk) & Q(slug=slug))
        # except Posts.DoesNotExist:
        #     raise Http404
