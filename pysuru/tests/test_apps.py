# coding: utf-8
import json
import pytest

try:
    from unittest import mock
except ImportError:
    import mock

from pysuru.apps import App, AppsAPI, AppDoesNotExists, AppError


def test_appsapi_all_should_return_list_of_apps(tsuru_apps_list):
    client = mock.MagicMock()
    client.get.return_value = (200, json.loads(tsuru_apps_list))

    apps = AppsAPI(client)

    all_apps = apps.list()

    assert 3 == len(all_apps)
    assert isinstance(all_apps[0], App)
    assert client.get.call_args_list == [mock.call('/apps')]


def test_update_should_make_request_with_correct_payload():
    client = mock.MagicMock()
    client.put.return_value.status = 200

    payload = {'random-field': 'random-value'}

    apps = AppsAPI(client)

    assert apps.update('app-name', payload) is True
    assert client.put.call_args_list == [
        mock.call('/apps/app-name', data=payload)]


def test_delete_should_make_request_with_correct_params():
    client = mock.MagicMock()
    client.urlopen.return_value.status = 200

    apps = AppsAPI(client)

    assert apps.delete('app-name') is True
    assert client.urlopen.call_args_list == [
        mock.call('DELETE', '/apps/app-name')]


def test_delete_should_raise_error_if_app_does_not_exists():
    client = mock.MagicMock()
    client.urlopen.return_value.status = 404

    apps = AppsAPI(client)

    with pytest.raises(AppDoesNotExists):
        apps.delete('app-does-not-exists')


def test_delete_should_raise_apperror_if_unknown_error_ocurred():
    client = mock.MagicMock()
    client.urlopen.return_value.status = 500

    apps = AppsAPI(client)

    with pytest.raises(AppError):
        apps.delete('forced-app-error')
