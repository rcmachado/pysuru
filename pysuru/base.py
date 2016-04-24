# coding: utf-8
import json

import certifi
from urllib3 import PoolManager


class BaseAPI(object):
    def __init__(self, client):
        self.client = client

    def get_request(self, path):
        response = self.client.urlopen('GET', path)

        content = None
        if response.data:
            content = json.loads(response.data.decode('utf-8'))

        return response.status, content


class ObjectMixin(object):
    @classmethod
    def create(cls, client=None, **kwargs):
        """Remove any unknown field from kwargs and return the object"""
        attrs = {k: kwargs.get(k, None) for k in cls._fields}
        obj = cls(**attrs)
        obj._client = client
        return obj
