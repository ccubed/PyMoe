import requests
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

        if len(kwargs) == 2:
            if (('username' in kwargs) or ('email' in kwargs)) and 'password' in kwargs:
                user = kwargs.get('username') if 'username' in kwargs else kwargs.get('email')
                password = kwargs.pop('password')
                usertype = 'username' if 'username' in kwargs else 'email'
            else:
                raise SyntaxError("Invalid arguments passed to __init__ for login at hummingbird instance.")
            self._login(user, password, usertype)

    def _login(self, user, pw, usertype):
        """
        Login and get a user's auth_token

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

    def anime_id(self, aid, title=None):
        """
        Get anime information by id.

        :param aid: ID of the anime.
        :param title: If specified, will submit the title_language_preference param. This must be canonical, english or romanized.
        :return: Anime object (Dictionary) or None (for not found)
        """
        if title:
            r = requests.get(self.apiurl + "/anime/{}".format(aid), params={'title_language_preference': title},
                             headers=self.header)
        else:
            r = requests.get(self.apiurl + "/anime/{}".format(aid), headers=self.header)

        if r.status_code != 200:
            if r.status_code == 404:
                return None
            else:
                raise ServerError

        return r.json()

    def anime_v2(self, clientid, **kwargs):
        """
        This will call the V2 endpoint for anime. It requires an id and you have to register your application on hummingbird.

        :param clientid: The client id given to you after registering your app.

        Only Pass One of these
        :param id: The Hummingbird ID for the anime
        :param malid: The MyAnimeList ID for the anime
        :return: Anime Object V2 or None (for not found)
        """
        headers = self.header
        headers['X-Client-Id'] = clientid

        if 'id' in kwargs:
            url = "https://hummingbird.me/api/v2/anime/{}".format(kwargs.pop('id'))
        else:
            url = "https://hummingbird.me/api/v2/anime/myanimelist:{}".format(kwargs.pop('malid'))

        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            if r.status_code == 404:
                return None
            else:
                raise ServerError
        else:
            return r.json()

    def anime_search(self, term):
        """
        Search for anime by term.

        :param term: What to search for.
        :return: The results as an array of anime objects. Limit 7. None if empty.
        """
        r = requests.get(self.apiurl + "/search/anime", params={"query": term}, headers=self.header)
        if r.status_code != 200:
            raise ServerError
        jsd = r.json()
        if len(jsd):
            return jsd
        else:
            return None

    def library_all(self, username, status=None):
        """
        Get a user's library entries.

        :param username: The user whose entries we want.
        :param status: Optional filter. One of: currently-watching, plan-to-watch, completed, on-hold or dropped.
        :return: None or the results in a dictionary
        """
        if status:
            r = requests.get(self.apiurl + "/users/{}/library".format(username), params={'status': status}, headers=self.header)
        else:
            r = requests.get(self.apiurl+"/users/{}/library".format(username), headers=self.header)

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

    def library_add_update(self, aid, auth_token, **kwargs):
        """
        Prepare yourself for a giant list of params. :/
        This is the endpoint for adding and/or updating an entry.

        :param aid: the anime id we're updating
        :param auth_token: The auth token received from the login function/endpoint.

        This is the giant list of kwargs. All are optional.
        :param status: currently-watching, plan-to-watch, completed, on-hold, dropped
        :param privacy: public or private. Private means don't show to others.
        :param rating: 0, 0.5, 1, 1.5 ... 5. Setting it to 0 or the current value will remove it
        :param sane_rating_update: See above. Except with this one only setting it to 0 removes it.
        :param rewatching: true or false. You know, if you are rewatching it.
        :param rewatched_times: Number of rewatches. 0 or above.
        :param notes: Personal notes.
        :param episodes_watched: Number of episodes watch. Between 0 and total_episodes. If equal to total_episodes, you must set status to complete or you'll get 500'd.
        :param increment_episodes: If set to true will increment episodes_watched by 1. If used along with episodes_watched, will increment that value by 1.

        :return: True if Ok, ServerError if failed, GeneralLoginError if 401'd, False if we got an invalid JSON object
        """
        params = kwargs
        params['auth_token'] = auth_token

        r = requests.post(self.apiurl+"/libraries/{}".format(aid), params=params, headers=self.header)

        if r.status_code not in [200, 201]:
            if r.status_code == 401:
                raise GeneralLoginError("Auth_Token not accepted for library update.")
            if r.status_code == 500:
                raise ServerError
            return False  # Must be an invalid json object
        return True

    def library_remove(self, aid, auth_token):
        """
        Remove an entry from a library.

        :param aid: The ID to be removed.
        :param auth_token: The auth_token for the user from the login function/endpoint.
        :return: True if successful, GeneralLoginError for 401, ServerError for 500.
        """
        r = requests.post(self.apiurl + "/libraries/{}/remove".format(aid), params={'auth_token': auth_token}, headers=self.header)

        if r.status_code != 201:
            if r.status_code == 401:
                raise GeneralLoginError("Auth_Token not accepted on library removal.")
            if r.status_code == 500:
                raise ServerError

        return True

    def user_info(self, username):
        """
        Get information about a user.

        :param username: User to get information about.
        :return: User object or a json decoder error.
        """
        r = requests.get(self.apiurl+"/users/{}".format(username), headers=self.header)
        return r.json()

    def user_feed(self, username):
        """
        Get a user's activity feed.

        :param username: User whose feed we are getting
        :return: An array of story objects or a json decoder error
        """
        r = requests.get(self.apiurl + "/users/{}/feed".format(username), headers=self.header)
        return r.json()

    def user_favorite(self, username):
        """
        Get a user's favorite anime.

        :param username: User whose favorite anime we are retrieving.
        :return: An array of anime objects with an added fav_rank and fav_id key or ServerError on 500
        """
        r = requests.get(self.apiurl + "/users/{}/favorite_anime".format(username), headers=self.header)

        if r.status_code == 500:
            raise ServerError

        return r.json()
