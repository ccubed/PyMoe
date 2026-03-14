from datetime import date
from pymoe.baseclass import BaseAPI
from pymoe.utilities.helpers import whatseason

class GetEndpoints:
    def __init__(self, parent):
        self.parent = parent

    def character(self, item_id):
        return self.parent._get(
            endpoint = f"characters/{item_id}"
        )

    def anime(self, item_id):
        return self.parent._get(
            endpoint = f"anime/{item_id}"
        )

    def manga(self, item_id):
        return self.parent._get(
            endpoint = f"manga/{item_id}"
        )

    def episode(self, item_id):
        return self.parent._get(
            endpoint = f"episodes/{item_id}"
        )

    def anime_staff(self, item_id):
        return self.parent._get(
            endpoint = f"anime-staff/{item_id}/person"
        )

    def manga_staff(self, item_id):
        return self.parent._get(
            endpoint = f"manga-staff/{item_id}/person"
        )

    def studio(self, item_id):
        return self.parent._get(
            endpoint = f"anime-productions/{item_id}/producer"
        )

    def producer(self, item_id):
        return self.parent._get(
            endpoint = f"producers/{item_id}"
        )

    def streaming(self, item_id: int):
        data = self.anime(item_id)['data']['relationships']['streamingLinks']['links']['related'].split("edge")[1][1:]

        return self.parent._get(
            endpoint = data
        )

class SearchEndpoints:
    def __init__(self, parent):
        self.parent = parent

    def manga(self, term: str):
        return self.parent._get(
            endpoint = "/manga",
            params = {
                "filter[text]": term
            }
        )

    def anime(self, term: str):
        return self.parent._get(
            endpoint = "/anime",
            params = {
                "filter[text]": term
            }
        )

    def characters(self, term: str):
        return self.parent._get(
            endpoint = "/characters",
            params = {
                "filter[text]": term
            }
        )

    def season(self, theseason: str | None = None, year: int = date.today().year):
        return self.parent._get(
            endpoint = "/anime",
            params = {
                "filter[season]": whatseason(date.today().month).upper() if theseason is None else theseason.upper(),
                "filter[seasonYear]": year
            }
        )

class KitsuAPI(BaseAPI):
    def __init__(self, web_client):
        super().__init__(web_client, "https://kitsu.io/api/edge")
        self.apiheaders = {
            "Content-Type": "application/vnd.api+json",
            "Accept": "application/vnd.api+json"
        }
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

    # Kitsu does not use post endpoints
    def _post(self, **kwargs):
        pass
