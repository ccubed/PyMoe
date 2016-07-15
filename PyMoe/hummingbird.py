import requests
import ujson
from .errors import *

class hummingbird:
    def __init__(self, **kwargs):
        """
        Initialize a new hummingbird API instance. If you want to log in as a certain user, then pass either a username
        or email and a password. Do not pass both.

        ONLY PASS ONE OF THESE
        :param username: The user's username to login with.
        :param email: The user's email to login with.

        :param password: The user's password
        """
        self.apiurl = "https://hummingbird.me/api/v1"
        self.header = {'User-Agent': 'PyMoe (git.vertinext.com/ccubed/PyMoe'}
        self.user = None
        self.password = None
        self.usertype = None
        if len(kwargs) == 2:
            if (('username' in kwargs) or ('email' in kwargs)) and 'password' in kwargs:
                self.user = kwargs.get('username') if 'username' in kwargs else kwargs.get('email')
                self.password = kwargs.pop('password')
                self.usertype = 'username' if 'username' in kwargs else 'email'
            else:
                raise SyntaxError("Invalid arguments passed to __init__ for login at hummingbird instance.")
            self._login()

    def _login(self):
        """
        Login and get a user's auth_token
        """
        r = requests.post(self.apiurl+"/users/authenticate", params={self.usertype: self.user, 'password': self.password}, headers=self.header)
        if r.status_code != 201:
            raise GeneralLoginError("{} and password combination not accepted by hummingbird.".format(self.usertype))
        else:
            return r.json()

    def login(self, password, **kwargs):
        """
        A public method for logging in later after initialization.
        :param password: user's password.

        Pass one of these:
        :param username: the username to login with
        :param email: the email to login with
        :return: User's auth_token

        Errors:
            MoeError.GeneralLoginError - Got a Not Authorized
            SyntaxError - Read the docstring again
        """
        if len(kwargs):
            self.password = password
            if 'username' in kwargs:
                self.usertype = 'username'
                self.user = kwargs.pop('username')
            else:
                self.usertype = 'email'
                self.user = kwargs.pop('email')
            return self._login()
        else:
            raise SyntaxError("Not enough parameters to login.")

    def anime(self, id, title=None):
        """
        Get anime information by id.

        :param id: ID of the anime.
        :param title: If specified, will submit the title_language_preference param. This must be canonical, english or romanized.
        :return: Anime object (Dictionary)
        """
        if title:
            r = requests.get(self.apiurl+"/anime/{}".format(id), params={'title_language_preference': title}, headers=self.header)
        else:
            r = requests.get(self.apiurl+"/anime/{}".format(id), headers=self.header)
        if r.status_code != 200:
            raise ServerError
        return r.json()

    def anime_v2(self, clientid, **kwargs):
        """
        This will call the V2 endpoint for anime. It requires an id and you have to register your application on hummingbird.

        :param clientid: The client id given to you after registering your app.

        Only Pass One of these
        :param id: The Hummingbird ID for the anime
        :param malid: The MyAnimeList ID for the anime
        :return: Anime Object V2
        """
