# coding: utf-8
import certifi
from urllib3 import PoolManager


class HttpClient(object):
    _conn = None

    def __init__(self, target, token):
        self.target = target
        self.token = token

    @property
    def conn(self):
        """
        Pool manager object

        Creates PoolManager object when first used.
        """
        if not self._conn:
            self._conn = PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        return self._conn

    @property
    def headers(self):
        """Default headers for all requests"""
        return {
            'Authorization': 'bearer {}'.format(self.token)
        }

    def urlopen(self, method, path, headers=None, body=None):
        """
        Execute request on API

        Sent a request to URL built using target argument from
        constructor and provided ``path``. Also pass correct
        Authorization header.
        """
        headers = dict(headers or {})
        headers.update(self.headers)
        url = self.build_url(path)
        return self.conn.urlopen(method, url, headers=headers, body=body)

    def build_url(self, url):
        return '{}/{}'.format(self.target.rstrip('/'), url.lstrip('/'))
