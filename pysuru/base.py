# coding: utf-8
import json

import certifi
from urllib3 import PoolManager


class BaseAPI(object):
    _conn = None

    def __init__(self, target, token):
        self.target = target
        self.token = token

    @property
    def conn(self):
        """Connection object"""
        if not self._conn:
            self._conn = PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        return self._conn

    @property
    def headers(self):
        """Default headers for all requests"""
        return {
            'Authorization': 'bearer {}'.format(self.token)
        }

    def build_url(self, url):
        return '{}/{}'.format(self.target.rstrip('/'), url.lstrip('/'))

    def get_request(self, path):
        url = self.build_url(path)
        response = self.conn.request('GET', url, headers=self.headers)

        content = None
        if response.data:
            content = json.loads(response.data.decode('utf-8'))

        return response.status, content

    def request(self, method, path):
        return self.conn.request(method, self.build_url(path), headers=self.headers)

    def post_json(self, path, payload):
        body = json.dumps(payload)
        return self.conn.urlopen('POST', self.build_url(path),
                                 headers=self.headers, body=body)


class ObjectMixin(object):
    @classmethod
    def create(cls, **kwargs):
        """Remove any unknown field from kwargs and return the object"""
        attrs = {k: kwargs.get(k, None) for k in cls._fields}
        return cls(**attrs)
