from datetime import date
import ujson
import requests
from pymoe.errors import serializationFailed, serverError, methodNotSupported
from pymoe.helpers import whatSeason

settings = {
    'header': {
        'Content-Type': 'application/json',
        'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)',
        'Accept': 'application/json'
    },
    'apiurl': 'https://graphql.anilist.co'
}

def character(item_id : int):
    """
        Get a character with a certain ID in the anilist API.

        :param item_id: The ID of the character you want information on.
    """
    query_string = '''
        query ($id: Int){
            Character (id: $id){
                name{
                    full
                }
                image {
                    large
                    medium
                }
                description
                gender
                age
                siteUrl
                media{
                    nodes{
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
    '''

    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json={
            'query': query_string,
            'variables': {
                'id': item_id
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

def show(item_id : int):
    """
        Get a show with a certain ID in the anilist API.

        :param item_id: The ID of the show you want information on.
    """
    query_string = '''
        query ($id: Int) {
            Media (id: $id, type: ANIME) {
                title {
                    romaji
                    english
                    native
                }
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
                bannerImage
                format
                status
                episodes
                season
                seasonYear
                description
                averageScore
                meanScore
                genres
                synonyms
                isAdult
                siteUrl
                nextAiringEpisode {
                    timeUntilAiring
                    airingAt
                }
                streamingEpisodes {
                    title
                    thumbnail
                    url
                    site
                }
                externalLinks{
                    url
                    site
                    language
                }
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
    '''

    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json={
            'query': query_string,
            'variables': {
                'id': item_id
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

def season(theSeason : str = None, year : int = date.today().year, page : int = 1, perPage : int = 3):
    """
        Get a list of seasonal anime given a season and year.

        :param theSeason: What Season? See pymoe.helpers for a list of seasons.
        :param year: What year do you want info on?
        :param page: Which page of results do you want?
        :param perPage: How many results per page?

        TODO: Test return data on this
    """
    myseason = theSeason if theSeason else whatSeason(date.today().month)

    query_string = '''
        query($season: MediaSeason, $seasonYear: Int, $page: Int, $perPage: Int){
            Page (page: $page, perPage: $perPage) {
                pageInfo {
                    currentPage
                    hasNextPage
                }
                media (season: $season, seasonYear: $seasonYear){
                    id
                    idMal
                    title
                    description
                    genres
                    coverImage
                    isAdult
                    nextAiringEpisode {
                        timeUntilAiring
                        airingAt
                    }
                    startDate
                    streamingEpisodes {
                        title
                        thumbnail
                        url
                        site
                    }
                    siteUrl
                    externalLinks {
                        url
                        site
                        language
                    }
                }
            }
        }
    '''

    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json={
            'query': query_string,
            'variables': {
                'season': myseason,
                'seasonYear': year,
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


def episode(item_id : int):
    """
        Unsupported on Anilist
    """
    raise methodNotSupported("pymoe.anime.get.anilist.episode", "anilist")
    

def streaming(item_id : int, page : int = 1, perPage : int = 3):
    '''
        Given a show ID, return all streaming links for that show.

        :param item_id: The ID of the show you want streaming links for
    '''
    query_string = '''
        query ($id: Int) {
            Media(id: $id){
                streamingEpisodes {
                    title
                    thumbnail
                    url
                    site
                }
            }
        }
    '''

    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json={
            'query': query_string,
            'variables': {
                'id': item_id                
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


def staff(item_id : int):
    """
        Get information on a specific staffer given their ID.

        :param item_id: The ID of the staff member you want information on.
    """
    query_string = '''
        query ($id: Int){
            Staff (id: $id){
                name {
                    full
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
                staffMedia{
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
                characters{
                    nodes {
                        name {
                            full
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
    '''

    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json={
            'query': query_string,
            'variables': {
                'id': item_id
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

def studio(item_id : int):
    """
        Get a studio with a specific id.

        :param item_id: The ID of the studio you want information on.
    """
    query_string = '''
        query ($id: Int) {
            Studio (id: $id) {
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
    '''

    r = requests.post(
        settings['apiurl'],
        headers = settings['header'],
        json={
            'query': query_string,
            'variables': {
                'id': item_id
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
