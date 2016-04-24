# coding: utf-8
import os

from pysuru.apps import AppsAPI
from pysuru.http import HttpClient


class Tsuru(object):
    """
    Main class to interact with Tsuru API
    """

    def __init__(self, target=None, token=None):
        """
        Creates an object and stores credentials used to connect to
        Tsuru API.

        Receives ``target`` and ``token`` or, if not provided, read
        ``TSURU_TARGET`` and ``TSURU_TOKEN`` env variables. If neither
        options are provided, raises ValueError exception.
        """
        if not target:
            target = os.environ.get('TSURU_TARGET', None)
            if not target:
                raise ValueError(
                    'Missing target argument. Either provide target param or '
                    'set TSURU_TARGET env variable.')

        if not token:
            token = os.environ.get('TSURU_TOKEN', None)
            if not token:
                raise ValueError(
                    'Missing token argument. Either provide token param or '
                    'set TSURU_TOKEN env variable.')

        self.target = target
        self.token = token
        self.client = HttpClient(target, token)

    @property
    def apps(self):
        return AppsAPI(self.client)
