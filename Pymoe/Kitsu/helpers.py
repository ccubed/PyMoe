import requests


class SearchWrapper(list):
    """
        :ivar _url str: Link to the next set of results
        :ivar header dict: Headers needed for API calls
    """
    def __init__(self, data, link, headers):
        """
        Initialize a new SearchWrapper. This is an API aware iterator that subclasses list.
        
        :param data: The first set of results populates our list at initilization 
        :param link: the link to the next set of results
        :param headers: a dictionary of necessary headers on each API call
        """
        super().__init__(data)
        self._url = link
        self.header = headers

    def __iter__(self):
        return self

    def __next__(self):
        if self.__len__():
            return self.pop()
        else:
            if self._url is None:
                raise StopIteration
            else:
                r = requests.get(self._url, headers=self.header)

                if r.status_code != 200:
                    raise StopIteration
                else:
                    jsd = r.json()

                    if 'next' in jsd['links']:
                        self._url = jsd['links']['next']
                    else:
                        self._url = None

                    self.extend(jsd['data'])
                    return self.pop()

    def next(self):
        """
        This is simply an alias for __next__. Included for compatibility and ease of use.
        
        :return: the next result 
        """
        return self.__next__()
