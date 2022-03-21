import requests

def whatSeason(month : int):
    """
        TODO: Write This
    """
    if month in [12,1,2]:
        return "winter"
    elif month in [3,4,5]:
        return "spring"
    elif month in [6,7,8]:
        return "summer"
    else:
        return "fall"

#class SearchWrapper(list):
#    """
#        :ivar _url str: Link to the next set of results
#        :ivar header dict: Headers needed for API calls
#    """
#    def __init__(self, data : list, link : str, headers : dict):
#        """
#        Initialize a new SearchWrapper. This is an API aware iterator that subclasses list.
#
#        :param data list: The first set of results populates our list at initilization
#        :param link str: the link to the next set of results
#        :param headers dict: a dictionary of necessary headers on each API call
#        """
#        super().__init__(data)
#        self._url = link
#        self.header = headers
#
#    def __iter__(self):
#        return self
#
#    def __next__(self):
#        if self.__len__():
#            return self.pop()
#        else:
#            if self._url is None:
#                raise StopIteration
#            else:
#                r = requests.get(self._url, headers=self.header)
#
#                if r.status_code != 200:
#                    raise StopIteration
#                else:
#                    jsd = r.json()
#
#                    if not self.which: # 0 is Anilist
#                        pass
#                    elif self.which = 1: # 1 is Kitsu
#                        self._url = jsd['links']['next'] if 'next' in jsd['links'] else None
#                    elif self.which = 2: # 2 is MAL
#                        pass
#
#                    self.extend(jsd['data'])
#                    return self.pop()
