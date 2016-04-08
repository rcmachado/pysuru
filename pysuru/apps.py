# coding: utf-8
from builtins import tuple as _tuple
from collections import namedtuple


app_attrs = (
    'name',
    'description',
    'platform',
    'pool',
)


class App(namedtuple('App', app_attrs)):
    @classmethod
    def create(cls, **kwargs):
        """Remove any unknown field from ``data`` dictionary and return an instance"""
        attrs = {k: kwargs.get(k, None) for k in app_attrs}
        return cls(**attrs)

