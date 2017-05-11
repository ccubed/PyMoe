import requests
from ..errors import *
from .helpers import SearchWrapper

class KitsuLib:
    def __init__(self, api, header):
        self.apiurl = api
        self.header = header

    def get(self, uid):
        """
        Get a user's list of library entries. This is a little annoying.
        The list of Library Entries by default doesn't name the item it relates
        to. Here's the other problem, it lists a relationship to all three
        types of items. And there's no indication of which type of item it is.
        I have no idea how to handle this and there's no way you can just make
        hundreds (and with some people thousands) of calls to see if it returns
        Null for the given item or until you get data back. Good Luck I guess.

        :param uid int: User ID to get library entries for
        """
        r = requests.get(self.apiurl + "/users/{}/library-entries".format(uid), headers=self.header)

        if r.status_code != 200:
            raise ServerError

        jsd = r.json()

        if jsd['meta']['count']:
            return SearchWrapper(jsd['data'], jsd['links']['next'] if 'next' in jsd['links'] else None, self.header)
        else:
            return None
