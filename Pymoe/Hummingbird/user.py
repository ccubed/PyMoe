import requests
from ..errors import *


class HBirdUser:
    def __init__(self, api, header):
        self.apiurl = api
        self.header = header

    def _login(self, user, pw, usertype):
        """
        Login and get a user's auth_token. Internal function.

        :param user: username or email
        :param pw: password
        :param usertype: email or username, used for the params.
        """
        r = requests.post(self.apiurl + "/users/authenticate", params={usertype: user, 'password': pw},
                          headers=self.header)
        if r.status_code != 201:
            raise GeneralLoginError("{} and password combination not accepted by hummingbird.".format(usertype))
        else:
            return r.json()

    def authenticate(self, password, **kwargs):
        """
        A method for calling the authenticate endpoint to login as a specific user and obtain an auth_token.
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
            pw = password
            if 'username' in kwargs:
                usertype = 'username'
                user = kwargs.pop('username')
            else:
                usertype = 'email'
                user = kwargs.pop('email')
            return self._login(user, pw, usertype)
        else:
            raise SyntaxError("Not enough parameters to login.")

    def info(self, username):
        """
        Get information about a user.

        :param username: User to get information about.
        :return: User object or a json decoder error.
        """
        r = requests.get(self.apiurl + "/users/{}".format(username), headers=self.header)
        return r.json()

    def feed(self, username):
        """
        Get a user's activity feed.

        :param username: User whose feed we are getting
        :return: An array of story objects or a json decoder error
        """
        r = requests.get(self.apiurl + "/users/{}/feed".format(username), headers=self.header)
        return r.json()

    def favorite_anime(self, username):
        """
        Get a user's favorite anime.

        :param username: User whose favorite anime we are retrieving.
        :return: An array of anime objects with an added fav_rank and fav_id key or ServerError on 500
        """
        r = requests.get(self.apiurl + "/users/{}/favorite_anime".format(username), headers=self.header)

        if r.status_code == 500:
            raise ServerError

        return r.json()