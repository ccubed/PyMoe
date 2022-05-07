from datetime import date
from typing import Dict
import ujson
import requests
from pymoe.errors import serializationFailed, serverError
from pymoe.helpers import anilistWrapper

settings = {
    'header': {
        'Content-Type': 'application/json',
        'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)',
        'Accept': 'application/json'
    },
    'apiurl': 'https://graphql.anilist.co'
}

def characters(term : str, page : int = 1, perPage : int = 3):
    """
        Search for characters that match the term in the API.

        :param term: Search Term
        :param page: Which page of the results?
        :param perPage: How many results per page?
    """
    query_string = """\
        query ($query: String, $page: Int, $perPage: Int){
            Page (page: $page, perPage: $perPage) {
                pageInfo {
                    currentPage
                    hasNextPage
                }
                characters (search: $query) {
                    id
                    name{
                        first
                        last
                    }
                    image{
                        large
                    }
                    description
                    gender
                    age
                    siteUrl
                    media {
                        nodes {
                            id
                            idMal
                            title {
                                romaji
                                english
                                native
                            }
                            coverImage {
                                extraLarge
                                large
                                medium
                                color
                            }
                            siteUrl
                        }
                    }
                }
            }
        }
    """

    json_params = {
        'query': query_string,
        'variables': {
            'query': term,
            'page': page,
            'perPage': perPage
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
            if jsd['data']['Page']['pageInfo']['hasNextPage']:
                return anilistWrapper(
                    jsd['data']['Page']['characters'],
                    json_params,
                    settings['header'],
                    settings['apiurl']
                )
            else:
                return jsd['data']['Page']['characters']

def shows(term : str, page : int = 1, perPage : int = 3):
    """
        Search for shows(anime) that match the term in the API.

        :param term: Search Term
        :param page: Which page of the results?
        :param perPage: How many results per page?
    """
    query_string = """\
        query ($query: String, $page: Int, $perPage: Int){
            Page (page: $page, perPage: $perPage){
                pageInfo {
                    currentPage
                    hasNextPage
                }
                media (search: $query, type: ANIME) {
                    id
                    idMal
                    title {
                        romaji
                        english
                        native
                    }
                    coverImage {
                        extraLarge
                        large
                        medium
                        color
                    }
                    averageScore
                    popularity
                    episodes
                    season
                    hashtag
                    isAdult
                    siteUrl
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
        }
    """

    json_params = {
        'query': query_string,
        'variables': {
            'query': term,
            'page': page,
            'perPage': perPage
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
            if jsd['data']['Page']['pageInfo']['hasNextPage']:
                return anilistWrapper(
                    jsd['data']['Page']['media'],
                    json_params,
                    settings['header'],
                    settings['apiurl']
                )
            else:
                return jsd['data']['Page']['media']

def staff(term: str, page : int = 1, perPage : int = 3):
    """
        Search for staffers that match the term in the API.

        :param term: Search Term
        :param page: Which page of the results?
        :param perPage: How many results per page?
    """
    query_string = """\
        query($query: String, $page: Int, $perPage: Int){
            Page(page: $page, perPage: $perPage){
                pageInfo{
                    currentPage
                    hasNextPage
                }
                staff (search: $query){
                    name {
                        first
                        last
                    }
                    languageV2
                    image {
                        large
                        medium
                    }
                    description
                    primaryOccupations
                    gender
                    dateOfBirth {
                        year
                        month
                        day
                    }
                    dateOfDeath {
                        year
                        month
                        day
                    }
                    age
                    homeTown
                    yearsActive
                    siteUrl
                    staffMedia {
                        nodes {
                            id
                            idMal
                            title {
                                romaji
                                english
                                native
                            }
                            coverImage {
                                extraLarge
                                large
                                medium
                                color
                            }
                            siteUrl
                        }
                    }
                    characters {
                        nodes {
                            name {
                                first
                                last
                            }
                            image {
                                large
                                medium
                            }
                            age
                            siteUrl
                            media {
                                nodes {
                                    id
                                    idMal
                                    title {
                                        romaji
                                        english
                                        native
                                    }
                                    coverImage {
                                        extraLarge
                                        large
                                        medium
                                        color
                                    }
                                    siteUrl
                                }
                            }
                        }
                    }
                }
            }
        }
    """

    json_params = {
        'query': query_string,
        'variables': {
            'query': term,
            'page': page,
            'perPage': perPage
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
            if jsd['data']['Page']['pageInfo']['hasNextPage']:
                return anilistWrapper(
                    jsd['data']['Page']['staff'],
                    json_params,
                    settings['header'],
                    settings['apiurl']
                )
            else:
                return jsd['data']['Page']['staff']

def studios(term : str, page : int = 1, perPage : int = 3):
    """
        Search for studios that match the term in the API.

        :param term: Search Term
        :param page: Which page of the results?
        :param perPage: How many results per page?
    """
    query_string = """\
        query($query: String, $page: Int, $perPage: Int){
            Page(page: $page, perPage: $perPage){
                pageInfo{
                    currentPage
                    hasNextPage
                }
                studios(search: $query){
                    id
                    name
                    siteUrl
                    media {
                        nodes {
                            id
                            idMal
                            title {
                                romaji
                                english
                                native
                            }
                            coverImage {
                                extraLarge
                                large
                                medium
                                color
                            }
                            siteUrl
                        }
                    }
                }
            }
        }
    """

    json_params = {
        'query': query_string,
        'variables': {
            'query': term,
            'page': page,
            'perPage': perPage
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
            if jsd['data']['Page']['pageInfo']['hasNextPage']:
                return anilistWrapper(
                    jsd['data']['Page']['studios'],
                    json_params,
                    settings['header'],
                    settings['apiurl']
                )
            else:
                return jsd['data']['Page']['studios']

def airingSchedule(item_id: int, notYetAired: bool = False):
    """
        Given an anime id, return the airing schedule.
        This returns a full airing schedule, including already aired episodes.
        If an episode has already aired timeUntilAiring will be <= 0.
        timeUntilAiring is just seconds.
    """
    query_string = """\
        query( $id: Int, $page: Int, $perPage: Int ) {
            Page ( page: $page, perPage: $perPage ) {
                pageInfo {
                    currentPage
                    hasNextPage
                }
                airingSchedules ( mediaId: $id ) {
                    id
                    episode
                    timeUntilAiring
                }
            }
        }
    """

    json_params = {
        'query': query_string,
        'variables': {
            'id': item_id,
            'page': 1,
            'perPage': 3
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
            if jsd['data']['Page']['pageInfo']['hasNextPage']:
                return anilistWrapper(
                    jsd['data']['Page']['airingSchedules'],
                    json_params,
                    settings['header'],
                    settings['apiurl']
                )
            else:
                return jsd['data']['Page']['airingSchedules']