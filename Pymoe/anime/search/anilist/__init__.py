from datetime import date
from typing import Dict
import ujson
import requests
from pymoe.errors import *
from pymoe.helpers import *

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
        TODO: Write This
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

    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json={
            'query': query_string,
            'variables': {
                'query': term,
                'page': page,
                'perPage': perPage
            }
        }
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

def shows(term : str, page : int = 1, perPage : int = 3):
    """
        TODO: Write This
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
                return searchWrapper
            else:
                return jsd['data']['Page']['media']

def staff(term: str, page : int = 1, perPage : int = 3):
    """
        TODO: Write This
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

    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json={
            'query': query_string,
            'variables': {
                'query': term,
                'page': page,
                'perPage': perPage
            }
        }
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

def studios(term : str, page : int = 1, perPage : int = 3):
    """
        TODO: Write this
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

    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json={
            'query': query_string,
            'variables': {
                'query': term,
                'page': page,
                'perPage': perPage
            }
        }
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