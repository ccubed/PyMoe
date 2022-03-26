from datetime import date
import ujson
import requests
from pymoe.errors import *
from pymoe.helpers import *

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
        TODO: Write This
    """
    r = requests.get(
        settings['apiurl'] + "/anime-characters",
        params={
            'filter[text]': term
        },
        headers = settings['header']
    )

    if r.status_code != 200:
        raise ServerError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise SerializationFailed(r.text, r.status_code)
    else:
        return jsd

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
        raise ServerError(r.text, r.status_code)
    
    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise SerializationFailed(r.text, r.status_code)
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
        raise ServerError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise SerializationFailed(r.text, r.status_code)
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
        raise ServerError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise SerializationFailed(r.text, r.status_code)
    else:
        return jsd