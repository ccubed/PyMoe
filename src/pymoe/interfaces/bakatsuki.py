from pymoe.baseclass import BaseAPI

class GetEndpoints:
    def __init__(self, parent):
        self.parent = parent

    def light_novels(self, language: str = "English", cmcontinue: str = None):
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": f"Category:Light_novel_({language.replace(' ', '_')})",
            "cmtype": "page",
            "cmlimit": "500",
            "format": "json"
        }
        if cmcontinue:
            params["cmcontinue"] = cmcontinue
            
        return self.parent._get(params=params)

    def teasers(self, language: str = "English", cmcontinue: str = None):
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": f"Category:Teaser_({language.replace(' ', '_')})",
            "cmtype": "page",
            "cmlimit": "500",
            "format": "json"
        }
        if cmcontinue:
            params["cmcontinue"] = cmcontinue
            
        return self.parent._get(params=params)

    def web_novels(self, language: str = "English", cmcontinue: str = None):
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": f"Category:Web_novel_({language.replace(' ', '_')})",
            "cmtype": "page",
            "cmlimit": "500",
            "format": "json"
        }
        if cmcontinue:
            params["cmcontinue"] = cmcontinue
            
        return self.parent._get(params=params)

class BakatsukiAPI(BaseAPI):
    def __init__(self, web_client):
        super().__init__(web_client, "https://www.baka-tsuki.org/project/api.php")
        self.apiheaders = {}
        self.get = GetEndpoints(self)

    def _get(self, **kwargs):
        url = self.base_url

        merged = None
        if kwargs.get("headers", False):
            merged = self._merge_headers(kwargs.get("headers")).update(self.apiheaders)
        else:
            merged = self._merge_headers(self.apiheaders)

        response = self.web_client.get(
            url,
            headers = merged,
            params = kwargs.get("params", None)
        )
        return response.json()

    def _post(self, **kwargs):
        pass
