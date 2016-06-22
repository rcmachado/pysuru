Services Instances
==================

Creating a service instance
---------------------------

To create a new instance of a service:

.. code:: python

    data = {
        'name': 'my-dummy-instance',
        'service': 'dummy-service',
        'plan': 'dummy-plan',
        'description': 'A service instance with a dumb name',
        'owner': 'my-team',
    }
    client = TsuruClient()
    client.services_instances.create(data)

Binding to an app
-----------------

To bind a service instance to an app, call ``bind`` method:

.. code:: python

    client = TsuruClient()
    app.services.bind('my-service-instance')
