import requests
from ..errors import *


class HBirdManga:
    def __init__(self, api, header):
        self.apiurl = api
        self.header = header

    def id(self, aid):
        """
        Get manga information by id.

        :param int aid: ID of the manga.
        :return: Dictionary or None (for not found)
        :rtype: Dictionary or None
        :raises: :class:`Pymoe.errors.ServerError`
        """
        r = requests.get(self.apiurl + "/manga/{}".format(aid), headers=self.header)

        if r.status_code != 200:
            if r.status_code == 404:
                return None
            else:
                raise ServerError

        return r.json()

    def search(self, term):
        """
        Search for manga by term.

        :param str term: What to search for.
        :return: The results as a list of Dictionaries objects. Limit 7. None if empty.
        :rtype: List of Dictionaries or NoneType
        """
        r = requests.get(self.apiurl + "/manga", params={"filter[text]": term}, headers=self.header)
        
        if r.status_code != 200:
            raise ServerError
        
        jsd = r.json()
        
        if len(jsd):
            return jsd
        else:
            return None