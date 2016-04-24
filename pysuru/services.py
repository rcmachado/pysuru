# coding: utf-8
import json
from collections import namedtuple

from pysuru.base import BaseAPI, ObjectMixin


SERVICE_INSTANCE_ATTRS = (
    'name',
    'description',
    'type',
    'plan',
)


_ServiceInstance = namedtuple('ServiceInstance', SERVICE_INSTANCE_ATTRS)


class ServiceInstance(_ServiceInstance, ObjectMixin):
    pass


class ServiceInstanceAPI(BaseAPI):
    def filter_by_app(self, name):
        path = '/services/instances?app={}'.format(name)
        _, response = self.client.get(path)

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

    def add(self, data):
        body = json.dumps(data)
        http_response = self.client.urlopen('POST', '/services/instances',
                                            body=body)
        response = json.loads(http_response.data.decode('utf-8'))
        if response.status == 409:
            raise ServiceAlreadyExists()
        elif response.status == 200:
            return True
        else:
            return False


class ServiceAlreadyExists(Exception):
    pass
