import requests
import ujson
from datetime import timedelta
import time
from .errors import *


class Anilist:
    def __init__(self, cid, csecret):
        """
        Initialize an instance of the AniList API interface. Pass your client id and client secret in.
        This is stored on the instance so that it can make calls against your id and secret.
        This interface will handle readonly credentials and will use them to gather information from calls
        that do not require a user's details. On calls that require a specific user's details, you will
        be asked to provide that users token.

        :param cid: Client ID
        :param csecret: Client Secret
        """
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'PyMoe'}
        self.apiurl = "https://anilist.co/api"
        self.cid = cid
        self.csecret = csecret
        self.readonly = {}
        self.get_readonly()

    def get_readonly(self):
        data = {'grant_type': 'client_credentials', 'client_id': self.cid, 'client_secret': self.csecret}
        req = requests.post(self.apiurl + '/auth/access_token', params=data)
        if req.status_code == 200:
            jsd = req.json()
            self.readonly = {'Expiration': jsd['expires'], 'Token': jsd['access_token']}
