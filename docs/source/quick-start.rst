Quick Start
===========

All operations must be done via ``TsuruClient`` class. Using the API
classes directly should be avoided.

Install
-------

The ``pysuru`` is available via pip:

.. code:: shell

    $ pip install pysuru

Usage
-----

After installing, call ``TsuruClient`` passing the target (the API
domain) and the Bearer authentication token:

.. code:: python

    client = TsuruClient('target.example.com', 'auth-token')
    client.apps.list()

You can also omit target and token if you have ``TSURU_TARGET`` and
``TSURU_TOKEN`` environment variables set:

.. code:: python

    client = TsuruClient()
    client.apps.list()

For other features, check the respective sections.
