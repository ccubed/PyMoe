import requests
from ..errors import *

class HBirdLib:
    def __init__(self, api, header):
        self.apiurl = api
        self.header = header

    def get(self, username, status=None):
        """
        Get a user's library entries.

        :param username: The user whose entries we want.
        :param status: Optional filter. One of: currently-watching, plan-to-watch, completed, on-hold or dropped.
        :return: None or a list of library entry objects
        :rtype: NoneType or a list of dictionaries
        """
        if status:
            r = requests.get(self.apiurl + "/users/{}/library".format(username), params={'status': status},
                             headers=self.header)
        else:
            r = requests.get(self.apiurl + "/users/{}/library".format(username), headers=self.header)

        if r.status_code != 200:
            if r.status_code == 404:
                return None
            else:
                return ServerError

        jsd = r.json()
        if len(jsd):
            return jsd
        else:
            return None

    def set(self, aid, auth_token, **kwargs):
        """
        Prepare yourself for a giant list of params. This is the endpoint for adding and/or updating an entry. All kwargs are optional.

        :param aid: the anime id we're updating
        :param auth_token: The auth token received from the login function/endpoint.
        :param status: currently-watching, plan-to-watch, completed, on-hold, dropped
        :param privacy: public or private. Private means don't show to others.
        :param rating: 0, 0.5, 1, 1.5 ... 5. Setting it to 0 or the current value will remove it
        :param sane_rating_update: See above. Except with this one only setting it to 0 removes it.
        :param rewatching: true or false. You know, if you are rewatching it.
        :param rewatched_times: Number of rewatches. 0 or above.
        :param notes: Personal notes.
        :param episodes_watched: Number of episodes watched. Between 0 and total_episodes. If equal to total_episodes, you must set status to complete or you'll get 500'd.
        :param increment_episodes: If set to true will increment episodes_watched by 1. If used along with episodes_watched, will increment that value by 1.
        :return: True if Ok, False if we got an invalid JSON object
        :rtype: Boolean
        :raises: :class:`Pymoe.errors.ServerError` - 500
        :raises: :class:`Pymoe.errors.GeneralLoginError` - 401
        """
        params = kwargs
        params['auth_token'] = auth_token

        r = requests.post(self.apiurl + "/libraries/{}".format(aid), params=params, headers=self.header)

        if r.status_code not in [200, 201]:
            if r.status_code == 401:
                raise GeneralLoginError("Auth_Token not accepted for library update.")
            if r.status_code == 500:
                raise ServerError
            return False  # Must be an invalid json object
        return True

    def remove(self, aid, auth_token):
        """
        Remove an entry from a library.

        :param aid: The ID to be removed.
        :param auth_token: The auth_token for the user from the login function/endpoint.
        :return: True if successful
        :rtype: Boolean
        :raises: :class:`Pymoe.errors.ServerError` - 500
        :raises: :class:`Pymoe.errors.GeneralLoginError` - 401
        """
        r = requests.post(self.apiurl + "/libraries/{}/remove".format(aid), params={'auth_token': auth_token},
                          headers=self.header)

        if r.status_code != 201:
            if r.status_code == 401:
                raise GeneralLoginError("Auth_Token not accepted on library removal.")
            if r.status_code == 500:
                raise ServerError

        return True