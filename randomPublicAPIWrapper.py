import endpointWrappingClasses as bases
import json
import requests

"""
Class wrapping a public API returning a random other public API.
"""
class randomPublicAPIWrapper(bases.dataEndpointWrapper):
    def __init__(self, url):
        self.url = url
        self.method = "GET"
        self.body = None
        self.parameters = None

    """
    Constructor based on appropriately structured JSON config.
    
    :param configFile: Path to the config file.
    """
    @classmethod
    def makeFromConfig(cls, configFile):
        config = None

        with open(configFile) as f:
            config = json.load(f)

        if len(config["categories"]) > 0:
            # TODO: Implement this
            pass
        else:
            return cls(config["baseURL"])

    """
    DTO class for the object returned by the API.
    """
    class publicAPIDTO:
        def __init__(self, api, description, auth, https, cors, link, category):
            self.api = api
            self.description = description
            self.auth = auth
            self.https = https
            self.cors = cors
            self.link = link
            self.category = category

        """
        Constructor based on the dictionary returned when parsing the response content JSON.
        """
        @classmethod
        def makeFromDict(cls, apiDICT):
            return cls(apiDICT["API"], apiDICT["Description"], apiDICT["Auth"], apiDICT["HTTPS"], apiDICT["Cors"], apiDICT["Link"], apiDICT["Category"])

    """
    Get data from the API.
    """
    def getData(self):
        try:
            resp = self.performWebRequest(self.url, "GET", None, None)

            if resp.status_code == requests.codes.ok:
                respData = json.loads(resp.text)

                retAPI = self.publicAPIDTO.makeFromDict(respData["entries"][0])

                return bases.dataEndpointResponse.makeFromData(retAPI)
            else:
                return bases.dataEndpointResponse.makeFailed("Error fetching data! Status code {0}.".format(resp.status_code))
        except ValueError as e:
            return bases.dataEndpointResponse.makeFailed(e)
