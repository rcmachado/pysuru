Apps
====

To interact with apps in Tsuru API, use the ``apps`` property on a
``TsuruClient`` instance.

Listing apps
------------

To list all apps that your team can see, just use ``list`` method:

.. code:: python

    client = TsuruClient('<TARGET>', '<TOKEN>')
    apps = client.apps.list()
    for app in apps:
        print('App: {}'.format(app.name))

It'll return a list of ``App`` objects containing basic metadata for
each app. Note that only data returned by Tsuru API (from ``/apps``
endpoint, to be more specific) is populated in the object. There is no
automatic hydration - if you need other information is recomended to
call ``get`` method for the specific app.

In the future this call can be made on-demand in such cases.

Retrieve app
------------

To get information for only one specific app, use the ``get`` method
passing the app name:

.. code:: python

    client = TsuruClient('<TARGET>', '<TOKEN>')
    apps = client.apps.get('my-awesome-app')
    print('App: {}'.format(app.name))

Retrieving data for a specific app returns more information that
listing them - but be aware that for each ``get`` call we make one call
to the ``/apps/<app_name>`` api - there is no cache involved. Store the
``App`` instance in a variable, if you need.

Creating app
------------

You can call ``create`` method to create an app:

.. code:: python

    client = TsuruClient('<TARGET>', '<TOKEN>')
    app = client.apps.create({
        'name': 'my-awesome-app',
        'description': 'My Awesome App does something very cool',
        'pool': 'my-pool',
    })
    print("App: {}".format(app.name))

Note that there is no automatic validation for the data informed. This
can change in the future (checking with attributes specified in ``App``
class, for example). The ``create`` method returns an ``App`` instance.

Updating an app
---------------

To update an app, just call ``update`` method passing app name and the
new data:

.. code:: python

    client = TsuruClient('<TARGET>', '<TOKEN>')
    client.apps.update('my-app', {'description': 'new description'})

Only the data informed will be update. Note that **no check is made -
the data is passed as is to API**.

Removing an app
---------------

To remove an app, call ``delete`` method passing the app name:

.. code:: python

    client = TsuruClient('<TARGET>', '<TOKEN>')
    client.apps.delete('my-old-app')
