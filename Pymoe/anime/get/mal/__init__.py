from datetime import date
import ujson
import requests
from pymoe.errors import methodNotSupported, serverError

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

def keyAssert():
    """
        This is just an assert. It cancels the request if the API Key is not present.
    """
    if not settings['header']['X-MAL-CLIENT-ID'] or type(settings['header']['X-MAL-CLIENT-ID']) != str:
        raise ValueError("pymoe.anime.get.mal.keyAssert: API Key should be a string.")
    else:
        pass

def character(item_id : int):
    """
        No endpoint exists for this at this time
        Method not supported
    """
    raise methodNotSupported("pymoe.anime.get.mal.character", "myanimelist")

def show(item_id : int, fields : str = None):
    """
        Get a show with the specific ID from the myanimelist api.

        :param item_id: ID of the show you want info on.
    """
    keyAssert()

    r = requests.get(
        settings['apiurl'] + "anime/{}".format(item_id),
        params={
            'fields': fields or settings['default_fields'],
            'nsfw': 'true' 
        },
        headers = settings['header']
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)

    return ujson.loads(r.text)

def episode(item_id : int):
    """
        No endpoint exists for this at this time
        Method not supported
    """
    raise methodNotSupported("pymoe.anime.get.mal.episode", "myanimelist")

def streaming(item_id : int):
    """
        No endpoint exists for this at this time
        Method not supported
    """
    raise methodNotSupported("pymoe.anime.get.mal.streaming", "myanimelist")

def staff(item_id : int):
    """
        No endpoint exists for this at this time
        Method not supported
    """
    raise methodNotSupported("pymoe.anime.get.mal.staff", "myanimelist")

def studio(item_id : int):
    """
        No endpoint exists for this at this time
        Method not supported
    """
    raise methodNotSupported("pymoe.anime.get.mal.studio", "myanimelist")