Python-Restmapper
=================

|ci|_   |version|_   |downloads|_

.. |ci| image:: https://img.shields.io/travis/lionheart/python-restmapper.svg?style=flat
.. _ci: https://travis-ci.org/lionheart/restmapper.py

.. |downloads| image:: https://img.shields.io/pypi/dm/restmapper.svg?style=flat
.. _downloads: https://pypi.python.org/pypi/restmapper

.. |version| image:: https://img.shields.io/pypi/v/restmapper.svg?style=flat
.. _version: https://pypi.python.org/pypi/restmapper


python-restmapper is a tool that makes writing RESTful API clients a breeze. It removes all of the complexity with writing API-specific code, and lets you focus all your energy on the important stuff. Restmapper will even parse JSON and XML objects and display them nicely, based on a declarative format you provide for each API you integrate with.


Installation
------------

python-restmapper is available for download through the Python Package Index (PyPi). You can install it right away using pip or easy_install.

.. code:: bash

   pip install restmapper

No dependencies (besides Python 2.7).


Usage
-----

The first thing you need to do is generate a base RestMapper object that will allow you to instantiate a connection a remote API with authentication.

.. code:: pycon

   >>> from requests_oauthlib import OAuth1
   >>> Twitter = RestMapper("https://api.twitter.com/1.1/", url_transformer=lambda url: url + ".json")


Now, just get an access key and secret, and then start making calls with the API object.

.. code:: pycon

   >>> auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
   >>> twitter = Twitter(auth=auth)
   >>> response = twitter.statuses.mentions_timeline()


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

