import requests
from ..errors import *


class HBirdAnime:
    def __init__(self, api, header):
        self.apiurl = api
        self.header = header

    def id(self, aid, title=None):
        """
        Get anime information by id.

        :param int aid: ID of the anime.
        :param str title: If specified, will submit the title_language_preference param. This must be canonical, english or romanized.
        :return: Anime object or None (for not found)
        :rtype: Dictionary or None
        :raises: :class:`Pymoe.errors.ServerError`
        """
        if title:
            r = requests.get(self.apiurl + "/anime/{}".format(aid), params={'title_language_preference': title},
                             headers=self.header)
        else:
            r = requests.get(self.apiurl + "/anime/{}".format(aid), headers=self.header)

        if r.status_code != 200:
            if r.status_code == 404:
                return None
            else:
                raise ServerError

        return r.json()

    def v2(self, clientid, **kwargs):

        """
        This will call the V2 endpoint for anime. It requires an id and you have to register your application on hummingbird. You should only pass one of id or malid.

        :param str clientid: The client id given to you after registering your app.
        :param int id: The Hummingbird ID for the anime
        :param int malid: The MyAnimeList ID for the anime
        :return: Anime Object V2 or None (for not found)
        :rtype: Dictionary or NoneType
        :raises: :class:`Pymoe.errors.ServerError`
        """
        headers = self.header
        headers['X-Client-Id'] = clientid

        if 'id' in kwargs:
            url = "https://hummingbird.me/api/v2/anime/{}".format(kwargs.pop('id'))
        else:
            url = "https://hummingbird.me/api/v2/anime/myanimelist:{}".format(kwargs.pop('malid'))

        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            if r.status_code == 404:
                return None
            else:
                raise ServerError
        else:
            return r.json()

    def search(self, term):
        """
        Search for anime by term.

        :param str term: What to search for.
        :return: The results as a list of anime objects. Limit 7. None if empty.
        :rtype: List of Dictionaries or NoneType
        """
        r = requests.get(self.apiurl + "/search/anime", params={"query": term}, headers=self.header)
        if r.status_code != 200:
            raise ServerError
        jsd = r.json()
        if len(jsd):
            return jsd
        else:
            return None
