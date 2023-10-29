import requests

"""
Base class meant for use when wrapping other public APIs.
"""
class dataEndpointWrapper:
    """
    Virtual init, meant to be implemented in inheriting classes
    """
    def __init__(self):
        pass

    """
    Virtual, meant to be implemented in inheriting classes
    """
    def getData(self):
        pass

    """
    Perform a web request.

    :param url: The URL to where the request is to be performed.
    :param method: The HTTP method to be used, provided as a string in all-caps. Only GET currently implemented.
    :param body: Request body.
    :param parameters: Request parameters.
    :returns: The full response object.
    :raises Error: Request errors.
    """
    def performWebRequest(self, url, method, body, parameters):
        if method == "GET":
            return requests.get(url)
        elif method == "POST":
            # return requests.post(url, body=body, data=body)
            pass
        elif method == "PUT":
            # requests.put(url)
            pass
        elif method == "DELETE":
            # return requests.delete(url)
            pass
        elif method == "HEAD":
            # return requests.head(url)
            pass
        elif method == "OPTIONS":
            # return requests.options('https://httpbin.org/get')
            pass

"""
Object wrapping the response from a public API. To be returned in the getData function.
"""
class dataEndpointResponse:
    def __init__(self, success, data, message):
        self.success = success
        self.data = data
        self.message = message

    """
    Constructor for an object denoting failure to fetch data.
    
    :param message: The error message to be returned.
    """
    @classmethod
    def makeFailed(cls, message):
        return cls(False, None, message)

    """
    Constructor for an object denoting successful data fetch.
    
    :param data: Representation of fetched data.
    """
    @classmethod
    def makeFromData(cls, data):
        return cls(True, data, "")
