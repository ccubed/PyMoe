from typing import Dict
import requests
import ujson
from pymoe.utils.errors import serializationFailed, serverError
from pymoe.utils.helpers import mangaupdatesWrapper

settings = {
    "header": {
        "Content-Type": "application/json",
        "User-Agent": "Pymoe (github.com/ccubed/PyMoe)",
        "Accept": "application/json",
    },
    "apiurl": "https://api.mangaupdates.com/v1/",
}


def series(title: str, options: Dict = None, page: int = 1, perPage: int = 5):
    """
    Search for a series with title on Mangaupdates.
    Options is an optional dictionary containing additional search options to pass.

    :param title: The title to search for
    :param options: An optional dictionary of additional search criteria
    :param page: Which page of results
    :param perPage: Results per page. Note that the only acceptable values are 5,10,15,25,30,40,50,75,100
    """
    thisData = None
    if options:
        thisData = options
        thisData["search"] = title
        thisData["page"] = page
        thisData["perPage"] = perPage
    else:
        thisData = {"search": title, "page": page, "perPage": perPage}

    r = requests.post(
        settings["apiurl"] + "series/search", headers=settings["header"], json=thisData
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["total_hits"] > jsd["per_page"]:
            return mangaupdatesWrapper(
                jsd["results"],
                settings["apiurl"] + "series/search",
                settings["header"],
                thisData,
                round(jsd["total_hits"] / jsd["per_page"], 0),
            )
        else:
            return jsd["results"]


def releases(seriesId: int, options: Dict = None, page: int = 1, perPage: int = 5):
    """
    Search for releases for a specific series ID.
    Options is an optional dictionary containing additional search options to pass.

    :param seriesId: The Series ID to find releases for
    :param options: An optional dictionary of additional search criteria
    :param page: Which page of results
    :param perPage: Results per page. Note that the only acceptable values are 5,10,15,25,30,40,50,75,100
    """
    thisData = None
    if options:
        thisData = options
        thisData["search"] = str(seriesId)
        thisData["search_type"] = "series"
        thisData["page"] = page
        thisData["perPage"] = perPage
    else:
        thisData = {
            "search": str(seriesId),
            "search_type": "series",
            "page": page,
            "perPage": perPage,
        }

    r = requests.post(
        settings["apiurl"] + "releases/search", headers=settings["header"], json=thisData
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["total_hits"] > jsd["per_page"]:
            return mangaupdatesWrapper(
                jsd["results"],
                settings["apiurl"] + "series/search",
                settings["header"],
                thisData,
                round(jsd["total_hits"] / jsd["per_page"], 0),
            )
        else:
            return jsd["results"]


def reviews(seriesId: int, options: Dict = None, page: int = 1, perPage: int = 5):
    """
    Search for reviews for a given series ID.
    Options is an optional dictionary containing additional search options to pass.

    :param seriesId: The ID of the series to get reviews for
    :param options: An optional dictionary of additional search criteria
    :param page: Which page of results
    :param perPage: Results per page. Note that the only acceptable values are 5,10,15,25,30,40,50,75,100
    """
    thisData = None
    if options:
        thisData = options
        thisData["series_id"] = str(seriesId)
        thisData["page"] = page
        thisData["perPage"] = perPage
    else:
        thisData = {"series_id": str(seriesId), "page": page, "perPage": perPage}

    r = requests.post(
        settings["apiurl"] + "reviews/search", headers=settings["header"], json=thisData
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["total_hits"] > jsd["per_page"]:
            return mangaupdatesWrapper(
                jsd["results"],
                settings["apiurl"] + "series/search",
                settings["header"],
                thisData,
                round(jsd["total_hits"] / jsd["per_page"], 0),
            )
        else:
            return jsd["results"]


def publishers(title: str, options: Dict = None, page: int = 1, perPage: int = 5):
    """
    Search for Publishers that match the title.
    Options is an optional dictionary containing additional search options to pass.

    :param title: The name of the publisher to find
    :param options: An optional dictionary of additional search criteria
    :param page: Which page of results
    :param perPage: Results per page. Note that the only acceptable values are 5,10,15,25,30,40,50,75,100
    """
    thisData = None
    if options:
        thisData = options
        thisData["search"] = title
        thisData["page"] = page
        thisData["perPage"] = perPage
    else:
        thisData = {"search": title, "page": page, "perPage": perPage}

    r = requests.post(
        settings["apiurl"] + "publishers/search",
        headers=settings["header"],
        json=thisData,
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["total_hits"] > jsd["per_page"]:
            return mangaupdatesWrapper(
                jsd["results"],
                settings["apiurl"] + "series/search",
                settings["header"],
                thisData,
                round(jsd["total_hits"] / jsd["per_page"], 0),
            )
        else:
            return jsd["results"]


def groups(title: str, options: Dict = None, page: int = 1, perPage: int = 5):
    """
    Search for Groups that match the title.
    Groups are scanlators, uploaders, raw providers, etc.
    Options is an optional dictionary containing additional search options to pass.

    :param title: The name of the group to find
    :param options: An optional dictionary of additional search criteria
    :param page: Which page of results
    :param perPage: Results per page. Note that the only acceptable values are 5,10,15,25,30,40,50,75,100
    """
    thisData = None
    if options:
        thisData = options
        thisData["search"] = title
        thisData["page"] = page
        thisData["perPage"] = perPage
    else:
        thisData = {"search": title, "page": page, "perPage": perPage}

    r = requests.post(
        settings["apiurl"] + "groups/search", headers=settings["header"], json=thisData
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["total_hits"] > jsd["per_page"]:
            return mangaupdatesWrapper(
                jsd["results"],
                settings["apiurl"] + "series/search",
                settings["header"],
                thisData,
                round(jsd["total_hits"] / jsd["per_page"], 0),
            )
        else:
            return jsd["results"]


def authors(title: str, options: Dict = None, page: int = 1, perPage: int = 5):
    """
    Search for Authors that match the title.
    Options is an optional dictionary containing additional search options to pass.

    :param title: The name of the Author to find
    :param options: An optional dictionary of additional search criteria
    :param page: Which page of results
    :param perPage: Results per page. Note that the only acceptable values are 5,10,15,25,30,40,50,75,100
    """
    thisData = None
    if options:
        thisData = options
        thisData["search"] = title
        thisData["page"] = page
        thisData["perPage"] = perPage
    else:
        thisData = {"search": title, "page": page, "perPage": perPage}

    r = requests.post(
        settings["apiurl"] + "authors/search", headers=settings["header"], json=thisData
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["total_hits"] > jsd["per_page"]:
            return mangaupdatesWrapper(
                jsd["results"],
                settings["apiurl"] + "series/search",
                settings["header"],
                thisData,
                round(jsd["total_hits"] / jsd["per_page"], 0),
            )
        else:
            return jsd["results"]


def categories(title: str, options: Dict = None, page: int = 1, perPage: int = 5):
    """
    Search for Categories that match the title.
    Options is an optional dictionary containing additional search options to pass.

    :param title: The name of the Author to find
    :param options: An optional dictionary of additional search criteria
    :param page: Which page of results
    :param perPage: Results per page. Note that the only acceptable values are 5,10,15,25,30,40,50,75,100
    """
    thisData = None
    if options:
        thisData = options
        thisData["search"] = title
        thisData["page"] = page
        thisData["perpage"] = perPage
    else:
        thisData = {"search": title, "page": page, "perPage": perPage}

    r = requests.post(
        settings["apiurl"] + "categories/search",
        headers=settings["header"],
        json=thisData,
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["total_hits"] > jsd["per_page"]:
            return mangaupdatesWrapper(
                jsd["results"],
                settings["apiurl"] + "series/search",
                settings["header"],
                thisData,
                round(jsd["total_hits"] / jsd["per_page"], 0),
            )
        else:
            return jsd["results"]
