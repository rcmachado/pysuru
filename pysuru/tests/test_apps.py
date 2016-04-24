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

    apps = AppsAPI(None)

    assert 3 == len(apps.all)
    assert isinstance(apps.all[0], App)
    assert AppsAPI.get_request.call_args_list == [mock.call('/apps')]


def test_update_should_make_request_with_correct_payload():
    client= mock.MagicMock()
    client.urlopen.return_value.status = 200

    payload = {'random-field': 'random-value'}

    apps = AppsAPI(client)

    assert apps.update('app-name', payload) is True
    assert client.urlopen.call_args_list == [
        mock.call('POST', '/apps/app-name', body=json.dumps(payload))]
