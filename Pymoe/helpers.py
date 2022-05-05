import requests
import ujson
from pymoe.errors import serializationFailed, serverError

def whatSeason(month : int):
    """
        Given a month, return which anime season it falls in.

        :param month int: What month is it?
    """
    if month in [12,1,2]:
        return "winter"
    elif month in [3,4,5]:
        return "spring"
    elif month in [6,7,8]:
        return "summer"
    else:
        return "fall"

class searchWrapper(list):
    """
        :ivar _url str: Link to the next set of results
        :ivar header dict: Headers needed for API calls
    """
    def __init__(self, data: list, link: str, headers: dict):
        """
        Initialize a new SearchWrapper. This is an API aware iterator that subclasses list.

        :param data list: The first set of results populates our list at initilization
        :param link str: the link to the next set of results
        :param headers dict: a dictionary of necessary headers on each API call
        """
        super().__init__(data)
        self._url = link
        self.header = headers

    def __iter__(self):
        return self

class kitsuWrapper(searchWrapper):
    """
        :ivar _url str: Link to the next set of results
        :ivar header dict: Headers needed for API calls
    """
    def __init__(self, data: list, link: str, headers: dict):
        """
        Initialize a new SearchWrapper. This is an API aware iterator that subclasses list.

        :param data list: The first set of results populates our list at initilization
        :param link str: the link to the next set of results
        :param headers dict: a dictionary of necessary headers on each API call
        """
        super().__init__(data, link, headers)

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


                self._url = jsd['links']['next'] if 'next' in jsd['links'] else None


                self.extend(jsd['data'])
                return self.pop()

class malWrapper(searchWrapper):
    """
        :ivar _url str: Link to the next set of results
        :ivar header dict: Headers needed for API calls
    """
    def __init__(self, data: list, link: str, headers: dict):
        """
        Initialize a new SearchWrapper. This is an API aware iterator that subclasses list.

        :param data list: The first set of results populates our list at initilization
        :param link str: the link to the next set of results
        :param headers dict: a dictionary of necessary headers on each API call
        """
        super().__init__(data, link, headers)

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


                self._url = jsd['paging']['next'] if 'next' in jsd['paging'] else None


                self.extend(jsd['data'])
                return self.pop()

class anilistWrapper(list):
    """
        This is a search wrapper for anilist. It does not inherit from the subclass of SearchWrapper because the GraphQL interface is too different from the other apis.

        :ivar _url str: Link to the next set of results
        :ivar header dict: Headers needed for API calls
    """
    def __init__(self, data: list, json: dict, headers: dict, base_url: str):
        """
        Initialize a new SearchWrapper. This is an API aware iterator that subclasses list.

        :param data list: The first set of results populates our list at initilization
        :param link str: the link to the next set of results
        :param headers dict: a dictionary of necessary headers on each API call
        """
        super().__init__(data)
        self.json = json
        self.json['variables']['page'] += 1
        self.header = headers
        self.base_url = base_url
        self.isNext = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.__len__():
            return self.pop()
        else:
            if not self.isNext:
                raise StopIteration
            else:
                r = requests.post(
                    self.base_url,
                    headers = self.header,
                    json = self.json
                )

                try:
                    jsd = ujson.loads(r.text)
                except ValueError:
                    raise serializationFailed(r.text, r.status_code)
                else:
                    if 'errors' in jsd:
                        raise serverError(r.text, r.status_code)
                    else:
                        self.extend(jsd['data']['Page'][list(jsd['data']['Page'].keys())[1]])
                
                if jsd['data']['Page']['pageInfo']['hasNextPage']:
                    self.isNext = 1
                    self.json['variables']['page'] += 1
                else:
                    self.isNext = 0

                return self.pop()

class vndbWrapper(list):
    """
        This is a search wrapper for VNDB. It does not inherit from the subclass of SearchWrapper because the interface is too different from the other apis.

        :ivar sock: The socket reference
        :ivar page: The next page
        :ivar command: The command
    """
    def __init__(self, theData: list, theSocket, thePage: int | None, theCommand: str):
        super.__init__(theData)
        self.sock = theSocket
        self.page = thePage
        self.command = theCommand

    def __iter__(self):
        return self

    def __next__(self):
        if self.__len__():
            return self.pop()
        else:
            if not self.page:
                raise StopIteration
            else:
                data = self.sock.send_command(self.command + ' ' + ujson.dumps({'page': self.page}))

                if data['more']:
                    self.page += 1
                else:
                    self.page = None

                self.extend(data['items'])
