# coding: utf-8
try:
    from unittest import mock
except ImportError:
    import mock

from pysuru.base import BaseAPI, ObjectMixin


def SKIP_test_build_url_should_return_full_api_endpoint():
    api = BaseAPI('http://example.com/', None)
    assert 'http://example.com/apis' == api.build_url('/apis')

    api = BaseAPI('http://example.com', None)
    assert 'http://example.com/apis' == api.build_url('/apis')


def SKIP_test_baseapi_get_request_should_return_parsed_data():
    api = BaseAPI('http://example.com', None)

    with mock.patch.object(api.client, 'request') as request:
        request.return_value.status = 200
        request.return_value.data.decode.return_value = '{"key":"value"}'
        response = api.get_request('/endpoint')

    expected_url = 'http://example.com/endpoint'

    assert response == (200, {'key': 'value'})
    assert request.call_args_list == [mock.call('GET', expected_url, headers=api.headers)]


def SKIP_test_baseapi_get_request_should_return_none_if_empty_response():
    api = BaseAPI('http://example.com', None)

    with mock.patch.object(api.client, 'request') as request:
        request.return_value.status = 500
        request.return_value.data = ''
        response = api.get_request('/endpoint')

    assert response == (500, None)


def test_baseobject_create_should_ignore_unknown_fields():
    data = {'field1': 'value1', 'unknown': 'ignored'}
    created = _DummyObject.create(**data)

    assert created.attrs['field1'] == 'value1'
    assert 'unknown' not in created.attrs


class _DummyObject(ObjectMixin):
    _fields = ('field1', 'field2')

    def __init__(self, **kwargs):
        self.attrs = kwargs
