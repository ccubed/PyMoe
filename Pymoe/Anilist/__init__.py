from .auth import *


class Anilist:
    """
        Initialize a new instance to the Anilist API. This instance will handle read only credentials.
        Pass in your client id and client secret. In calls that require a user's auth token, you will need to provide it.

        :ivar dict settings: Various settings used across the module
        :ivar ALAuth auth: Handle Authorization endpoints
    """
    def __init__(self, csecret, cid):
        """
        :param csecret: Client Secret
        :param cid: Client ID
        """
        self.settings = {'header': {'Content-Type': 'application/x-www-form-urlencoded',
                                    'User-Agent': 'Pymoe (git.vertinext.com/ccubed/PyMoe'},
                         'apiurl': 'https://anilist.co/api',
                         'cid': cid,
                         'csecret': csecret}
        self.auth = ALAuth(self.settings)
