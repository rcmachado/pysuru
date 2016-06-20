# coding: utf-8
class BaseAPI(object):
    """
    Base class for API related classes

    Provides basic skeleton for API related classes
    """
    def __init__(self, client):
        self.client = client

    def list(self, *args, **kwargs):
        raise NotImplemented('Object list not implemented')

    def get(self, name):
        raise NotImplemented('Object get not implemented')

    def create(self, data):
        raise NotImplemented('Object creation not implemented')

    def update(self, name, data):
        raise NotImplemented('Object update not implemented')

    def delete(self, name):
        raise NotImplemented('Object deletion not implemented')


class ObjectMixin(object):
    @classmethod
    def create(cls, client=None, **kwargs):
        """Remove any unknown field from kwargs and return the object"""
        attrs = {k: kwargs.get(k, None) for k in cls._fields}
        obj = cls(**attrs)
        obj._client = client
        return obj
