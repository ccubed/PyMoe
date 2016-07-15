import requests
import time


class ALAuth:
    def __init__(self, settings):
        self.settings = settings
        self.credentials = None
        self.readonly()

    def readonly(self):
        """
        Grab readonly credentials. Used for calls that don't need user permissions.

        :return: Nothing or an error
        """
        if self.credentials is None or int(self.credentials['expires']) < time.time():
            r = requests.post(self.settings['apiurl'] + "/auth/access_token",
                              params={'grant_type': 'client_credentials', 'client_id': self.settings['cid'],
                                      'client_secret': self.settings['csecret']},
                              headers=self.settings['header'])
            self.credentials = r.json()

    def refresh_authorization(self, refresh_token):
        """
        The oauth flow in general is outside the scope of what this lib wants to provide, but it does at least provide assistance in refreshing access tokens.

        :param refresh_token: your refresh token
        :return: a dictionary consisting of: access_token, token_type, expires, expires_in or None to indicate an error
        """
        r = requests.post(self.settings['apiurl'] + "/auth/access_token",
                          params={'grant_type': 'refresh_token', 'client_id': self.settings['cid'],
                                  'client_secret': self.settings['csecret'], 'refresh_tokne': refresh_token},
                          headers=self.settings['header'])
        if r.status_code == 200:
            return r.json()
        else:
            return None