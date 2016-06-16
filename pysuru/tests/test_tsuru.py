# coding: utf-8
import os

try:
    from unittest import mock
except ImportError:
    import mock

import pytest

from pysuru.tsuru import Tsuru


def test_create_object_with_credentials_from_arguments():
    os.environ['TSURU_TARGET'] = 'target'
    os.environ['TSURU_TOKEN'] = 'token'

    obj = Tsuru('target', 'token')
    assert obj.target == 'target'
    assert obj.token == 'token'


def test_create_object_with_credentials_from_env_variables():
    os.environ['TSURU_TARGET'] = 'target'
    os.environ['TSURU_TOKEN'] = 'token'

    obj = Tsuru()
    assert obj.target == 'target'
    assert obj.token == 'token'


def test_create_object_without_credentials_should_raise_error():
    os.environ['TSURU_TARGET'] = ''
    os.environ['TSURU_TOKEN'] = ''

    with pytest.raises(ValueError) as excinfo:
        Tsuru(None, 'something')
    assert 'target' in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        Tsuru('something', None)
    assert 'token' in str(excinfo.value)


@mock.patch('pysuru.tsuru.AppsAPI')
def test_apps_should_create_appsapi_object(AppsAPI, tsuru_apps_list):
    api = Tsuru('TARGET', 'TOKEN')
    api.apps()

    assert AppsAPI.call_args_list == [mock.call(api.client)]
