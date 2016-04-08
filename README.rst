pysuru
======

Python lib to access Tsuru API.

Install
-------

.. code:: shell

    pip install psuru

Works on Python 2.7 and 3.5.

Usage
-----

.. code:: python

    tsuru = TsuruAPI('<target>', '<token>')
    for app in tsuru.apps():
        print(app.name)

Developing
----------

.. code:: shell

    pip install -r requirements.txt

License
-------

MIT. See [LICENSE](./LICENSE).
