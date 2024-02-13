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


def series(seriesId: int):
    """
    Get a specific series by series ID.

    :param seriesId: The Series ID to get data for.
    """
    r = requests.get(
        settings["apiurl"] + "series/{}".format(seriesId), headers=settings["header"]
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd


def review(reviewId: int):
    """
    Get a specific review by ID

    :param reviewId: The Review ID to get data for.
    """
    r = requests.get(
        settings["apiurl"] + "reviews/{}".format(reviewId), headers=settings["header"]
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd


def publisher(publisherId: int):
    """
    Get a specific publisher by ID

    :param publisherId: The Publisher ID to get data for.
    """
    r = requests.get(
        settings["apiurl"] + "publishers/{}".format(publisherId),
        headers=settings["header"],
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd


def group(groupId: int):
    """
    Get a specific group by ID

    :param groupId: The group ID to get data for.
    """
    r = requests.get(
        settings["apiurl"] + "groups/{}".format(groupId), headers=settings["header"]
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd


def author(authorId: int):
    """
    Get a specific author by ID

    :param authorId: The author ID to get data for.
    """
    r = requests.get(
        settings["apiurl"] + "authors/{}".format(authorId), headers=settings["header"]
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd


def seriesReleaseFeed(seriesId: int):
    """
    Get an RSS Feed of Releases for a specific series

    :param seriesId: The Series ID to get a feed for
    """
    r = requests.get(
        settings["apiurl"] + "series/{}/rss".format(seriesId), headers=settings["header"]
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    # This is simply XML data.
    return r.text


def releasesFeed():
    """
    Get an RSS Feed of Releases for the entire site
    """
    r = requests.get(settings["apiurl"] + "releases/rss", headers=settings["header"])

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    # This is simply XML data.
    return r.text


def seriesByAuthor(authorId: int):
    """
    Get a list of series an author has worked on

    :param authorId: The author ID to get data for.
    """
    r = requests.post(
        settings["apiurl"] + "authors/{}/series".format(authorId),
        headers=settings["header"],
        json={"orderby": "title"},
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd


def groupsBySeries(seriesId: int):
    """
    Get a list of groups that have worked on a series

    :param seriesId: The Series to find groups for
    """
    r = requests.get(
        settings["apiurl"] + "series/{}/groups".format(seriesId),
        headers=settings["header"],
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd


def genres():
    """
    Get a list of all genres.
    Note that this literally returns all genres as a list of dictionaries.
    """
    r = requests.get(settings["apiurl"] + "genres", headers=settings["header"])

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd
