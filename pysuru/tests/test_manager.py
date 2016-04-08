# coding: utf-8
try:
    from unittest import mock
except ImportError:
    import mock

from pysuru.apps import App
from pysuru.manager import TsuruAPI


def test_manager_headers_should_return_authorization_header():
    api = TsuruAPI(None, 'TOKEN')
    assert {'Authorization': 'bearer TOKEN'} == api.headers


@mock.patch('pysuru.manager.TsuruAPI.request')
def test_apps_should_return_list_of_app_objects(request, tsuru_apps_list):
    request.return_value.read.return_value = tsuru_apps_list

    api = TsuruAPI('TARGET', 'TOKEN')
    apps = api.apps()

    assert 3 == len(apps)
    assert isinstance(apps[0], App)
    assert request.call_args_list[0] == mock.call('GET', '/apps', headers=mock.ANY)
