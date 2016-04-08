# coding: utf-8
from pysuru.base import BaseAPI

def test_baseapi_headers_should_return_authorization_header():
    api = BaseAPI(None, 'TOKEN')
    assert {'Authorization': 'bearer TOKEN'} == api.headers
