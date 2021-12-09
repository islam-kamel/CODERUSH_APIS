"""
Manage Serializer Method
"""
from posts_apis.serializer import PostSerializer


class Empty:
    """
    This class is used to represent no data being provided for a given input
    or output value.
    It is required because `None` may be a valid input or output value.
    """
    pass


class Serializer(Empty):
    """
    This class is used to Get Json  from  database
    It is required because instance.
    """

    def get_serializer(self, instance=None, data=Empty, **kwargs):
        isMany = kwargs.pop('many', False)
        if data is not Empty: return PostSerializer(instance, data=data, many=isMany)
        return PostSerializer(instance, many=isMany)
