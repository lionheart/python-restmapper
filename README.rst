Python-Restmapper
=================

|ci|_   |version|_   |downloads|_

.. |ci| image:: https://img.shields.io/travis/lionheart/python-restmapper.svg?style=flat
.. _ci: https://travis-ci.org/lionheart/restmapper.py

.. |downloads| image:: https://img.shields.io/pypi/dm/restmapper.svg?style=flat
.. _downloads: https://pypi.python.org/pypi/restmapper

.. |version| image:: https://img.shields.io/pypi/v/restmapper.svg?style=flat
.. _version: https://pypi.python.org/pypi/restmapper


Installation
------------

python-restmapper is available for download through the Python Package Index (PyPi). You can install it right away using pip or easy_install.

.. code:: bash

   pip install restmapper

No dependencies (besides Python 2.7).


Miscellaneous
'''''''''''''

By default, python-restmapper will return parsed JSON objects. If you'd like the raw response object for a request, just pass in `parse_response=False`.

.. code:: pycon

   >>> response = ...
   ... your org ...


Support
-------

If you like this library, or need help implementing it, send us an email: hi@lionheartsw.com.

License
-------

.. image:: http://img.shields.io/pypi/l/restmapper.svg?style=flat
   :target: LICENSE

Apache License, Version 2.0. See `LICENSE <LICENSE>`_ for details.

