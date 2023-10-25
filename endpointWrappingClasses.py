import requests

class dataEndpointWrapper:
    def __init__(self, url, method, body, parameters):
        self.url = url
        self.method = method
        self.body = body
        self.parameters = parameters

    def getData(self):
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
