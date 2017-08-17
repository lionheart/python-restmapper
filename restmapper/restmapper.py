# Copyright 2015-2017 Lionheart Software LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import requests

class RestMapper(object):
    def __init__(self, url_format, parsers={}, callback=None, method=requests.get, verify_ssl=True):
        self.url_format = url_format
        self.parsers = parsers
        self.callback = callback
        self._method = None
        self.verify_ssl = verify_ssl
        self.auth = None
        self.client = requests.session()

    def __call__(self, auth=None, headers={}, params={}, **kwargs):
        """ Set request session with kwargs """
        session = requests.Session()
        session.auth = auth
        session.headers.update(headers)
        session.params = params

        self.url_format_parameters = kwargs
        self.session = session
        return self

    def __repr__(self):
        return "<RestMapper url={}>".format(self.url_format)

    @property
    def method(self):
        if self._method is None:
            return self.session.get
        else:
            return self._method

    @method.setter
    def method(self, method):
        self._method = method

    def __getitem__(self, k):
        return self.__getattr__(k)

    def __getattr__(self, k):
        if k in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
            self.method = getattr(self.session, k.lower())
            return self
        else:
            method = self.method
            self.method = None
            return RestMapperCall(self.url_format, method, k, self.auth,
                    self.parsers, self.callback, self.verify_ssl, **self.url_format_parameters)


class RestMapperCall(object):
    def __init__(self, url_format, method, path, auth, parsers, callback=None, verify_ssl=True, **kwargs):
        self.method = method
        self.components = [path]
        self.url_format = url_format
        self.auth = auth
        self.parsers = parsers
        self.method = method
        self.url_format_parameters = kwargs

        if callback is None:
            self.callback = lambda response: response
        else:
            self.callback = callback

        self.verify_ssl = verify_ssl

    def __getattr__(self, k):
        self.components.append(k)
        return self

    def __getitem__(self, k):
        self.components.append(k)
        return self

    def __call__(self, *args, **kwargs):
        path = "/".join(self.components)

        if "{path}" in self.url_format:
            url_format_parameters = self.url_format_parameters
            url_format_parameters.update({'path': path})
            url = self.url_format.format(**url_format_parameters)
        else:
            url = self.url_format.format(**self.url_format_parameters) + path

        parse_response = kwargs.get('parse_response', True)
        headers = kwargs.get('headers', {})

        if 'headers' in kwargs:
            del kwargs['headers']

        if 'parse_response' in kwargs:
            del kwargs['parse_response']

        if 'params' in kwargs:
            params = kwargs['params']
            del kwargs['params']

            params.update(kwargs)
        else:
            params = kwargs

        if len(args) > 0:
            data = args[0]
        else:
            data = None

        response = self.method(
            url,
            data=data,
            params=params,
            auth=self.auth,
            verify=self.verify_ssl,
            headers=headers
        )

        Object = None
        if parse_response:
            parse_as = None
            for (component, parser) in list(self.parsers.items()):
                if component in self.components:
                    Object = parser

            try:
                json_response = response.json()
            except ValueError:
                return response
            else:
                self.callback(json_response)

                if parse_response and Object is not None:
                    if isinstance(json_response, list):
                        return [Object(**Object.parse(k)) for k in json_response]
                    else:
                        return Object(**Object.parse(json_response))
                else:
                    return json_response
        else:
            return response

