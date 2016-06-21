# coding: utf-8
import json

import certifi
from urllib3 import PoolManager


class HttpClient(object):
    """
    Thin wrapper around urllib3.PoolManager

    Wrapper to urllib3 lib that enables SSL cert validation and
    provides methods to work with Tsuru API authentication.
    """
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
        return self.conn.request(method, url, headers=headers, data=body)

    def get(self, *args, **kwargs):
        """
        Make GET requests against API

        Wrapper for ``urlopen`` to make GET requests. Assume that
        responses are encoded as JSON and decodes them appropriately.
        """
        response = self.urlopen('GET', *args, **kwargs)
        content = None
        if response.data:
            content = json.loads(response.data.decode('utf-8'))
        return response.status, content

    def post(self, url, data, *args, **kwargs):
        """Send a post request to API"""
        url = self.build_url(url)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
        }
        headers.update(self.headers)
        response = self.conn.request_encode_body(
            'POST', url, fields=data, headers=headers, encode_multipart=False,
            *args, **kwargs)
        return response.status, response.read()

    def build_url(self, url):
        return 'http://{}/{}'.format(self.target.rstrip('/'), url.lstrip('/'))
