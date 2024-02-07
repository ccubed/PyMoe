from typing import Dict
import requests
import ujson
from pymoe.utils.errors import serializationFailed, serverError
from pymoe.utils.helpers import mangaupdatesWrapper

settings = {
    'header': {
        'Content-Type': 'application/json',
        'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)',
        'Accept': 'application/json'
    },
    'apiurl': 'https://api.mangaupdates.com/v1/'
}

def series(title : str, options : Dict = None, page : int = 1, perPage : int = 5):
    """
        Search for a series with title on Mangaupdates.
        Options is an optional dictionary containing additional search optiosn to pass.

        :param title: The title to search for
        :param options: An optional dictionary of additional search criteria
        :param page: Which page of results
        :param perPage: Results per page. Note that the only acceptable values are 5,10,15,25,30,40,50,75,100
    """
    thisData = None
    if options:
        thisData = options
        thisData['search'] = title
        thisData['page'] = page
        thisData['perPage'] = perPage
    else:
        thisData = {'search': title, 'page': page, 'perPage': perPage}

    r = requests.post(
        settings['apiurl']+"series/search",
        headers = settings['header'],
        data = thisData
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)
    
    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if jsd['total_hits'] > jsd['perPage']:
            return mangaupdatesWrapper(
                jsd['results'],
                settings['apiurl']+"series/search",
                settings['header'],
                thisData,
                round(jsd['total_hits']/jsd['perPage'],0)
            )
        else:
            return jsd['results']
        
def releases():
    pass

def reviews():
    pass

def publishers():
    pass

def groups():
    pass

def authors():
    pass