from inspect import currentframe, getargvalues
from typing import Dict, Tuple

import requests
import ujson

from pymoe.utils.errors import serializationFailed, serverError

settings = {
    "apiurl": "https://www.wlnupdates.com/api",
    "header": {
        "User-Agent": "Pymoe (github.com/ccubed/Pymoe)",
        "Content-Type": "application/json",
        "Accept": "application/json",
    },
}


def series(title_text: str):
    """
    Given the title_text to search by, return a list of results.
    This is the best method to find a title by name.

    :param title_text: The title to search for.
    """
    r = requests.post(
        settings["apiurl"],
        headers=settings["header"],
        json={"title": title_text, "mode": "search-title"},
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["error"]:
            raise serverError(jsd["message"], r.status_code)
        else:
            return jsd["data"]


def tags():
    """
    This simply returns a list of all tags along with their IDs.
    These are the tags you can use in Parametric search.
    You can also use these in pymoe.ln.get.wlnupdates.tag
    """
    r = requests.post(
        settings["apiurl"], headers=settings["header"], json={"mode": "enumerate-tags"}
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["error"]:
            raise serverError(jsd["message"], r.status_code)
        else:
            return jsd["data"]


def genres():
    """
    This simply returns a list of all genres along with their IDs.
    These are the genres you can use in Parametric search.
    You can also use these in pymoe.ln.get.wlnupdates.genre
    """
    r = requests.post(
        settings["apiurl"], headers=settings["header"], json={"mode": "enumerate-genres"}
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["error"]:
            raise serverError(jsd["message"], r.status_code)
        else:
            return jsd["data"]


def parametric(
    title_search_text: str = None,
    tag_category=None,
    genre_category: Dict = None,
    chapter_limits: tuple = None,
    series_type: Dict = None,
    sort_mode: str = "name",
    include_results: Dict = None,
):
    """
    Perform a Parametric search. This is the search-advanced route.
    You have to pass at least one of tags or genres. If you don't, this function will refer your search to title search.
    If you don't need to search by tags or genres, title search is a better option per the api documentation.
    The parameters have the same name as the API due to how the query is built.

    :param title-search-text: Optional title to search by
    :param tags: A dictionary consisting of pairs of 'tag' keys and then 'included' or 'excluded'
    :param genres: A dictionary consisting of pairs of 'genre' keys and then 'included' or 'excluded'
    :param chapter_limit: A tuple consisting of (minimum,maximum) to limit by chapter count. Passing 0 disables the limit it was passed for.
    :param series_type: A dictionary consisting of the keys 'Translated' and 'Original English Language' along with Included or Excluded as the value for each.
    :param sort_mode: One of update, chapter-count, or name. Defaults to name.
    :param include_results: A list of strings to represent what additional information to return. Only accepts description, covers, tags, genres.
    """
    if not (tag_category or genre_category):
        if title_search_text:
            return series(title_search_text)
        else:
            raise ValueError(
                "pymoe.ln.search.wlnupdates.parametric: Requires one of tag_category or genre_category."
            )

    json_data = {"mode": "search-advanced"}

    args, _, _, values = getargvalues(currentframe())

    for item in args:
        if values[item]:
            json_data[item.replace("_", "-")] = values[item]

    r = requests.post(settings["apiurl"], headers=settings["header"], json=json_data)

    print(r.text)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["error"]:
            raise serverError(jsd["message"], r.status_code)
        else:
            return jsd["data"]
