# coding: utf-8
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

    def request(self, method, path):
        return self.conn.request(method, self.build_url(path))
