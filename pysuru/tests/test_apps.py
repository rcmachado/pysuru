# coding: utf-8
import json

try:
    from unittest import mock
except ImportError:
    import mock

from pysuru.apps import App, AppsAPI


def test_appsapi_all_should_return_list_of_apps(tsuru_apps_list):
    AppsAPI.get_request = mock.MagicMock()
    AppsAPI.get_request.return_value = (200, json.loads(tsuru_apps_list))

    apps = AppsAPI('TARGET', 'TOKEN')

    assert 3 == len(apps.all)
    assert isinstance(apps.all[0], App)
    assert AppsAPI.get_request.call_args_list == [mock.call('/apps')]


def test_update_should_make_request_with_correct_payload():
    AppsAPI.post_json = mock.MagicMock()
    AppsAPI.post_json.return_value.status = 200

    payload = {'random-field': 'random-value'}

    apps = AppsAPI('TARGET', 'TOKEN')

    assert apps.update('app-name', payload) is True
    assert AppsAPI.post_json.call_args_list[0] == mock.call('/apps/app-name', payload)
