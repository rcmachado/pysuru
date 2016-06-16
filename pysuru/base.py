# coding: utf-8
class BaseAPI(object):
    def __init__(self, client):
        self.client = client


class ObjectMixin(object):
    @classmethod
    def create(cls, client=None, **kwargs):
        """Remove any unknown field from kwargs and return the object"""
        attrs = {k: kwargs.get(k, None) for k in cls._fields}
        obj = cls(**attrs)
        obj._client = client
        return obj
