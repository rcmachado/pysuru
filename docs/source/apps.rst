Apps API
========

The ``AppsAPI`` class is responsible for interacting with ``/apps``
endpoints.

Listing apps
------------

To list all apps that you have access, just call ``all`` attribute:

.. code:: python

    apps = AppsAPI('<TARGET>', '<TOKEN>')
    my_apps = apps.all


You could also iterate over object directly:

.. code:: python

    apps = AppsAPI('<TARGET>', '<TOKEN>')
    for app in apps:
        # do something


Both returns a list of ``App`` objects containing basic metadata for
each app. Note that only data returned from ``/apps`` endpoint is
populated - there is no on-demand hydration or something like that.
This is intentional, to avoid overhead.

Retrieve specific app
---------------------

To get information for only one specific app, use the ``get`` method:

.. code:: python

    api = AppsAPI('<TARGET>', '<TOKEN>')
    app = api.get('my-awesome-app')
    print(app.name)

Retrieving data for a specific app returns more information that
listing them - but be aware that for each ``get`` call we make one call
for the ``/apps/<app_name>`` api.
