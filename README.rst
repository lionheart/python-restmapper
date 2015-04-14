Python-Restmapper
=================

|ci|_   |version|_   |downloads|_

.. |ci| image:: https://img.shields.io/travis/lionheart/python-restmapper.svg?style=flat
.. _ci: https://travis-ci.org/lionheart/restmapper.py

.. |downloads| image:: https://img.shields.io/pypi/dm/restmapper.svg?style=flat
.. _downloads: https://pypi.python.org/pypi/restmapper

.. |version| image:: https://img.shields.io/pypi/v/restmapper.svg?style=flat
.. _version: https://pypi.python.org/pypi/restmapper


python-restmapper is a tool that makes writing RESTful API clients a breeze. It removes all of the complexity with writing API-specific code, and lets you focus all your energy on the important stuff. Using Python-Requests, RestMapper will parse JSON and display responses nicely, based on a declarative format you provide for each API you integrate with (in progress).


Installation
------------

python-restmapper is available for download through the Python Package Index (PyPi). You can install it right away using pip or easy_install.

.. code:: bash

   pip install restmapper

No dependencies (besides Python 2.7).


Usage
-----

The first thing you need to do is generate a base RestMapper object that will allow you to instantiate a connection with a remote API.

.. code:: pycon

   >>> Twitter = RestMapper("https://api.twitter.com/1.1/", url_transformer=lambda url: url + ".json")


The next step is to provide authentication. For Twitter, you'll need to provide OAuth1 credentials (for other APIs, any other `requests-compatible <http://docs.python-requests.org/en/latest/user/authentication/>`_ auth object will do):

.. code:: pycon

   >>> from requests_oauthlib import OAuth1
   >>> auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
   >>> twitter = Twitter(auth=auth)

And start making calls. The API object is declarative, meaning that attributes and properties map 1-1 with the API you're integrating with. I.e., the below:

.. code:: pycon

   >>> response = twitter.statuses.mentions_timeline()

...will request https://api.twitter.com/1.1/statuses/mentions_timeline.json. Notice the url_transformer object used above---this adds ".json" to any request. You can pass in any function into the url_transformer object to handle more complicated situations.

If you want to pass in body data for a POST, provide a single argument to the call to the API, and specify "POST" as the first attribute. I.e.

.. code:: pycon

   >>> twitter.POST.my.request(data)

PATCH, PUT, GET, and POST are all supported (more will come later). GET is currently the default.

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

