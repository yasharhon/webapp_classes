import endpointWrappingClasses as bases
import json
import requests

class randomPublicAPIWrapper(bases.dataEndpointWrapper):
    def __init__(self, url):
        self.url = url
        self.method = "GET"
        self.body = None
        self.parameters = None

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

    class publicAPIDTO:
        def __init__(self, api, description, auth, https, cors, link, category):
            self.api = api
            self.description = description
            self.auth = auth
            self.https = https
            self.cors = cors
            self.link = link
            self.category = category

        @classmethod
        def makeFromDict(cls, apiDICT):
            return cls(apiDICT["API"], apiDICT["Description"], apiDICT["Auth"], apiDICT["HTTPS"], apiDICT["Cors"], apiDICT["Link"], apiDICT["Category"])

    def getData(self):
        resp = self.performWebRequest(self.url, "GET", None, None)

        if resp.status_code == requests.codes.ok:
            respData = json.loads(resp.text)

            retAPI = self.publicAPIDTO.makeFromDict(respData["entries"][0])

            return bases.dataEndpointResponse.makeFromData(retAPI)
        else:
            return bases.endpointResponse.makeFailed("Error fetching data! Status code {0}.".format(resp.status_code))
