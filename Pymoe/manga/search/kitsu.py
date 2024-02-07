import ujson
import requests
from pymoe.utils.errors import serverError, serializationFailed
from pymoe.utils.helpers import kitsuWrapper

settings = {
    'header': {
        'Content-Type': 'application/vnd.api+json',
        'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)',
        'Accept': 'application/vnd.api+json'
    },
    'apiurl': 'https://kitsu.io/api/edge'
}

def manga(term: str):
    """
        Search for manga that match the search term in the Kitsu API.
    
        :param term: Search Term
    """
    r = requests.get(
        settings['apiurl'] + "/manga",
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