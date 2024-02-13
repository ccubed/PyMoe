from datetime import date
import ujson
import requests
from pymoe.utils.errors import methodNotSupported, serverError, serializationFailed
from pymoe.utils.helpers import kitsuWrapper, whatSeason
from pymoe.anime.get.kitsu import show

settings = {
    "header": {
        "Content-Type": "application/vnd.api+json",
        "User-Agent": "Pymoe (github.com/ccubed/PyMoe)",
        "Accept": "application/vnd.api+json",
    },
    "apiurl": "https://kitsu.io/api/edge",
}


def characters(term: str):
    """
    Search for characters that match the term in the Kitsu API.

    :param term: Search Term
    """
    r = requests.get(
        settings["apiurl"] + "/characters",
        params={"filter[name]": term},
        headers=settings["header"],
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["meta"]["count"]:
            return kitsuWrapper(
                jsd["data"],
                jsd["links"]["next"] if "next" in jsd["links"] else None,
                settings["header"],
            )
        else:
            return jsd


def shows(term: str):
    """
    Search for shows that match the term in the Kitsu API.

    :param term: Search Term
    """
    r = requests.get(
        settings["apiurl"] + "/anime",
        params={"filter[text]": term},
        headers=settings["header"],
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["meta"]["count"]:
            return kitsuWrapper(
                jsd["data"],
                jsd["links"]["next"] if "next" in jsd["links"] else None,
                settings["header"],
            )
        else:
            return jsd


def staff(term: str):
    """
    Kitsu doesn't support text filtering on the anime-staff endpoint.
    Method not supported.
    """
    raise methodNotSupported("pymoe.anime.search.kitsu.staff", "kitsu")


def studios(term: str):
    """
    Kitsu doesn't support text filtering on the anime-producers endpoint.
    Method not supported.
    """
    raise methodNotSupported("pymoe.anime.search.kitsu.studios", "kitsu")


def season(season: str = None, seasonYear: int = date.today().year):
    """
    Given a season and a year, return a list of shows airing in that season and year.
    This can also pull historical and future data. (Though not too far in the future)

    :param season: Which Season? See pymoe.helpers for a list of seasons.
    :param seasonYear: What year?
    """
    myseason = season if season else whatSeason(date.today().month)

    r = requests.get(
        settings["apiurl"] + "/anime",
        params={"filter[season]": myseason, "filter[seasonYear]": seasonYear},
        headers=settings["header"],
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["meta"]["count"]:
            return kitsuWrapper(
                jsd["data"],
                jsd["links"]["next"] if "next" in jsd["links"] else None,
                settings["header"],
            )
        else:
            return jsd


def streaming(item_id: int):
    """
    Given a media ID, return all streaming links related to that media.
    Unlike anilist, this returns one link per streaming service.

    :param term: Search Term
    """
    data = show(item_id)

    r = requests.get(
        data["data"]["relationships"]["streamingLinks"]["links"]["related"],
        headers=settings["header"],
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd["meta"]["count"]:
            return kitsuWrapper(
                jsd["data"],
                jsd["links"]["next"] if "next" in jsd["links"] else None,
                settings["header"],
            )
        else:
            return jsd
