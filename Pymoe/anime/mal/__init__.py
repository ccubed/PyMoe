from datetime import date
import requests
from pymoe.errors import *

class Mal:
    """
        Initialize a new instance to the MyAnimeList API.
        This instance will use your API Token to access public information.
        Get your API Token from https://myanimelist.net/apiconfig
    """
    def __init__(self, apikey : str):
        """
            This is a helper class to make managing API Changes easier.

            :param apikey: Provide your API KEY from the website.
        """
        self.settings = {
            'header': {
                'Content-Type': 'application/json',
                'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)',
                'Accept': 'application/json',
                'X-MAL-CLIENT-ID': apikey
            },
            'apiurl': 'https://api.myanimelist.net/v2/',
            'default_fields': 'id,title,main_picture,alternative_titles,start_date,end_date,nsfw,genres,status,media_type,broadcast'
        }

    @staticmethod
    def offsets(limit : int = 10, offset : int = 0, more : bool = True):
        """
            Static method to get rid of reused code to calculate the offsets for paging.

            :param limit: How many results on one page
            :param offset: which result did we start at
            :param more: Do we need a next?
        """
        return {
            "previous": (offset - limit) if offset > 0 else None,
            "next": (offset + limit) if more else None
        }

    @staticmethod
    def titleKeys(data : dict):
        """
            Static method to get rid of reused code that recreates the dictionary with the anime title as the key

            :param data: The dictionary to be realigned
        """
        return {item['node']['title'] : item['node'] for item in data}

    def search(self, name : str, limit : int = 10, offset : int = 0, fields : str = None, nsfw = None):
        """
            Search for anime matching name. If fields is none, it will default to giving enough information to facilitate finding an anime.
            Otherwise, provide a list of fields separated by ',' with no spaces.
            See self.settings['default_fields'] for an example.
            
            :param name: Term to search for
            :param limit: How many results on one page, defaults to 10 in alignment with API
            :param offset: Which result do I start at (exclusive), defaults to 0 in alignment with API
            :param fields: What fields should I return, defaults to None
            :param nsfw: By default most endpoints don't return NSFW content. Set this to some true value to get NSFW results.

            :return: A dictionary of search results with keys of the anime titles and a single paging key that gives the offset for the previous and next set of results.
        """
        r = requests.get(
            self.settings['apiurl'] + "anime",
            params={
                'q': name,
                'fields': fields or 'id,title,main_picture,alternative_titles,start_date',
                'limit': limit,
                'offset': offset,
                'nsfw': 'false' if not nsfw else 'true'
            },
            headers=self.settings['header']
        )

        if r.status_code != 200:
            raise ServerError(r.text, r.status_code)

        jsd = r.json()

        # Create a new Dictionary with the anime title as the key instead of just node
        rdict = self.titleKeys(jsd['data'])
        rdict['paging'] = self.offsets(limit, offset, 'next' in jsd['paging'])

        return rdict

    def get(self, id : int, fields : str = None):
        """
            Search for details on a specific anime with the id given.
            Fields will default to settings['default_fields'] unless provided.
        
            :param id: Which ID to get info on
            :param fields: A list of fields to grab separated by ',' with no spaces

            :return: A dictionary containing the information requested on the anime.
        """
        r = requests.get(
            self.settings['apiurl'] + "anime/{}".format(id),
            params={
                'fields': fields or self.settings['default_fields'],
                'nsfw': 'true' # If you search by ID, you want whatever you get
            },
            headers = self.settings['header']
        )
        
        if r.status_code != 200:
            raise ServerError(r.text, r.status_code)

        return r.json()

    def ranking(self, rank_type : str = "all", limit : int = 10, offset : int = 0, fields : str = None, nsfw = None ):
        """
            Get top lists by rank_type.
            rank_type can be one of all, airing, upcoming, tv, ova, movie, special, bypopularity, favorite.

            :param rank_type: A string specifying which ranking list to get
            :param limit: How many per page? Defaults to 10 in alignment with API
            :param offset: Which result do I start at (exclusive), defaults to 0 in alignment with API
            :param fields: A list of fields to grab separated by ',' with no spaces
            :param nsfw: By default most endpoints don't return NSFW content. Set this to some true value to get NSFW results.
        """
        r = requests.get(
            self.settings['apiurl'] + "anime/ranking",
            params={
                'ranking_type': rank_type,
                'limit': limit,
                'offset': offset,
                'fields': fields or 'id,title,main_picture,alternative_titles,start_date',
                'nsfw': 'false' if not nsfw else 'true'
            },
            headers = self.settings['header']
        )

        if r.status_code != 200:
            return None # TODO: This should return an error

        jsd = r.json()
        
        # Ok, let's make this dictionary useful again
        rdict = {}
        rdict['ranking'] = {item['ranking']['rank'] : item['node'] for item in jsd['data']}
        rdict['paging'] = self.offsets(limit, offset, 'next' in jsd['paging'])

        return rdict

    def seasonal(self, year : int = date.today().year, season : str = None, sort : str = "anime_score", limit : int = 10, offset : int = 0, fields : str = None, nsfw = None):
        """
            Get a list of anime for a given season and year.

            :param year: Which Year, defaults to Current Year
            :param season: Which Season, defaults to season based on Current Month
            :param sort: How should we sort results, defaults to 'anime_score' but can be 'anime_num_list_users' if given
            :param limit: How many results per page, defaults to 10
            :param offset: Which result do we start at (Exclusive), defaults to 0
            :param fields: A list of fields to grab separated by ',' with no space
            :param nsfw: By default most endpoints don't return NSFW content. Set this to some true value to get NSFW results.
        """
        myseason = season
        if not season:
            if date.today().month <= 3:
                myseason = "winter"
            elif date.today().month <= 6:
                myseason = "spring"
            elif date.today().month <= 9:
                myseason = "summer"
            else:
                myseason = "fall"
        
        r = requests.get(
            self.settings['apiurl'] + "anime/season/{}/{}".format(year, myseason),
            params = {
                'sort': sort,
                'limit': limit,
                'offset': offset,
                'fields': fields or 'id,title,main_picture,alternative_titles,start_date'
            },
            headers = self.settings['header']
        )

        if r.status_code != 200:
            return None # TODO: This should return an error

        jsd = r.json()

        # Create a new Dictionary with the anime title as the key instead of just node
        rdict = self.titleKeys(jsd['data'])
        rdict['paging'] = self.offsets(limit, offset, 'next' in jsd['paging'])

        return rdict
