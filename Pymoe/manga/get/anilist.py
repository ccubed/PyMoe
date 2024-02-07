import requests
import ujson
from pymoe.utils.errors import serializationFailed, serverError
from pymoe.anime.get.anilist import character as cref
from pymoe.anime.get.anilist import staff as sref

settings = {
    'header': {
        'Content-Type': 'application/json',
        'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)',
        'Accept': 'application/json'
    },
    'apiurl': 'https://graphql.anilist.co'
}

def manga(item_id: int):
    """
        The function to retrieve a manga's details.
        I really couldn't think of another name for this.
    """
    query_string = """\
        query( $id: Int ) {
            Media( id: $id, type: MANGA ) {
                idMal
                title {
                    romaji
                    english
                }
                status
                description
                startDate {
                    year
                    month
                    day
                }
                endDate {
                    year
                    month
                    day
                }
                coverImage {
                    extraLarge
                    large
                    medium
                    color
                }
                chapters
                volumes
                genres
                synonyms
                averageScore
                isAdult
                siteUrl
                popularity
                characters {
                    nodes {
                        id
                        name {
                            first
                            last
                        }
                        image {
                            large
                            medium
                        }
                        description
                        gender
                        age
                        siteUrl
                    }
                }
            }
        }        
    """

    json_params = {
        'query': query_string,
        'variables': {
            'id': item_id
        }
    }

    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json = json_params
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        if 'errors' in jsd:
            raise serverError(r.text, r.status_code)
        else:
            return jsd

def character(item_id: int):
    """
        Anilist does not separate characters by anime/manga. 
        This is simply a reference to the character function that already exists.
    """
    return cref(item_id)

def staff(item_id: int):
    """
        Anilist does not separate staff by anime/manga. 
        This is simply a reference to the staff function that already exists.
    """
    return sref(item_id)