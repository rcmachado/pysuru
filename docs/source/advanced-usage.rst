Advanced Usage
==============

    > Note: In most cases there is no need to use the advanced features
    describe in this document. Also notes that this interface is
    subject to change in future versions.

Retrive object attributes
-------------------------

If you need a way to retrieve object properties, you can use
``ObjectMixin.ATTRIBUTES`` method. This is useful to inspect all the
attributes from a specific resource. For example, to get all attributes
that an App object exposes, you could do:

.. code-block:: python

    print(App.ATTRIBUTES())
