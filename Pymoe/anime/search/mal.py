from datetime import date
import ujson
import requests
from pymoe.utils.errors import methodNotSupported, serializationFailed, serverError
from pymoe.utils.helpers import malWrapper, whatSeason

settings = {
    "header": {
        "Content-Type": "application/json",
        "User-Agent": "Pymoe (github.com/ccubed/PyMoe)",
        "Accept": "application/json",
        "X-MAL-CLIENT-ID": None,
    },
    "apiurl": "https://api.myanimelist.net/v2/",
    "default_fields": "id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,nsfw,genres,media_type,status,num_episodes,start_season,broadcast,source,rating,studios,related_anime,related_manga",
}


def keyAssert():
    """
    This is just an assert. It cancels the request if the API Key is not present.
    """
    if (
        not settings["header"]["X-MAL-CLIENT-ID"]
        or type(settings["header"]["X-MAL-CLIENT-ID"]) != str
    ):
        raise ValueError("pymoe.anime.search.mal.keyAssert: API Key should be a string.")
    else:
        pass


def characters(term: str):
    """
    No endpoint exists for this at this time.
    Method not supported
    """
    raise methodNotSupported("pymoe.anime.search.mal.characters", "myanimelist")


def shows(
    term: str,
    fields: str | None = None,
    limit: int = 10,
    offset: int = 0,
    nsfw: bool = False,
):
    """
    Search for shows that match the given search term.

    :param term: Search Term
    :param fields: a comma separated list of fields to request from the API
    :param limit: How many results per page?
    :param offset: Which result should we start at?
    :param nsfw: Return adult results?
    """
    keyAssert()

    r = requests.get(
        settings["apiurl"] + "anime",
        params={
            "q": term,
            "fields": settings["default_fields"] or fields,
            "limit": limit,
            "offset": offset,
            "nsfw": "false" if not nsfw else "true",
        },
        headers=settings["header"],
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)

    rdict = [item["node"] for item in jsd["data"]]
    r_url = jsd["paging"]["next"] if "next" in jsd["paging"] else None

    return malWrapper(rdict, r_url, settings["header"])


def staff(term: str):
    """
    No endpoint exists for this at this time.
    Method not supported
    """
    raise methodNotSupported("pymoe.anime.search.mal.staff", "myanimelist")


def studios(term: str):
    """
    No endpoint exists for this at this time.
    Method not supported
    """
    raise methodNotSupported("pymoe.anime.search.mal.studios", "myanimelist")


def season(
    season: str = None,
    seasonYear: int = date.today().year,
    limit: int = 10,
    offset: int = 0,
    nsfw: bool = False,
):
    """
    Search for shows from a given season in a given year.

    :param season: Which season? See pymoe.helpers for a list.
    :param seasonYear: Which year?
    :param limit: How many results per page?
    :param offset: Which result do we start at?
    :param nsfw: Return adult results?
    """
    keyAssert()

    myseason = season or whatSeason(date.today().month)

    r = requests.get(
        settings["apiurl"] + "anime/season/{}/{}".format(seasonYear, myseason),
        params={
            "sort": "anime_score",
            "limit": limit,
            "offset": offset,
            "fields": "id,title,main_picture,alternative_titles,start_date,broadcast",
            "nsfw": "false" if not nsfw else "true",
        },
        headers=settings["header"],
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)

    rdict = [item["node"] for item in jsd["data"]]
    r_url = jsd["paging"]["next"] if "next" in jsd["paging"] else None

    return malWrapper(rdict, r_url, settings["header"])
