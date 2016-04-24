# coding: utf-8
import json
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
        api = ServiceInstanceAPI(self._client)
        return api.filter_by_app(self.name)


class AppsAPI(BaseAPI):
    _data = []

    @property
    def all(self):
        if not self._data:
            _, response = self.client.get('/apps')
            for data in response:
                self._data.append(App.create(self.client, **data))
        return self._data

    def __len__(self):
        return len(self.all)

    def __iter__(self):
        return iter(self.all)

    def __getitem__(self, key):
        return self.all[key]

    def get(self, name):
        status, response = self.client.get('/apps/{}'.format(name))
        if status == 404:
            raise AppDoesNotExists('App {} not found'.format(name))

        if status != 200:
            return False

        data = {
            'name': response['name'],
            'description': response['description'],
            'plan': response['plan']['name'],
            'pool': response['pool'],
            'team_owner': response['teamowner'],
            'platform': response['platform'],
        }
        return App.create(self.client, **data)

    def add(self, data):
        body = json.dumps(data)
        http_response = self.client.urlopen('POST', '/apps', body=body)
        if http_response.status == 200:
            return True
        elif http_response.status == 409:
            raise
        return False

    def update(self, name, data):
        body = json.dumps(data)
        http_response = self.client.urlopen('POST', '/apps/{}'.format(name),
                                            body=body)
        if http_response.status == 200:
            return True
        else:
            return False

    def bind_service(self, name, service_instance):
        path = ('/services/{}/instances/{}/{}'
                .format(service_instance.type, service_instance.name, name))
        http_response = self.client.urlopen('PUT', path)
        if http_response.status == 200:
            return True
        return False


class AppAlreadyExists(Exception):
    pass

class AppDoesNotExists(Exception):
    pass
