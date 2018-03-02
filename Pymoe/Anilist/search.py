import json
import requests


class ASearch:
    def __init__(self, settings):
        self.settings = settings

    def character(self, term):
        """
        Search for a character by term.
        
        :param term str: Name to search by
        :return: List of dictionaries which are character objects or None
        :rtype: list of dict or NoneType
        """
        r = requests.get(
                self.settings['apiurl'] + "/character/search/" + term.replace(' ', '%20'),
                params={'access_token': self.rl()}, 
                headers=self.settings['header']
            )
        
        jsd = r.text
        
        # AniList can return a newline for no results for some reason
        if jsd == '\n' or r.status_code == 404:
            return None
        else:
            jsd = json.loads(jsd)
            if 'error' in jsd:
                # it can also return a json error
                return None
            else:
                if len(jsd):
                    return jsd
                else:
                    # it can also return a blank list
                    return None
                    
    def anime(self, term):
        """
        Search for an anime by term.
        
        :param term str: Name to search by
        :return: List of dictionaries which are anime objects or None
        :rtype: list of dict or NoneType
        """
        r = requests.get(
                self.settings['apiurl'] + "/anime/search/" + term.replace(' ', '%20'),
                params={'access_token': self.rl()}, 
                headers=self.settings['header']
            )
        
        jsd = r.text
        
        # AniList can return a newline for no results for some reason
        if jsd == '\n' or r.status_code == 404:
            return None
        else:
            jsd = json.loads(jsd)
            if 'error' in jsd:
                # it can also return a json error
                return None
            else:
                if len(jsd):
                    return jsd
                else:
                    # it can also return a blank list
                    return None

    def manga(self, term):
        """
        Search for a manga by term.
        
        :param term str: Name to search by
        :return: List of dictionaries which are manga objects or None
        :rtype: list of dict or NoneType
        """
        r = requests.get(
                self.settings['apiurl'] + "/manga/search/" + term.replace(' ', '%20'),
                params={'access_token': self.rl()}, 
                headers=self.settings['header']
            )
        
        jsd = r.text
        
        # AniList can return a newline for no results for some reason
        if jsd == '\n' or r.status_code == 404:
            return None
        else:
            jsd = json.loads(jsd)
            if 'error' in jsd:
                # it can also return a json error
                return None
            else:
                if len(jsd):
                    return jsd
                else:
                    # it can also return a blank list
                    return None
                    
    def staff(self, term):
        """
        Search for staff by term. Staff means actors, directors, etc.
        
        :param term str: Name to search by
        :return: List of dictionaries which are staff objects or None
        :rtype: list of dict or NoneType
        """
        r = requests.get(
                self.settings['apiurl'] + "/staff/search/" + term.replace(' ', '%20'),
                params={'access_token': self.rl()}, 
                headers=self.settings['header']
            )
        
        jsd = r.text
        
        # AniList can return a newline for no results for some reason
        if jsd == '\n' or r.status_code == 404:
            return None
        else:
            jsd = json.loads(jsd)
            if 'error' in jsd:
                # it can also return a json error
                return None
            else:
                if len(jsd):
                    return jsd
                else:
                    # it can also return a blank list
                    return None
                    
    def studio(self, term):
        """
        Search for a studio by term.
        
        :param term str: Name to search by
        :return: List of dictionaries which are studio objects or None
        :rtype: list of dict or NoneType
        """
        r = requests.get(
                self.settings['apiurl'] + "/studio/search/" + term.replace(' ', '%20'),
                params={'access_token': self.rl()}, 
                headers=self.settings['header']
            )
        
        jsd = r.text
        
        # AniList can return a newline for no results for some reason
        if jsd == '\n' or r.status_code == 404:
            return None
        else:
            jsd = json.loads(jsd)
            if 'error' in jsd:
                # it can also return a json error
                return None
            else:
                if len(jsd):
                    return jsd
                else:
                    # it can also return a blank list
                    return None

