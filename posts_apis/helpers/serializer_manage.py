"""
Manage Serializer Method
"""
from posts_apis.serializer import PostSerializer


class Serializer:
    @staticmethod
    def get_serializer(post=None, many=False, **kwargs):
        if kwargs and post is None: return PostSerializer(data=kwargs['data'], many=many)
        return PostSerializer(post, many=many)
