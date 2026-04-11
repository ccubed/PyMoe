from typing import Dict
from pymoe.baseclass import BaseAPI

class GetEndpoints:
    def __init__(self, parent):
        self.parent = parent

    def series(self, item_id: int):
        return self.parent._post(json={"id": item_id, "mode": "get-series-id"})

    def artist(self, item_id: int):
        return self.parent._post(json={"id": item_id, "mode": "get-artist-id"})

    def author(self, item_id: int):
        return self.parent._post(json={"id": item_id, "mode": "get-author-id"})

    def genre(self, item_id: int):
        return self.parent._post(json={"id": item_id, "mode": "get-genre-id"})

    def group(self, item_id: int):
        return self.parent._post(json={"id": item_id, "mode": "get-group-id"})

    def publisher(self, item_id: int):
        return self.parent._post(json={"id": item_id, "mode": "get-publisher-id"})

    def tag(self, item_id: int):
        return self.parent._post(json={"id": item_id, "mode": "get-tag-id"})

class SearchEndpoints:
    def __init__(self, parent):
        self.parent = parent

    def series(self, title_text: str):
        return self.parent._post(json={"title": title_text, "mode": "search-title"})

    def tags(self):
        return self.parent._post(json={"mode": "enumerate-tags"})

    def genres(self):
        return self.parent._post(json={"mode": "enumerate-genres"})

    def parametric(self, title_search_text: str = None, tag_category = None, genre_category: Dict = None,
                   chapter_limits: tuple = None, series_type: Dict = None, sort_mode: str = "name",
                   include_results: Dict = None):
        if not (tag_category or genre_category):
            if title_search_text:
                return self.series(title_search_text)
            else:
                raise ValueError("pymoe.interfaces.wlnupdates.parametric: Requires one of tag_category or genre_category.")

        json_data = {"mode": "search-advanced"}
        
        args_dict = {
            "title-search-text": title_search_text,
            "tag-category": tag_category,
            "genre-category": genre_category,
            "chapter-limits": chapter_limits,
            "series-type": series_type,
            "sort-mode": sort_mode,
            "include-results": include_results
        }
        
        for key, value in args_dict.items():
            if value:
                json_data[key] = value

        return self.parent._post(json=json_data)

class WLNUpdatesAPI(BaseAPI):
    def __init__(self, web_client):
        super().__init__(web_client, "https://www.wlnupdates.com/api")
        self.apiheaders = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.get = GetEndpoints(self)
        self.search = SearchEndpoints(self)

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
            json = kwargs.get("json", None)
        )
        return response.json()
