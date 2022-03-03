import requests
from ..errors import *
from .helpers import SearchWrapper


class KitsuUser:
    def __init__(self, api, header):
        self.apiurl = api
        self.header = header

    def search(self, term):
        """
        Search for a user by name.

        :param str term: What to search for.
        :return: The results as a SearchWrapper iterator or None if no results.
        :rtype: SearchWrapper or None
        """
        r = requests.get(self.apiurl + "/users", params={"filter[name]": term}, headers=self.header)

        if r.status_code != 200:
            raise ServerError

        jsd = r.json()

        if jsd['meta']['count']:
            return SearchWrapper(jsd['data'], jsd['links']['next'] if 'next' in jsd['links'] else None, self.header)
        else:
            return None

    def create(self, data):
        """
        Create a user. Please review the attributes required. You need only provide the attributes.

        :param data: A dictionary of the required attributes
        :return: Dictionary returned by server or a ServerError exception
        :rtype: Dictionary or Exception
        """
        final_dict = {"data": {"type": "users", "attributes": data}}
        r = requests.post(self.apiurl + "/users", json=final_dict, headers=self.header)

        if r.status_code != 200:
            raise ServerError

        return r.json()

    def get(self, uid):
        """
        Get a user's information by their id.

        :param uid str: User ID
        :return: The user's information or None
        :rtype: Dictionary or None
        """
        r = requests.get(self.apiurl + "/users/{}".format(uid), headers=self.header)

        if r.status_code != 200:
            raise ServerError

        jsd = r.json()

        if jsd['data']:
            return jsd['data']
        else:
            return None

    def update(self, uid, data, token):
        """
        Update a user's data. Requires an auth token.

        :param uid str: User ID to update
        :param data dict: The dictionary of data attributes to change. Just the attributes.
        :param token str: The authorization token for this user
        :return: True or Exception
        :rtype: Bool or ServerError
        """
        final_dict = {"data": {"id": uid, "type": "users", "attributes": data}}
        final_headers = self.header
        final_headers['Authorization'] = "Bearer {}".format(token)
        r = requests.patch(self.apiurl + "/users/{}".format(uid), json=final_dict, headers=final_headers)

        if r.status_code != 200:
            raise ServerError

        return True
