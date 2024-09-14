import requests
import ujson

from pymoe.utils.errors import serializationFailed, serverError


def base36Decode(number: str):
    """
    This is a utility function for MangaUpdates.
    This function will convert a Base 36 ID to an ID that can be used with the API.
    The search functions return only the right IDs, but if you take an ID from the website that would need to be run through here.
    Given https://www.mangaupdates.com/series/z5e3xwc/raising-my-fiance-with-money, z5e3xwc is not a valid API id.
    This function would return 76513411164 which is the right ID for this series in the API.

    :param number: The Base 36 Encoded ID to be Decoded
    """
    return int(number, 36)


def whatSeason(month: int):
    """
    Given a month, return which anime season it falls in.

    :param month int: What month is it?
    """
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    else:
        return "fall"


class searchWrapper(list):
    """
    This is an API aware iterator that subclasses list.

    :ivar _url: Link to the next set of results
    :ivar header: Headers needed for API calls
    """

    def __init__(self, data: list, link: str, headers: dict):
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


class mangaupdatesWrapper(searchWrapper):
    """
    This is an API aware iterator that subclasses list. This is for MangaUpdates.

    :ivar _url: Link to the next set of results
    :ivar header: Headers needed for API calls
    """

    def __init__(self, data: list, link: str, headers: dict, json_data: dict, pages: int):
        """
        Initialize a new SearchWrapper. This is an API aware iterator that subclasses list.

        :param data: The first set of results populates our list at initilization
        :param link: the link to the next set of results
        :param headers: a dictionary of necessary headers on each API call
        :param json_data: A dictionary of data to send on each request
        :param pages: Total number of pages
        """
        super().__init__(data, link, headers)
        self.data = json_data
        self.data["page"] += 1
        self.totalPages = pages

    def __next__(self):
        if self.__len__():
            return self.pop()
        else:
            if self._url is None:
                raise StopIteration
            else:
                r = requests.post(self._url, headers=self.header, data=self.data)

                if r.status_code != 200:
                    raise serverError(r.text, r.status_code)

                try:
                    jsd = ujson.loads(r.text)
                except ValueError:
                    raise serializationFailed(r.text, r.status_code)
                else:
                    if (self.data["page"] + 1) <= self.totalPages:
                        self.data["page"] += 1
                    else:
                        self._url = None
                    self.extend(jsd["results"])

                return self.pop()


class kitsuWrapper(searchWrapper):
    """
    This is an API aware iterator that subclasses list. This is for Kitsu.

    :ivar _url: Link to the next set of results
    :ivar header: Headers needed for API calls
    """

    def __init__(self, data: list, link: str, headers: dict):
        """
        Initialize a new SearchWrapper. This is an API aware iterator that subclasses list.

        :param data: The first set of results populates our list at initilization
        :param link: the link to the next set of results
        :param headers: a dictionary of necessary headers on each API call
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
                    jsd = ujson.loads(r.text)

                self._url = jsd["links"]["next"] if "next" in jsd["links"] else None

                self.extend(jsd["data"])
                return self.pop()


class malWrapper(searchWrapper):
    """
    This is an API aware iterator that subclasses list. This is for MAL.

    :ivar _url: Link to the next set of results
    :ivar header: Headers needed for API calls
    """

    def __init__(self, data: list, link: str, headers: dict):
        """
        Initialize a new SearchWrapper. This is an API aware iterator that subclasses list.

        :param data: The first set of results populates our list at initilization
        :param link: the link to the next set of results
        :param headers: a dictionary of necessary headers on each API call
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
                    jsd = ujson.loads(r.text)

                self._url = jsd["paging"]["next"] if "next" in jsd["paging"] else None

                self.extend(jsd["data"])
                return self.pop()


class anilistWrapper(list):
    """
    This is a search wrapper for anilist.
    It does not inherit from the subclass of SearchWrapper because the GraphQL interface is too different from the other apis.

    :ivar json: The JSON Parameters to send with the request
    :ivar header: The Headers to send with the request
    :ivar base_url: The base API Url
    :ivar isNext: Simple switch for denoting no more results
    """

    def __init__(self, data: list, json: dict, headers: dict, base_url: str):
        """
        Initialize a new SearchWrapper. This is an API aware iterator that subclasses list.

        :param data list: The first set of results populates our list at initilization
        :param json: The JSON Parameters to send with the request
        :param headers: The Headers to send with the request
        :param base_url: The base API Url
        """
        super().__init__(data)
        self.json = json
        self.json["variables"]["page"] += 1
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
                r = requests.post(self.base_url, headers=self.header, json=self.json)

                try:
                    jsd = ujson.loads(r.text)
                except ValueError:
                    raise serializationFailed(r.text, r.status_code)
                else:
                    if "errors" in jsd:
                        raise serverError(r.text, r.status_code)
                    else:
                        self.extend(
                            jsd["data"]["Page"][list(jsd["data"]["Page"].keys())[1]]
                        )

                    if jsd["data"]["Page"]["pageInfo"]["hasNextPage"]:
                        self.json["variables"]["page"] += 1
                    else:
                        self.isNext = False

                return self.pop()
