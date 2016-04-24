# coding: utf-8
from pysuru.apps import AppsAPI


class Tsuru(object):
    def __init__(self, target, token):
        self.target = target
        self.token = token

    @property
    def apps(self):
        return AppsAPI(self.target, self.token)
