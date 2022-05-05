from datetime import date
import ujson
import requests
from pymoe.errors import serverError, serializationFailed

settings = {
    'header': {
        'Content-Type': 'application/vnd.api+json',
        'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)',
        'Accept': 'application/vnd.api+json'
    },
    'apiurl': 'https://kitsu.io/api/edge'
}

def character(item_id : int):
    """
        TODO: Write This
        ALSO TODO: REWRITE THIS TO USE CHARACTERS ENDPOINT
        ALSO TODO: WRITE NEW FUNCTIONS FOR GETTING ON ANIME-CHARACTERS ENDPOINT
    """
    r = requests.get(
        settings['apiurl'] + "/anime-characters/{}/character".format(item_id),
        headers = settings['header']
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd

def show(item_id : int):
    """
        TODO: Write This
    """
    r = requests.get(
        settings['apiurl'] + "/anime/{}".format(item_id),
        headers = settings['header']
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd 

def episode(item_id : int):
    """
        TODO: Write This
    """
    r = requests.get(
        settings['apiurl'] + "/episodes/{}".format(item_id),
        headers = settings['header']
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd
    
def staff(item_id : int):
    """
        TODO: Write This
    """
    r = requests.get(
        settings['apiurl'] + "/anime-staff/{}/person".format(item_id),
        headers = settings['header']
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd

def studio(item_id : int):
    """
        TODO: Write This
    """
    r = requests.get(
        settings['apiurl'] + "/anime-productions/{}/producer".format(item_id),
        headers = settings['header']
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd
