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
    def __init__(self, cid = None, csecret = None, credentials = None):
        """
        :param cid: Client ID
        :param csecret: Client Secret
        :param credentials: If provided, a JWT token for auth requests
        """
        self.settings = {'header': {'Content-Type': 'application/json',
                                    'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)',
                                    'Accept': 'application/json'},
                         'authurl': 'https://anilist.co/api',
                         'apiurl': 'https://graphql.anilist.co',
                         'cid': cid,
                         'csecret': csecret,
                         'token': credentials}
        self.search = ASearch(self.settings)
        self.get = AGet(self.settings)
