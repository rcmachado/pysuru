# coding: utf-8
import json
from collections import namedtuple
from urllib.parse import urlencode

from pysuru.base import BaseAPI, ObjectMixin
from pysuru.services import ServiceInstanceAPI


app_attrs = (
    'name',
    'description',
    'ip',
    'owner',
    'teamowner',
    'platform',
    'pool',
)


class App(namedtuple('App', app_attrs), ObjectMixin):
    def services(self):
        api = ServiceInstanceAPI(self._client)
        return api.list(app_name=self.name)


class AppsAPI(BaseAPI):

    def list(self):
        result = []
        _, response = self.client.get('/apps')
        for data in response:
            result.append(App.create(self.client, **data))
        return result

    def get(self, name):
        status, response = self.client.get('/apps/{}'.format(name))
        if status == 404:
            raise AppDoesNotExists('App {} not found'.format(name))

        if status != 200:
            return False

        return App.create(self.client, **response)

    def create(self, data):
        body = urlencode(data)
        http_response = self.client.urlopen('POST', '/apps', body=body)
        if http_response.status == 200:
            return True
        elif http_response.status == 403:
            raise QuotaExceeded("Can't create app {}: quota exceeded".format(data['name']))
        elif http_response.status == 409:
            raise AppAlreadyExists('App {} already exists'.format(data['name']))
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


class AppError(Exception):
    pass


class QuotaExceeded(AppError):
    pass


class AppAlreadyExists(AppError):
    pass


class AppDoesNotExists(AppError):
    pass
