# coding: utf-8
try:
    from unittest import mock
except ImportError:
    import mock

from pysuru.http import HttpClient


def test_headers_attribute_should_always_have_authorization_header_with_token():
    client = HttpClient('TARGET', 'TOKEN')
    assert 'Authorization' in client.headers
    assert client.headers['Authorization'] == 'bearer TOKEN'


def test_urlopen_should_build_full_url_using_target_and_path():
    client = HttpClient('example.com/api', 'TOKEN')
    client.conn.request = mock.MagicMock()
    client.urlopen('GET', '/sample')

    expected_url = 'http://example.com/api/sample'

    assert client.conn.request.call_args_list == [
        mock.call('GET', expected_url, headers=mock.ANY, fields=None)]


def test_urlopen_should_merge_headers_argument_with_headers_attribute():
    my_headers = {
        'X-Custom-Header': 'custom value'
    }

    expected_headers = {
        'Authorization': 'bearer TOKEN',
        'X-Custom-Header': 'custom value'
    }

    client = HttpClient('TARGET', 'TOKEN')
    client.conn.request = mock.MagicMock()
    client.urlopen('GET', '/sample', headers=my_headers)

    assert client.conn.request.call_args_list == [
        mock.call('GET', mock.ANY, headers=expected_headers, fields=None)]
