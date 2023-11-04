import webappclasses.endpointWrappingClasses as bases
import json
import requests

"""
Class wrapping a public API returning a random image of a dog.
"""
class randomDogWrapper(bases.dataEndpointWrapper):
    def __init__(self, url):
        self.url = url

    """
    Constructor based on appropriately structured JSON config.

    :param configFile: Path to the config file.
    """
    @classmethod
    def makeFromConfig(cls, configFile):
        config = None

        with open(configFile) as f:
            config = json.load(f)

        return cls(config["baseURL"])

    """
    DTO class for the object returned by the API.
    """
    class randomDogDTO:
        def __init__(self, message, status):
            self.message = message
            self.status = status

        """
        Constructor based on the dictionary returned when parsing the response content JSON.
        """
        @classmethod
        def makeFromDict(cls, dogDICT):
            return cls(dogDICT["message"], dogDICT["status"])

    """
    Get data from the API.
    """
    def getData(self):
        try:
            resp = self.performWebRequest(self.url, "GET", None, None)

            if resp.status_code == requests.codes.ok:
                respData = json.loads(resp.text)

                retDog = self.randomDogDTO.makeFromDict(respData)

                return bases.dataEndpointResponse.makeFromData(retDog)
            else:
                return bases.dataEndpointResponse.makeFailed("Error fetching data! Status code {0}.".format(resp.status_code))
        except ValueError as e:
            return bases.dataEndpointResponse.makeFailed(e)
