from datetime import date
from pymoe.baseclass import BaseAPI
from pymoe.utilities.helpers import whatseason

class GetEndpoints:
    def __init__(self, parent):
        self.parent = parent

    def anime(self, item_id: int, fields: str = None):
        params = {"nsfw": "true"}
        if fields:
            params["fields"] = fields
        else:
            params["fields"] = "id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,nsfw,genres,media_type,status,num_episodes,start_season,broadcast,source,rating,studios,related_anime,related_manga"
            
        return self.parent._get(
            endpoint = f"anime/{item_id}",
            params = params
        )

class SearchEndpoints:
    def __init__(self, parent):
        self.parent = parent

    def anime(self, term: str, fields: str = None, limit: int = 10, offset: int = 0, nsfw: bool = False):
        params = {
            "q": term,
            "limit": limit,
            "offset": offset,
            "nsfw": "true" if nsfw else "false"
        }
        if fields:
            params["fields"] = fields
        else:
            params["fields"] = "id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,nsfw,genres,media_type,status,num_episodes,start_season,broadcast,source,rating,studios,related_anime,related_manga"

        return self.parent._get(
            endpoint = "anime",
            params = params
        )

    def season(self, season: str = None, seasonYear: int = date.today().year, limit: int = 10, offset: int = 0, nsfw: bool = False):
        myseason = season or whatseason(date.today().month)
        
        return self.parent._get(
            endpoint = f"anime/season/{seasonYear}/{myseason}",
            params = {
                "sort": "anime_score",
                "limit": limit,
                "offset": offset,
                "fields": "id,title,main_picture,alternative_titles,start_date,broadcast",
                "nsfw": "true" if nsfw else "false"
            }
        )

class MALAPI(BaseAPI):
    def __init__(self, web_client, client_id: str = None):
        super().__init__(web_client, "https://api.myanimelist.net/v2")
        self.apiheaders = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        if client_id:
            self.apiheaders["X-MAL-CLIENT-ID"] = client_id
            
        self.get = GetEndpoints(self)
        self.search = SearchEndpoints(self)

    def _get(self, **kwargs):
        url = f"{self.base_url}/{kwargs.get('endpoint')}"

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
