# coding: utf-8
import json
from builtins import tuple as _tuple
from collections import namedtuple

from pysuru.base import BaseAPI


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


class AppsAPI(BaseAPI):
    _data = []

    @property
    def data(self):
        if not self._data:
            http_response = self.request('GET', '/apps', headers=self.headers)
            response = json.loads(http_response.read())
            for data in response:
                self._data.append(App.create(**data))
        return self._data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        return self.data[key]
