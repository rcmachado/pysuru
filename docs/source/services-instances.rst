Services Instances
==================

Services instances associated with an specific app can be consulted
directly through the ``App`` instance, via ``services`` attribute:

.. code:: python

    client = TsuruClient()
    app = client.apps.get('my-awesome-app')

    for service_instance in app.services.list():
        print('Service {si.name} is of type {si.type} with plan {si.plan}'
              .format(si=service_instance))

When accessing via an ``App`` instance, only services instances
associated with the app will be returned - even if you provide the
``app_name`` parameter to ``list`` method.
