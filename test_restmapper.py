#!/usr/bin/env python

import sys
import unittest
from restmapper import RestMapper

class TestRestMapper(unittest.TestCase):
    def setUp(self):
        pass

    def test_url_creation_with_kwargs_no_path(self):
        API = RestMapper("https://github.com/{username}/{repo}/")
        api = API(username="lionheartsw", repo="python-restmapper")
        response = api.issues(parse_response=False)
        assert(response.request.url == "https://github.com/lionheartsw/python-restmapper/issues")

    def test_url_creation_with_kwargs_and_path(self):
        API = RestMapper("https://github.com/{username}/{repo}/{path}")
        api = API(username="lionheartsw", repo="python-restmapper")
        response = api.issues(parse_response=False)
        assert(response.request.url == "https://github.com/lionheartsw/python-restmapper/issues")

    def test_url_creation_no_kwargs_mixed_attributes(self):
        API = RestMapper("https://github.com/")
        api = API()
        response = api.lionheartsw['python-restmapper'].issues(parse_response=False)
        assert(response.request.url == "https://github.com/lionheartsw/python-restmapper/issues")

    def test_url_creation_all_attributes(self):
        API = RestMapper("https://github.com/")
        api = API()
        response = api['lionheartsw']['python-restmapper']['issues'](parse_response=False)
        assert(response.request.url == "https://github.com/lionheartsw/python-restmapper/issues")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRestMapper)
    unittest.TextTestRunner(verbosity=2).run(suite)

