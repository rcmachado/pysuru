# coding: utf-8
import json

import certifi
from urllib3 import PoolManager

from pysuru.apps import AppsAPI


class TsuruAPI(object):
    def __init__(self, target, token):
        self.target = target
        self.token = token

    @property
    def apps(self):
        return AppsAPI(self.target, self.token)
