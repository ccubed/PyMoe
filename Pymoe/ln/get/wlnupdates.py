import requests
import ujson
from pymoe.utils.errors import serializationFailed, serverError

settings = {
    'apiurl': "https://www.wlnupdates.com/api",
    'header': {
        'User-Agent': 'Pymoe (github.com/ccubed/Pymoe)',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
}

def series(item_id : int):
    """
        Given an item_id, get information about the series with that item_id.

        :param item_id: The ID of the Series we want
    """
    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json = {
            'id': item_id,
            'mode': 'get-series-id'
        }
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['error']:
            raise serverError(jsd['message'], r.status_code)
        else:
            return jsd['data']
        
def artist(item_id : int):
    """
        Given an item_id, get information about the artist with that item_id.

        :param item_id: The ID of the Artist we want
    """
    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json = {
            'id': item_id,
            'mode': 'get-artist-id'
        }
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['error']:
            raise serverError(jsd['message'], r.status_code)
        else:
            return jsd['data']
        
def author(item_id : int):
    """
        Given an item_id, get information about the author with that item_id.

        :param item_id: The ID of the Author we want
    """
    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json = {
            'id': item_id,
            'mode': 'get-author-id'
        }
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['error']:
            raise serverError(jsd['message'], r.status_code)
        else:
            return jsd['data']
        
def genre(item_id : int):
    """
        Given an item_id, get information about the genre with that item_id.
        This actually returns all series with that genre along with the genre itself.

        :param item_id: The ID of the Genre we want
    """
    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json = {
            'id': item_id,
            'mode': 'get-genre-id'
        }
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['error']:
            raise serverError(jsd['message'], r.status_code)
        else:
            return jsd['data']
        
def group(item_id : int):
    """
        Given an item_id, get information about the group with that item_id.
        This appears to be scanlators/translators.

        :param item_id: The ID of the Group we want
    """
    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json = {
            'id': item_id,
            'mode': 'get-group-id'
        }
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['error']:
            raise serverError(jsd['message'], r.status_code)
        else:
            return jsd['data']
        
def publisher(item_id : int):
    """
        Given an item_id, get information about the publisher with that item_id.

        :param item_id: The ID of the Publisher we want
    """
    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json = {
            'id': item_id,
            'mode': 'get-publisher-id'
        }
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['error']:
            raise serverError(jsd['message'], r.status_code)
        else:
            return jsd['data']
        
def tag(item_id : int):
    """
        Given an item_id, get information about the tag with that item_id.
        This actually returns all series with that tag along with the tag itself.

        :param item_id: The ID of the Artist we want
    """
    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json = {
            'id': item_id,
            'mode': 'get-tag-id'
        }
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['error']:
            raise serverError(jsd['message'], r.status_code)
        else:
            return jsd['data']
        
    