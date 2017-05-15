import requests
import time
from ..errors import *


class KitsuAuth:
    def __init__(self, header, cid, csecret):
        self.apiurl = "https://kitsu.io/api/oauth"
        self.header = header
        self.remember = False
        self.cid = cid
        self.csecret = csecret
        self.token_storage = {}

    def set_remember(self, setting):
        """
        Adjust whether or not KitsuAuth will store your oauth tokens in memory. This enables you to call get on a user
        name or alias and get that user's oauth token for your current session.

        :param setting: bool
        :return: Nothing
        """
        self.remember = setting

    def authenticate(self, username, password):
        """
        Obtain an oauth token. Pass username and password. Get a token back. If KitsuAuth is set to remember your tokens
        for this session, it will store the token under the username given.

        :param username: username
        :param password: password
        :param alias: A list of alternative names for a person if using the KitsuAuth token storage
        :return: A tuple of (token, expiration time in unix time stamp, refresh_token) or ServerError
        """
        r = requests.post(self.apiurl + "/token",
                          params={"grant_type": "password", "username": username, "password": password,
                                  "client_id": self.cid, "client_secret": self.csecret})

        if r.status_code != 200:
            raise ServerError

        jsd = r.json()

        if self.remember:
            self.token_storage[username] = {'token': jsd['access_token'], 'refresh': jsd['refresh_token'],
                                            'expiration': int(jsd['created_at']) + int(jsd['expires_in'])}

        return jsd['access_token'], int(jsd['expires_in']) + int(jsd['created_at']), jsd['refresh_token']

    def refresh(self, refresh_token):
        """
        Renew an oauth token given an appropriate refresh token.

        :param refresh_token: The Refresh Token
        :return: A tuple of (token, expiration time in unix time stamp)
        """
        r = requests.post(self.apiurl + "/token", params={"grant_type": "refresh_token", "client_id": self.cid,
                                                          "client_secret": self.csecret,
                                                          "refresh_token": refresh_token})

        if r.status_code != 200:
            raise ServerError

        jsd = r.json()

        return jsd['access_token'], int(jsd['expires_in']) + int(jsd['created_at'])

    #TODO: Test that this is now fixed
    def get(self, username):
        """
        If using the remember option and KitsuAuth is storing your tokens, this function will retrieve one.

        :param username: The username whose token we are retrieving
        :return: A token, NotFound or NotSaving error
        """
        if not self.remember:
            raise NotSaving

        if username not in self.token_storage:
            raise UserNotFound

        if self.token_storage[username]['expiration'] < time.time():
            new_token = self.refresh(self.token_storage[username]['refresh'])
            self.token_storage[username]['token'] = new_token[0]
            self.token_storage[username]['expiration'] = new_token[1]
            return new_token[0]
        else:
            return self.token_storage[username]['token']
