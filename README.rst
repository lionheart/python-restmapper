Python-Restmapper |ci| |downloads| |version|
============================================

python-restmapper is a tool that makes writing RESTful API clients a breeze. It removes all of the complexity with writing API-specific code, and lets you focus all your energy on the important stuff. Using Python-Requests, RestMapper will parse JSON and display responses nicely, based on a declarative format you provide for each API you integrate with (in progress).

Installation
------------

python-restmapper is available for download through the Python Package Index (PyPi). You can install it right away using pip or easy_install.

.. code:: bash

   pip install restmapper

Usage
-----

The first thing you need to do is generate a base RestMapper object that will allow you to instantiate a connection with a remote API.

.. code:: pycon

   >>> Twitter = RestMapper("https://api.twitter.com/1.1/{path}.json")

`{path}` is just a placeholder for the rest of the path. You'll specify this later when making API calls.

Twitter's API is protected by OAuth1, so the next step is to provide authentication. When integrating with any other API, any `requests-compatible <http://docs.python-requests.org/en/latest/user/authentication/>`_ auth object can be provided.

.. code:: pycon

   >>> from requests_oauthlib import OAuth1
   >>> auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
   >>> twitter = Twitter(auth=auth)

Now you can start making calls. The API object's attributes and properties map one-to-one with the API you're integrating with. E.g., the below:

.. code:: pycon

   >>> response = twitter.statuses.mentions_timeline()

...will request https://api.twitter.com/1.1/statuses/mentions_timeline.json. The path implied by the attribute syntax is inserted right where the `path` placeholder is in the `Twitter` object's instantiation earlier.

If you want to pass in body data for a POST, provide a single argument to the call to the API, and specify "POST" as the first attribute. I.e.

.. code:: pycon

   >>> twitter.POST.my.request(data)

PATCH, PUT, GET, and POST are all supported. GET is currently the default.

Miscellaneous
'''''''''''''

By default, python-restmapper will return parsed JSON objects. If you'd like the raw response object for a request, just pass in `parse_response=False` as an argument to the API object.

Support
-------

If you like this library, or need help implementing it, send us an email: hi@lionheartsw.com.

License
-------

.. image:: http://img.shields.io/pypi/l/restmapper.svg?style=flat
   :target: LICENSE

Apache License, Version 2.0. See `LICENSE <LICENSE>`_ for details.

.. |ci| image:: https://img.shields.io/travis/lionheart/python-restmapper.svg?style=flat
.. _ci: https://travis-ci.org/lionheart/restmapper.py

.. |downloads| image:: https://img.shields.io/pypi/dm/restmapper.svg?style=flat
.. _downloads: https://pypi.python.org/pypi/restmapper

.. |version| image:: https://img.shields.io/pypi/v/restmapper.svg?style=flat
.. _version: https://pypi.python.org/pypi/restmapper

