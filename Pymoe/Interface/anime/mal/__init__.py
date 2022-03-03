import html
import xml.etree.ElementTree as ET
import requests
from .Abstractions import NT_MANGA, NT_ANIME, STATUS_INTS, NT_SEARCH_ANIME, \
    NT_SEARCH_MANGA, NT_USER_ANIME, NT_USER_MANGA
from requests.auth import HTTPBasicAuth
from .Objects import Anime, Manga, User
from ..errors import *


class Mal:
    """
    The interface for MyAnimeList, quite possibly the worst API in existence.

    :ivar NT_ANIME \aanime: Stores function references for anime. references available: search, add, update and delete.
    :ivar NT_MANGA manga: Stores function references for manga. references available: search, add, update and delete.
    """

    def __init__(self, username, password):
        """
        Initialize the instance. All methods require authorization so username and password aren't optional.

        :param username: The username to use.
        :param password: The password for that username.
        """
        self.apiurl = "https://myanimelist.net/api/"
        self.apiusers = "https://myanimelist.net/malappinfo.php"
        self.header = {'User-Agent': 'Pymoe (git.vertinext.com/ccubed/Pymoe)'}
        self.anime = NT_ANIME(search=self._search_anime, add=self._anime_add,
                              update=self._anime_update, delete=self._anime_delete)
        self.manga = NT_MANGA(search=self._search_manga, add=self._manga_add,
                              update=self._manga_update, delete=self._manga_delete)
        self._username = username
        self._password = password
        self._verify_credentials()

    def _verify_credentials(self):
        """
        An internal method that verifies the credentials given at instantiation.

        :raises: :class:`Pymoe.errors.UserLoginFailed`
        """
        r = requests.get(self.apiurl + "account/verify_credentials.xml",
                         auth=HTTPBasicAuth(self._username, self._password),
                         headers=self.header)
        if r.status_code != 200:
            raise UserLoginFailed("Username or Password incorrect.")

    def _search_anime(self, term):
        """
        An internal method that redirects to the real search method.

        :param term: What we are searching for.
        :rtype: list
        :return: list of :class:`Pymoe.Mal.Objects.Anime` objects
        """
        return self._search(1, term)

    def _search_manga(self, term):
        """
        An internal method that redirects to the real search method.

        :param term: What we are searching for.
        :rtype: list
        :return: list of :class:`Pymoe.Mal.Objects.Manga` objects
        """
        return self._search(2, term)

    def _search(self, which, term):
        """
        The real search method.

        :param which: 1 for anime, 2 for manga
        :param term: What to search for
        :rtype: list
        :return: list of :class:`Pymoe.Mal.Objects.Manga` or :class:`Pymoe.Mal.Objects.Anime` objects as per the type param.
        """
        url = self.apiurl + "{}/search.xml".format('anime' if which == 1 else 'manga')
        r = requests.get(url, params={'q': term},
                         auth=HTTPBasicAuth(self._username, self._password),
                         headers=self.header)
        if r.status_code != 200:
            return []
        data = ET.fromstring(r.text)
        final_list = []
        if which == 1:
            for item in data.findall('entry'):
                syn = item.find('synonyms').text.split(';') if item.find('synonyms').text else []
                final_list.append(Anime(
                    item.find('id').text,
                    title=item.find('title').text,
                    synonyms=syn.append(item.find('english').text),
                    episodes=item.find('episodes').text,
                    average=item.find('score').text,
                    anime_start=item.find('start_date').text,
                    anime_end=item.find('end_date').text,
                    synopsis=html.unescape(item.find('synopsis').text.replace('<br />', '')) if item.find(
                        'synopsis').text else None,
                    image=item.find('image').text,
                    status_anime=item.find('status').text,
                    type=item.find('type').text
                ))
            return NT_SEARCH_ANIME(
                airing=[x for x in final_list if x.status.series == "Currently Airing"],
                finished=[x for x in final_list if x.status.series == "Finished Airing"],
                unaired=[x for x in final_list if x.status.series == "Not Yet Aired"],
                dropped=[x for x in final_list if x.status.series == "Dropped"],
                planned=[x for x in final_list if x.status.series == "Plan to Watch"]
            )
        else:
            for item in data.findall('entry'):
                syn = item.find('synonyms').text.split(';') if item.find('synonyms').text else []
                final_list.append(Manga(
                    item.find('id').text,
                    title=item.find('title').text,
                    synonyms=syn.append(item.find('english').text),
                    chapters=item.find('chapters').text,
                    volumes=item.find('volumes').text,
                    average=item.find('score').text,
                    manga_start=item.find('start_date').text,
                    manga_end=item.find('end_date').text,
                    synopsis=html.unescape(item.find('synopsis').text.replace('<br />', '')) if item.find(
                        'synopsis').text else None,
                    image=item.find('image').text,
                    status_manga=item.find('status').text,
                    type=item.find('type').text
                ))
            return NT_SEARCH_MANGA(
                publishing=[x for x in final_list if x.status.series == "Publishing"],
                finished=[x for x in final_list if x.status.series == "Finished"],
                unpublished=[x for x in final_list if x.status.series == "Not Yet Published"],
                dropped=[x for x in final_list if x.status.series == "Dropped"],
                planned=[x for x in final_list if x.status.series == "Plan to Read"]
            )

    def _anime_add(self, data):
        """
        Adds an anime to a user's list.

        :param data: A :class:`Pymoe.Mal.Objects.Anime` object with the anime data
        :raises: SyntaxError on invalid data type
        :raises: ServerError on failure to add
        :rtype: Bool
        :return: True on success
        """
        if isinstance(data, Anime):
            xmlstr = data.to_xml()
            r = requests.get(self.apiurl + "animelist/add/{}.xml".format(data.id),
                             params={'data': xmlstr},
                             auth=HTTPBasicAuth(self._username, self._password),
                             headers=self.header)
            if r.status_code != 201:
                raise ServerError(r.text, r.status_code)
            return True
        else:
            raise SyntaxError(
                "Invalid type: data should be a Pymoe.Mal.Objects.Anime object. Got a {}".format(type(data)))

    def _manga_add(self, data):
        """
        Adds a manga to a user's list.

        :param data: A :class:`Pymoe.Mal.Objects.Manga` object with the manga data
        :raises: SyntaxError on invalid data type
        :raises: ServerError on failure to add
        :rtype: Bool
        :return: True on success
        """
        if isinstance(data, Manga):
            xmlstr = data.to_xml()
            r = requests.get(self.apiurl + "mangalist/add/{}.xml".format(data.id),
                             params={'data': xmlstr},
                             auth=HTTPBasicAuth(self._username, self._password),
                             headers=self.header)
            if r.status_code != 201:
                raise ServerError(r.text, r.status_code)
            return True
        else:
            raise SyntaxError(
                "Invalid type: data should be a Pymoe.Mal.Objects.Manga object. Got a {}".format(type(data)))

    def _anime_update(self, data):
        """
        Updates data for an anime on a user's list.

        :param data: A :class:`Pymoe.Mal.Objects.Anime` object with the anime data
        :raises: SyntaxError on invalid data type
        :raises: ServerError on failure to add
        :rtype: Bool
        :return: True on success
        """
        if isinstance(data, Anime):
            xmlstr = data.to_xml()
            r = requests.get(self.apiurl + "animelist/update/{}.xml".format(data.id),
                             params={'data': xmlstr},
                             auth=HTTPBasicAuth(self._username, self._password),
                             headers=self.header)
            if r.status_code != 200:
                raise ServerError(r.text, r.status_code)
            return True
        else:
            raise SyntaxError(
                "Invalid type: data should be a Pymoe.Mal.Objects.Anime object. Got a {}".format(type(data)))

    def _manga_update(self, data):
        """
        Updates data for a manga on a user's list.

        :param data: A :class:`Pymoe.Mal.Objects.Manga` object with the manga data
        :raises: SyntaxError on invalid data type
        :raises: ServerError on failure to add
        :rtype: Bool
        :return: True on success
        """
        if isinstance(data, Manga):
            xmlstr = data.to_xml()
            r = requests.get(self.apiurl + "mangalist/update/{}.xml".format(data.id),
                             params={'data': xmlstr},
                             auth=HTTPBasicAuth(self._username, self._password),
                             headers=self.header)
            if r.status_code != 200:
                raise ServerError(r.text, r.status_code)
            return True
        else:
            raise SyntaxError(
                "Invalid type: data should be a Pymoe.Mal.Objects.Manga object. Got a {}".format(type(data)))

    def _anime_delete(self, data):
        """
        Deletes an anime from a user's list

        :param data: A :class:`Pymoe.Mal.Objects.Anime` object with the anime data
        :raises: SyntaxError on invalid data type
        :raises: ServerError on failure to add
        :rtype: Bool
        :return: True on success
        """
        if isinstance(data, Anime):
            r = requests.get(self.apiurl + "animelist/delete/{}.xml".format(data.id),
                             auth=HTTPBasicAuth(self._username, self._password),
                             headers=self.header)
            if r.status_code != 200:
                raise ServerError(r.text, r.status_code)
            return True
        else:
            raise SyntaxError(
                "Invalid type: data should be a Pymoe.Mal.Objects.Anime object. Got a {}".format(type(data)))

    def _manga_delete(self, data):
        """
        Deletes a manga from a user's list

        :param data: A :class:`Pymoe.Mal.Objects.Manga` object with the manga data
        :raises: SyntaxError on invalid data type
        :raises: ServerError on failure to add
        :rtype: Bool
        :return: True on success
        """
        if isinstance(data, Manga):
            r = requests.get(self.apiurl + "mangalist/delete/{}.xml".format(data.id),
                             auth=HTTPBasicAuth(self._username, self._password),
                             headers=self.header)
            if r.status_code != 200:
                raise ServerError(r.text, r.status_code)
            return True
        else:
            raise SyntaxError(
                "Invalid type: data should be a Pymoe.Mal.Objects.Manga object. Got a {}".format(type(data)))

    def user(self, name):
        """
        Get a user's anime list and details. This returns an encapsulated data type.

        :param str name: The username to query
        :rtype: :class:`Pymoe.Mal.Objects.User`
        :return: A :class:`Pymoe.Mal.Objects.User` Object
        """
        anime_data = requests.get(self.apiusers, params={'u': name, 'status': 'all', 'type': 'anime'},
                                  headers=self.header)

        if anime_data.status_code != 200:
            raise ConnectionError(
                "Anime Data Request failed. Please Open a bug on https://github.com/ccubed/Pymoe and include the following data.\nStatus Code: {}\n\nText:{}".format(
                    anime_data.status_code, anime_data.text))

        manga_data = requests.get(self.apiusers, params={'u': name, 'status': 'all', 'type': 'manga'},
                                  headers=self.header)

        if manga_data.status_code != 200:
            raise ConnectionError(
                "Manga Data Request failed. Please Open a bug on https://github.com/ccubed/Pymoe and include the following data.\nStatus Code: {}\n\nText:{}".format(
                    manga_data.status_code, manga_data.text))

        root = ET.fromstring(anime_data.text)
        uid = root.find('myinfo').find('user_id').text
        uname = root.find('myinfo').find('user_name').text
        anime_object_list = self.parse_anime_data(anime_data.text)
        manga_object_list = self.parse_manga_data(manga_data.text)
        return User(uid=uid,
                    name=uname,
                    anime_list=NT_USER_ANIME(
                        watching=[x for x in anime_object_list['data'] if x.status.user == "Currently Watching"],
                        completed=[x for x in anime_object_list['data'] if x.status.user == "Completed"],
                        held=[x for x in anime_object_list['data'] if x.status.user == "On Hold"],
                        dropped=[x for x in anime_object_list['data'] if x.status.user == "Dropped"],
                        planned=[x for x in anime_object_list['data'] if x.status.user == "Plan to Watch"]
                    ),
                    anime_days=anime_object_list['days'],
                    manga_list=NT_USER_MANGA(
                        reading=[x for x in manga_object_list['data'] if x.status.user == "Currently Reading"],
                        completed=[x for x in manga_object_list['data'] if x.status.user == "Completed"],
                        held=[x for x in manga_object_list['data'] if x.status.user == "On Hold"],
                        dropped=[x for x in manga_object_list['data'] if x.status.user == "Dropped"],
                        planned=[x for x in manga_object_list['data'] if x.status.user == "Plan to Read"]
                    ),
                    manga_days=manga_object_list['days'])

    @staticmethod
    def parse_anime_data(xml):
        root = ET.fromstring(xml)
        anime_list = []
        for item in root.findall('anime'):
            syn = item.find('series_synonyms').text.split(';') if item.find('series_synonyms').text else []
            anime_list.append(Anime(
                item.find('series_animedb_id').text,
                title=item.find('series_title').text,
                synonyms=syn,
                episodes=item.find('series_episodes').text,
                episode=item.find('my_watched_episodes').text,
                score=item.find('my_score').text,
                anime_start=item.find('series_start').text,
                anime_end=item.find('series_end').text,
                date_start=item.find('my_start_date').text,
                date_finish=item.find('my_finish_date').text,
                image=item.find('series_image').text,
                status_anime=STATUS_INTS['anime'][item.find('series_status').text],
                status=STATUS_INTS['user']['anime'][item.find('my_status').text],
                rewatching=int(item.find('my_rewatching').text) if item.find('my_rewatching').text else None,
                type=item.find('series_type').text,
                tags=item.find('my_tags').text.split(',') if item.find('my_tags').text else []
            ))
        return {'data': anime_list,
                'days': root.find('myinfo').find('user_days_spent_watching').text}

    @staticmethod
    def parse_manga_data(xml):
        root = ET.fromstring(xml)
        manga_list = []
        for item in root.findall('manga'):
            syn = item.find('series_synonyms').text.split(';') if item.find('series_synonyms').text else []
            manga_list.append(Manga(
                item.find('series_mangadb_id').text,
                title=item.find('series_title').text,
                synonyms=syn,
                chapters=item.find('series_chapters').text,
                volumes=item.find('series_volumes').text,
                chapter=item.find('my_read_chapters').text,
                volume=item.find('my_read_volumes').text,
                user=item.find('my_score').text,
                manga_start=item.find('series_start').text,
                manga_end=item.find('series_end').text,
                date_start=item.find('my_start_date').text,
                date_finish=item.find('my_finish_date').text,
                image=item.find('series_image').text,
                status_manga=STATUS_INTS['manga'][item.find('series_status').text],
                status=STATUS_INTS['user']['manga'][item.find('my_status').text],
                rereading=int(item.find('my_rereadingg').text) if item.find('my_rereadingg') else None,
                type=item.find('series_type').text,
                tags=item.find('my_tags').text.split(',') if item.find('my_tags').text else []
            ))
        return {'data': manga_list,
                'days': root.find('myinfo').find('user_days_spent_watching').text}
