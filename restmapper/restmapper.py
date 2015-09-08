import json
import requests

class RestMapper(object):
    def __init__(self, endpoint, parsers={}, callback=None, url_transformer=None, method=requests.get, verify_ssl=True):
        self.endpoint = endpoint
        self.parsers = parsers
        self.callback = callback
        self._method = None
        self.verify_ssl = verify_ssl
        self.url_transformer = url_transformer
        self.auth = None
        self.client = requests.session()

    def __call__(self, **kwargs):
        """ Set request session with kwargs """
        session = requests.Session()
        session.auth = kwargs.get('auth')
        session.headers.update(kwargs.get('headers', {}))
        session.params = kwargs.get('params', {})

        self.session = session
        return self

    @property
    def method(self):
        if self._method is None:
            return self.session.get
        else:
            return self._method

    @method.setter
    def method(self, method):
        self._method = method

    def __getattr__(self, k):
        if k in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
            self.method = getattr(self.session, k.lower())
            return self
        else:
            method = self.method
            self.method = None
            return RestMapperCall(self.endpoint, method, k,
                    self.auth, self.parsers, self.callback,
                    self.url_transformer, self.verify_ssl)


class RestMapperCall(object):
    def __init__(self, endpoint, method, path, auth, parsers, callback=None, url_transformer=None, verify_ssl=True):
        self.method = method
        self.components = [path]
        self.endpoint = endpoint
        self.auth = auth
        self.parsers = parsers
        self.method = method

        if callback is None:
            self.callback = lambda response: response
        else:
            self.callback = callback

        if url_transformer is None:
            self.url_transformer = lambda url: url
        else:
            self.url_transformer = url_transformer

        self.verify_ssl = verify_ssl

    def __getattr__(self, k):
        self.components.append(k)
        return self

    def __getitem__(self, k):
        self.components.append(k)
        return self

    def __call__(self, *args, **kwargs):
        url = "{}{}".format(self.endpoint, "/".join(self.components))
        url = self.url_transformer(url)

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
            for component, parser in self.parsers.iteritems():
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
                        return map(lambda k: Object(**Object.parse(k)), json_response)
                    else:
                        return Object(**Object.parse(json_response))
                else:
                    return json_response
        else:
            return response

