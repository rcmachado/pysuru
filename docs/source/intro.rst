Intro
=====

``pysuru`` is a python library wrapper for Tsuru API version 1.0 and up.

Goals
-----

``pysuru`` was develop with these 3 goals in mind:

* Easy to use: The interface should be as easier to use as possible.
  If the user already knows how to create an app, creating a user or a
  service should not have to be much different.
* Fewer dependencies as possible: Use as little as dependencies as
  possible. This aims to make it easier to install and upgrade lib
  dependencies without require too much effort from the user.
* Python 3 first: We are in 2016, not 2006 (although it will work with
  python 2.7+ too).

Why not use official lib?
-------------------------

There is the official python-tsuruclient_ lib, but at the time of this
writing it isn't compatible with version 1.0 of API. Also, the official
lib uses requests_ and, to keep dependencies to a minimum, we opted for
using urllib3_ directly.

To see basic usage, go to ``Quick Start``.

.. _python-tsuruclient: https://github.com/tsuru/python-tsuruclient
.. _requests: http://example.com
.. _urllib3: http://example.com
