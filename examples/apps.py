# coding: utf-8
import os
import sys

from pysuru import TsuruClient


TSURU_TARGET = os.environ.get('TSURU_TARGET', None)
TSURU_TOKEN = os.environ.get('TSURU_TOKEN', None)

if not TSURU_TARGET or not TSURU_TOKEN:
    print('You must set TSURU_TARGET and TSURU_TOKEN env variables.')
    sys.exit(1)

# Creating TsuruClient instance
tsuru = TsuruClient(TSURU_TARGET, TSURU_TOKEN)

# List all apps that this user has access to
for app in tsuru.apps.list():
    print('App: {}'.format(app.name))

# Get information for one app
app = tsuru.apps.get('my-awesome-app')
print('{app.name}: {app.description}'.format(app=app))

# Update specific app
tsuru.apps.update('my-awesome-app', {'description': 'My new awesome description'})
