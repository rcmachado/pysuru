# coding: utf-8
try:
    from unittest import mock
except ImportError:
    import mock

from pysuru.apps import App, AppsAPI


def test_apps_should_return_list_of_app_objects(tsuru_apps_list):
    AppsAPI.request = mock.MagicMock()
    AppsAPI.request.return_value.read.return_value = tsuru_apps_list

    apps = AppsAPI('TARGET', 'TOKEN')

    assert 3 == len(apps)
    assert isinstance(apps[0], App)
    assert AppsAPI.request.call_args_list[0] == mock.call('GET', '/apps', headers=mock.ANY)
