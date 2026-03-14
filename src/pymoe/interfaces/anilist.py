from datetime import date
from pymoe.baseclass import BaseAPI
from pymoe.utilities.helpers import whatseason
from pymoe.utilities.anilist_queries import (
    # ANIME ENDPOINTS
    GET_ANIME_QUERY,
    GET_ANIMESTREAMING_QUERY,
    GET_ANIMEAIRINGSCHEDULE_QUERY,
    SEARCH_ANIMESEASON_QUERY,
    SEARCH_ANIME_QUERY,

    # MANGA ENDPOINTS
    GET_MANGA_QUERY,
    SEARCH_MANGA_QUERY,

    # SHARED ENDPOINTS
    GET_CHARACTER_QUERY,
    GET_STAFF_QUERY,
    GET_STUDIO_QUERY,
    SEARCH_CHARACTER_QUERY,
    SEARCH_STAFF_QUERY,
    SEARCH_STUDIO_QUERY
)

# TODO: Type classing
class GetEndpoints:
    def __init__(self, parent):
        self.parent = parent

    # ANIME
    def anime(self, item_id):
        return self.parent._post(
            headers = None,
            data = {
                "query": GET_ANIME_QUERY,
                "variables": {
                    "id": item_id
                }
            }
        )

    def streaming(self, item_id):
        return self.parent._post(
            headers = None,
            data = {
                "query": GET_ANIMESTREAMING_QUERY,
                "variables": {
                    "id": item_id
                }
            }
        )

    def airing_schedule(self, item_id):
        return self.parent._post(
            headers = None,
            data = {
                "query": GET_ANIMEAIRINGSCHEDULE_QUERY,
                "variables": {
                    "id": item_id
                }
            }
        )

    # SHARED
    def character(self, item_id):
        return self.parent._post(
            headers = None,
            data = {
                "query": GET_CHARACTER_QUERY,
                "variables": {
                    "id": item_id
                }
            }
        )

    def staff(self, item_id):
        return self.parent._post(
            headers = None,
            data = {
                "query": GET_STAFF_QUERY,
                "variables":{
                    "id": item_id
                }
            }
        )

    def studio(self, item_id):
        return self.parent._post(
            headers = None,
            data = {
                "query": GET_STUDIO_QUERY,
                "variables": {
                    "id": item_id
                }
            }
        )

    # MANGA
    def manga(self, item_id):
        return self.parent._post(
            headers = None,
            data = {
                "query": GET_MANGA_QUERY,
                "variables": {
                    "id": item_id
                }
            }
        )


class SearchEndpoints:
    def __init__(self, parent):
        self.parent = parent

    # ANIME
    def season(self, the_season: str | None = None, the_year: int = date.today().year, page: int = 1, per_page: int = 3):
        return self.parent._post(
            headers = None,
            data = {
                "query": SEARCH_ANIMESEASON_QUERY,
                "variables":{
                    "season": whatseason(date.today().month).upper() if the_season is None else the_season.upper(),
                    "seasonYear": the_year,
                    "page": page,
                    "perPage": per_page
                }
            }
        )

    def anime(self, term: str, page: int = 1, per_page: int = 3):
        return self.parent._post(
            headers = None,
            data = {
                "query": SEARCH_ANIME_QUERY,
                "variables": {
                    "query": term,
                    "page": page,
                    "perPage": per_page
                }
            }
        )

    # MANGA
    def manga(self, term: str, page: int = 1, per_page: int = 3):
        return self.parent._post(
            headers = None,
            data = {
                "query": SEARCH_MANGA_QUERY,
                "variables": {
                    "query": term,
                    "page": page,
                    "perPage": per_page
                }
            }
        )

    # SHARED
    def characters(self, term: str, page: int = 1, per_page: int = 3):
        return self.parent._post(
            headers = None,
            data = {
                "query": SEARCH_CHARACTER_QUERY,
                "variables": {
                    "query": term,
                    "page": page,
                    "perPage": per_page
                }
            }
        )

    def staff(self, term: str, page: int = 1, per_page: int = 3):
        return self.parent._post(
            headers = None,
            data = {
                "query": SEARCH_STAFF_QUERY,
                "variables": {
                    "query": term,
                    "page": page,
                    "perPage": per_page
                }
            }
        )

    def studios(self, term: str, page: int = 1, per_page: int = 3):
        return self.parent._post(
            headers = None,
            data = {
                "query": SEARCH_STUDIO_QUERY,
                "variables": {
                    "query": term,
                    "page": page,
                    "perPage": per_page
                }
            }
        )


class AnilistAPI(BaseAPI):
    def __init__(self, web_client):
        super().__init__(web_client, "https://graphql.anilist.co")
        self.apiheaders = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.get = GetEndpoints(self)
        self.search = SearchEndpoints(self)

    #TODO: Are we implementing custom iterators?
    # Anilist does not use get methods
    def _get(self, **kwargs):
        pass

    def _post(self, **kwargs):
        url = self.base_url

        merged = None
        if kwargs.get("headers", False):
            merged = self._merge_headers(kwargs.get("headers")).update(self.apiheaders)
        else:
            merged = self._merge_headers(self.apiheaders)

        response = self.web_client.post(
            url,
            headers = merged,
            json = kwargs.get("data")
        )
        return response.json()
