import time
import requests
from .get import *
from .search import *

class Anilist:
    """
        Initialize a new instance to the Anilist API.
        This instance will handle read only credentials.
        Pass in your client id and client secret.
        In calls that require a user's auth token, you will need to provide it.

        :ivar dict settings: Various settings used across the module
        :ivar ALAuth auth: Handle Authorization endpoints
    """
    def __init__(self, cid, csecret):
        """
        :param cid: Client ID
        :param csecret: Client Secret
        """
        self.settings = {'header': {'Content-Type': 'application/x-www-form-urlencoded',
                                    'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)'},
                         'apiurl': 'https://anilist.co/api',
                         'cid': cid,
                         'csecret': csecret}
        self.credentials = None
        self.search = ASearch(self.readonly, self.settings)
        self.get = AGet(self.readonly, self.settings)

    def readonly(self):
        """
        Grab readonly credentials. Used for calls that don't need user permissions.

        :return: Nothing
        :raises: JSONDecodeError
        """
        if self.credentials is None or int(self.credentials['expires']) < time.time():
            r = requests.post(self.settings['apiurl'] + "/auth/access_token",
                              params={'grant_type': 'client_credentials', 'client_id': self.settings['cid'],
                                      'client_secret': self.settings['csecret']},
                              headers=self.settings['header'])
            self.credentials = r.json()
            return self.credentials['access_token']
        else:
            return self.credentials['access_token']

    def refresh_authorization(self, refresh_token):
        """
        The oauth flow in general is outside the scope of what this lib wants to provide,
        but it does at least provide assistance in refreshing access tokens.

        :param refresh_token: your refresh token
        :return: a dictionary consisting of: access_token, token_type, expires, and expires_in or None to indicate an error
        :rtype: Dictionary, NoneType
        """
        r = requests.post(self.settings['apiurl'] + "/auth/access_token",
                          params={'grant_type': 'refresh_token', 'client_id': self.settings['cid'],
                                  'client_secret': self.settings['csecret'], 'refresh_token': refresh_token},
                          headers=self.settings['header'])
        if r.status_code == 200:
            return r.json()
        else:
            return None
