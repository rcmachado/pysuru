# coding: utf-8
from pytest import fixture

@fixture
def tsuru_apps_list():
    return """[
      {
        "name": "app1-dev",
        "cname": ["app1-dev.cname.example.com"],
        "ip": "app1-dev.example.com"
      },
      {
        "name": "app1-prod",
        "cname": [],
        "ip": "app1-prod.example.com"
      },
      {
        "name": "app2-dev",
        "cname": [],
        "ip": "app2-dev.example.com"
      }
    ]"""
