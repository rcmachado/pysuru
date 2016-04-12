# coding: utf-8
import os
import sys

from pysuru import TsuruAPI


TSURU_TARGET = os.environ.get('TSURU_TARGET', None)
TSURU_TOKEN = os.environ.get('TSURU_TOKEN', None)

if not TSURU_TARGET or not TSURU_TOKEN:
    print('You must set TSURU_TARGET and TSURU_TOKEN.')
    sys.exit(1)

api = TsuruAPI(TSURU_TARGET, TSURU_TOKEN)

# List all apps that this token has access to
for app in api.apps():
    print(app.name)

# Update one specific app
api.apps().update('my-awesome-app', {'description': 'My awesome app'})
