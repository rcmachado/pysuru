# coding: utf-8
from collections import namedtuple

from pysuru.base import BaseAPI, ObjectMixin


_service_instance = namedtuple(
    'ServiceInstance', ('name', 'description', 'type', 'plan', 'teamowner'))


class ServiceInstance(_service_instance, ObjectMixin):
    pass


class ServiceInstanceAPI(BaseAPI):
    def list(self, app_name=None):
        if 'app_name' in self.context:
            app_name = self.context['app_name']
        _, response = self._filter_by_app_name(app_name)

        services = []
        for service_data in response:
            for index, instance in enumerate(service_data['instances']):
                data = {
                    'name': instance,
                    'type': service_data['service'],
                    'plan': service_data['plans'][index],
                }
                services.append(ServiceInstance.create(self.client, **data))
        return services

    def _filter_by_app_name(self, app_name):
        path = '/services/instances?app={}'.format(app_name)
        return self.client.get(path)

    def create(self, data):
        name = data.pop('service')
        response = self.client.post('/services/{}/instances'.format(name),
                                    data=data)
        if response.status == 201:
            # TODO: return ServiceInstance instance
            return True

        if response.status == 409:
            raise ServiceInstanceAlreadyExists(
                'Service instance {} already exists'.format(data['name']))

        raise ServiceInstanceError(
            'Unknown error when creating service instance {}'
            .format(data['name']))

    def bind(self, service, service_instance, app_name=None):
        if 'app_name' in self.context:
            app_name = self.context['app_name']
        response = self.client.put('/services/{}/instances/{}/{}'
                                   .format(service, service_instance, app_name))
        if response.status == 200:
            return True

        raise ServiceInstanceError(
            'Unknown error when bind service instance {} to app {}'
            .format(service_instance, app_name))


class ServiceInstanceError(Exception):
    pass


class ServiceInstanceAlreadyExists(ServiceInstanceError):
    pass
