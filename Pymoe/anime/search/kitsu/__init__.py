from datetime import date
import ujson
import requests
from pymoe.errors import *
from pymoe.helpers import kitsuWrapper, whatSeason
from pymoe.anime.get.kitsu import show

settings = {
    'header': {
        'Content-Type': 'application/vnd.api+json',
        'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)',
        'Accept': 'application/vnd.api+json'
    },
    'apiurl': 'https://kitsu.io/api/edge'
}

def characters(term : str):
    """
        Kitsu doesn't support text filtering on the anime-characters endpoint
        Method not supported
    """
    raise methodNotSupported("pymoe.anime.search.kitsu.characters", "kitsu")

def shows(term: str):
    """
        TODO: Write This
    """
    r = requests.get(
        settings['apiurl'] + "/anime",
        params={
            'filter[text]': term
        },
        headers = settings['header']
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)
    
    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['meta']['count']:
            return kitsuWrapper(
                jsd['data'],
                jsd['links']['next'] if 'next' in jsd['links'] else None,
                settings['header']
            )
        else:
            return jsd

def staff(term : str):
    """
        TODO: Write This
    """
    r = requests.get(
        settings['apiurl'] + "/anime-staff",
        params={
            'filter[text]': term
        },
        headers = settings['header']
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['meta']['count']:
            return kitsuWrapper(
                jsd['data'],
                jsd['links']['next'] if 'next' in jsd['links'] else None,
                settings['header']
            )
        else:
            return jsd

def studios(term : str):
    """
        TODO: Write This
    """
    r = requests.get(
        settings['apiurl'] + "/anime-productions",
        params={
            'filter[text]': term
        },
        headers = settings['header']
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['meta']['count']:
            return kitsuWrapper(
                jsd['data'],
                jsd['links']['next'] if 'next' in jsd['links'] else None,
                settings['header']
            )
        else:
            return jsd

def season(season : str = None, seasonYear : int = date.today().year):
    """
        TODO: Write This
    """
    myseason = season if season else whatSeason(date.today().month)

    r = requests.get(
        settings['apiurl'] + "/anime",
        params = {
            "filter[season]": myseason,
            "filter[seasonYear]": seasonYear
        },
        headers = settings['header']
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['meta']['count']:
            return kitsuWrapper(
                jsd['data'],
                jsd['links']['next'] if 'next' in jsd['links'] else None,
                settings['header']
            )
        else:
            return jsd

def streaming(item_id : int):
    """
        TODO: Write This
    """
    data = show(item_id)

    r = requests.get(
        data['data']['relationships']['streamingLinks']['links']['related'],
        headers = settings['header']
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['meta']['count']:
            return kitsuWrapper(
                jsd['data'],
                jsd['links']['next'] if 'next' in jsd['links'] else None,
                settings['header']
            )
        else:
            return jsd