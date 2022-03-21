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

def character(item_id : int):
    """
        TODO: Write This
    """
    raise MethodNotSupported("pymoe.anime.get.mal.character", "myanimelist")

def show(item_id : int, fields : str = None):
    """
        TODO: Write This
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
        raise ServerError(r.text, r.status_code)

    return ujson.loads(r.text)

def season(season : str = None, seasonYear : int = date.today().year, offset : int = 0, nsfw = None):
    """
        TODO: Write This
    """
    myseason = season or whatSeason(date.today().month)

    r = requests.get(
        settings['apiurl'] + "anime/season/{}/{}".format(seasonYear, myseason),
        params = {
            'sort': 'anime_score',
            'limit': 10,
            'offset': offset,
            'fields': 'id,title,main_picture,alternative_titles,start_date,broadcast'
        },
        headers = settings['header']
    )

    if r.status_code != 200:
        raise ServerError(r.text, r.status_code)

    jsd = ujson.loads(r.text)

    rdict = {item['node']['title'] : item['node'] for item in jsd['data']}
    rdict['paging'] = {
        'previous': (offset - 10) if offset > 0 else None,
        'next': (offset + 10) if 'next' in jsd['paging'] else None
    }

    return rdict

def episode(item_id : int):
    """
        TODO: Write This
    """
    raise MethodNotSupported("pymoe.anime.get.mal.episode", "myanimelist")

def streaming(item_id : int):
    """
        TODO: Write This
    """
    raise MethodNotSupported("pymoe.anime.get.mal.streaming", "myanimelist")

def staff(item_id : int):
    """
        TODO: Write This
    """
    raise MethodNotSupported("pymoe.anime.get.mal.staff", "myanimelist")

def studio(item_id : int):
    """
        TODO: Write This
    """
    raise MethodNotSupported("pymoe.anime.get.mal.studio", "myanimelist")