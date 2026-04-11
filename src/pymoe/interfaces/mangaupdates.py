from typing import Dict
from pymoe.baseclass import BaseAPI

class GetEndpoints:
    def __init__(self, parent):
        self.parent = parent

    def manga(self, series_id: int):
        return self.parent._get(endpoint=f"series/{series_id}")

    def review(self, review_id: int):
        return self.parent._get(endpoint=f"reviews/{review_id}")

    def publisher(self, publisher_id: int):
        return self.parent._get(endpoint=f"publishers/{publisher_id}")

    def group(self, group_id: int):
        return self.parent._get(endpoint=f"groups/{group_id}")

    def author(self, author_id: int):
        return self.parent._get(endpoint=f"authors/{author_id}")

    def manga_release_feed(self, series_id: int):
        return self.parent._get(endpoint=f"series/{series_id}/rss", raw_text=True)

    def releases_feed(self):
        return self.parent._get(endpoint="releases/rss", raw_text=True)

    def manga_by_author(self, author_id: int):
        return self.parent._post(
            endpoint=f"authors/{author_id}/series",
            json={"orderby": "title"}
        )

    def groups_by_manga(self, series_id: int):
        return self.parent._get(endpoint=f"series/{series_id}/groups")

    def genres(self):
        return self.parent._get(endpoint="genres")

class SearchEndpoints:
    def __init__(self, parent):
        self.parent = parent

    def series(self, title: str, options: Dict = None, page: int = 1, per_page: int = 5):
        data = options or {}
        data.update({"search": title, "page": page, "perpage": per_page})
        return self.parent._post(endpoint="series/search", json=data)

    def reviews(self, series_id: int, options: Dict = None, page: int = 1, per_page: int = 5):
        data = options or {}
        data.update({"series_id": str(series_id), "page": page, "perpage": per_page})
        return self.parent._post(endpoint="reviews/search", json=data)

    def publishers(self, title: str, options: Dict = None, page: int = 1, per_page: int = 5):
        data = options or {}
        data.update({"search": title, "page": page, "perpage": per_page})
        return self.parent._post(endpoint="publishers/search", json=data)

    def groups(self, title: str, options: Dict = None, page: int = 1, per_page: int = 5):
        data = options or {}
        data.update({"search": title, "page": page, "perpage": per_page})
        return self.parent._post(endpoint="groups/search", json=data)

    def authors(self, title: str, options: Dict = None, page: int = 1, per_page: int = 5):
        data = options or {}
        data.update({"search": title, "page": page, "perpage": per_page})
        return self.parent._post(endpoint="authors/search", json=data)

    def categories(self, title: str, options: Dict = None, page: int = 1, per_page: int = 5):
        data = options or {}
        data.update({"search": title, "page": page, "perpage": per_page})
        return self.parent._post(endpoint="categories/search", json=data)


class MangaupdatesAPI(BaseAPI):
    def __init__(self, web_client):
        super().__init__(web_client, "https://api.mangaupdates.com/v1")
        self.apiheaders = {
            "Content-Type": "application/json",
            "Accept": "application/json"
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
        if kwargs.get("raw_text", False):
            return response.text
        return response.json()

    def _post(self, **kwargs):
        url = f"{self.base_url}/{kwargs.get('endpoint')}"

        merged = None
        if kwargs.get("headers", False):
            merged = self._merge_headers(kwargs.get("headers")).update(self.apiheaders)
        else:
            merged = self._merge_headers(self.apiheaders)

        response = self.web_client.post(
            url,
            headers = merged,
            json = kwargs.get("json", None)
        )
        return response.json()
