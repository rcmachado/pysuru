# coding: utf-8
try:
    from unittest import mock
except ImportError:
    import mock

from pysuru.manager import Tsuru


@mock.patch('pysuru.manager.AppsAPI')
def test_apps_should_create_appsapi_object(AppsAPI, tsuru_apps_list):
    api = Tsuru('TARGET', 'TOKEN')
    api.apps()

    assert AppsAPI.call_args_list[0] == mock.call('TARGET', 'TOKEN')
