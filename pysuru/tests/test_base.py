# coding: utf-8
from pysuru.base import BaseAPI

def test_baseapi_headers_should_return_authorization_header():
    api = BaseAPI(None, 'TOKEN')
    assert {'Authorization': 'bearer TOKEN'} == api.headers


def test_build_url_should_return_full_api_endpoint():
    api = BaseAPI('http://example.com/', None)
    assert 'http://example.com/apis' == api.build_url('/apis')

    api = BaseAPI('http://example.com', None)
    assert 'http://example.com/apis' == api.build_url('/apis')
