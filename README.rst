pysuru
======

|tests_build| |docs_build|

Python lib to interact with Tsuru API. Works with Python 2.7+ and 3.5+.

Install
-------

.. code:: shell

    pip install pysuru

Usage
-----

.. code:: python

    from pysuru import TsuruClient

    tsuru = TsuruClient('<target>', '<token>')
    for app in tsuru.apps.list():
        print(app.name)

Documentation
-------------

Full documentation is available at http://pysuru.readthedocs.org/.

Developing
----------

We use tox_ to test in multiple versions:

.. code:: shell

    tox

If you prefer to run the tests separately, install development
requirements:

.. code:: shell

    pip install -r requirements.txt

Run the lint and tests:

.. code:: shell

    make lint test

Don't forget to write documentation for your code!

License
-------

MIT. See LICENSE_.


.. _LICENSE: ./LICENSE
.. |tests_build| image:: https://travis-ci.org/rcmachado/pysuru.svg?branch=master
    :target: https://travis-ci.org/rcmachado/pysuru
    :alt: Tests
.. |docs_build| image:: https://readthedocs.org/projects/pysuru/badge/?version=latest
    :target: http://pysuru.readthedocs.org/
    :alt: Build status of documentation
.. _tox: https://pypi.python.org/pypi/tox
