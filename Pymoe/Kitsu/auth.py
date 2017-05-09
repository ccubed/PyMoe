import requests
from ..errors import *

class KitsuAuth:
    def __init__(self, header, cid, csecret):
        self.apiurl = "https://kitsu.io/api/oauth/token"
        self.header = header
        self.remember = False
        self.cid = cid
        self.csecret = csecret

    def remember(self, setting):
        """
        Adjust whether or not KitsuAuth will store your oauth tokens in memory. This enables you to call get on a user 
        name or alias and get that user's oauth token for your current session.
        
        :param setting: bool 
        :return: Nothing
        """
        self.remember = setting

    def authenticate(self, username, password, alias=None):
        """
        Obtain an oauth token. Pass username and password. Get a token back. If KitsuAuth is set to remember your tokens
        for this session, it will store the token under the username given and any aliases specified in alias.
        
        :param username: username
        :param password: password
        :param alias: A list of alternative names for a person if using the KitsuAuth token storage
        :return: The token or a ServerError
        """
        r = requests.get(self.apiurl, params={"grant_type": "password", "username": username, "password": password, "client_id": self.cid, "client_secret": self.csecret})

        if r.status_code != 200:
            raise ServerError

        return r.json()