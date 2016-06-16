# coding: utf-8
from pysuru.base import BaseAPI, ObjectMixin


def SKIP_test_build_url_should_return_full_api_endpoint():
    api = BaseAPI('http://example.com/', None)
    assert 'http://example.com/apis' == api.build_url('/apis')

    api = BaseAPI('http://example.com', None)
    assert 'http://example.com/apis' == api.build_url('/apis')


def test_baseobject_create_should_ignore_unknown_fields():
    data = {'field1': 'value1', 'unknown': 'ignored'}
    created = _DummyObject.create(**data)

    assert created.attrs['field1'] == 'value1'
    assert 'unknown' not in created.attrs


class _DummyObject(ObjectMixin):
    _fields = ('field1', 'field2')

    def __init__(self, **kwargs):
        self.attrs = kwargs
