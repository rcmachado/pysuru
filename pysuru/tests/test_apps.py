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


def test_update_should_make_request_with_correct_payload():
    AppsAPI.post_json = mock.MagicMock()
    AppsAPI.post_json.return_value.status = 200

    payload = {'random-field': 'random-value'}

    apps = AppsAPI('TARGET', 'TOKEN')

    assert apps.update('app-name', payload) is True
    assert AppsAPI.post_json.call_args_list[0] == mock.call('/apps/app-name', payload)
