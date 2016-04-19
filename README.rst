pysuru
======

|docs_build|

Python lib to access Tsuru API.

Install
-------

.. code:: shell

    pip install pysuru

Works on Python 2.7 and 3.5.

Usage
-----

.. code:: python

    from pysuru import TsuruAPI

    tsuru = TsuruAPI('<target>', '<token>')
    for app in tsuru.apps():
        print(app.name)

Dcoumentation
-------------

Documentation is available at http://pysuru.readthedocs.org/.

Developing
----------

Install development requirements:

.. code:: shell

    pip install -r requirements.txt

Run the tests:

.. code:: shell

    py.test --cov=pysuru

License
-------

MIT. See LICENSE_.


.. _LICENSE: ./LICENSE
.. |docs_build| image:: https://readthedocs.org/projects/pysuru/badge/?version=latest
    :target: http://pysuru.readthedocs.org/
    :alt: Build status of documentation
