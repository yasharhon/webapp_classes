import requests

class dataEndpointWrapper:
    def __init__(self):
        pass

    def getData(self):
        pass

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

class dataEndpointResponse:
    def __init__(self, success, data, message):
        self.success = success
        self.data = data
        self.message = message

    @classmethod
    def makeFailed(cls, message):
        return cls(False, None, message)

    @classmethod
    def makeFromData(cls, data):
        return cls(True, data, "")
