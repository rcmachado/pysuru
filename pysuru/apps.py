# coding: utf-8
import json
from builtins import tuple as _tuple
from collections import namedtuple

from pysuru.base import BaseAPI, ObjectMixin
from pysuru.services import ServiceInstanceAPI


app_attrs = (
    'name',
    'description',
    'platform',
    'team_owner',
    'pool',
)


class App(namedtuple('App', app_attrs), ObjectMixin):
    def services(self):
        api = ServiceInstanceAPI(self.target, self.token)
        return api.filter_by_app(self, self.name)


class AppsAPI(BaseAPI):
    _data = []

    @property
    def data(self):
        if not self._data:
            http_response = self.request('GET', '/apps', headers=self.headers)
            response = json.loads(http_response.data.decode('utf-8'))
            for data in response:
                self._data.append(App.create(**data))
        return self._data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def get(self, name):
        http_response = self.request('GET', '/apps/{}'.format(name))
        if http_response.status == 404:
            raise AppDoesNotExists('App {} not found'.format(name))

        if http_response.status != 200:
            return False

        response = json.loads(http_response.data.decode('utf-8'))
        data = {
            'name': response['name'],
            'description': response['description'],
            'plan': response['plan']['name'],
            'pool': response['pool'],
            'team_owner': response['teamowner'],
            'platform': response['platform'],
        }
        return App.create(**data)

    def add(self, data):
        http_response = self.post_json('/apps', data)
        if http_response.status == 200:
            return True
        elif http_response.status == 409:
            raise
        return False

    def update(self, name, data):
        http_response = self.post_json('/apps/{}'.format(name), data)
        if http_response.status == 200:
            return True
        else:
            return False

    def bind_service(self, name, service_instance):
        path = '/services/{}/instances/{}/{}'.format(service_instance.type, service_instance.name, name)
        http_response = self.request('PUT', path)
        if http_response.status == 200:
            return True
        return False


class AppAlreadyExists(Exception):
    pass

class AppDoesNotExists(Exception):
    pass
