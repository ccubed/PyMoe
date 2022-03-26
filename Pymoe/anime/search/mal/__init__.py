from datetime import date
import ujson
import requests
from pymoe.errors import *
from pymoe.helpers import *

settings = {
    'header': {
        'Content-Type': 'application/json',
        'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)',
        'Accept': 'application/json',
        'X-MAL-CLIENT-ID': None
    },
    'apiurl': 'https://api.myanimelist.net/v2/',
    'default_fields': 'id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,nsfw,genres,media_type,status,num_episodes,start_season,broadcast,source,rating,studios,related_anime,related_manga'
}

def setKey(apikey : str):
    """
        TODO: Write This
    """
    settings['header']['X-MAL-CLIENT-ID'] = apikey

def keyAssert():
    """
        TODO: Write This
    """
    if not settings['header']['X-MAL-CLIENT-ID'] or type(settings['header']['X-MAL-CLIENT-ID']) != str:
        raise ValueError("API Key should be a string.")
    else:
        pass

def characters(term : str):
    """
        TODO: Write This
    """
    raise MethodNotSupported("pymoe.anime.search.mal.characters", "myanimelist")

def shows(term: str, fields : str = None, limit : int = 10, offset : int = 0, nsfw : bool = False):
    """
        TODO: Write This
    """
    r = requests.get(
        settings['apiurl'] + "anime",
        params={
            'q': term,
            'fields': settings['default_fields'] or fields,
            'limit': limit,
            'offset': offset,
            'nsfw': 'false' if not nsfw else 'true'
        }
    )

    if r.status_code != 200:
        raise ServerError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise SerializationFailed(r.text, r.status_code)

    rdict = {item['node']['title'] : item['node'] for item in jsd['data']}
    rdict['paging'] = {
        'previous': (offset - 10) if offset > 0 else None,
        'next': (offset + 10) if 'next' in jsd['paging'] else None
    }

    return rdict

def staff(term : str):
    """
        TODO: Write This
    """
    raise MethodNotSupported("pymoe.anime.search.mal.staff", "myanimelist")

def studios(term : str):
    """
        TODO: Write This
    """
    raise MethodNotSupported("pymoe.anime.search.mal.studios", "myanimelist")