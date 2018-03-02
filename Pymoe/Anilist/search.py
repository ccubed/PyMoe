import json
import requests


class ASearch:
    def __init__(self, settings):
        self.settings = settings

    def character(self, term, page = 1, perpage = 3):
        """
        Search for a character by term.
        Results are paginated by default. Page specifies which page we're on.
        Perpage specifies how many per page to request. 3 is just the example from the API docs.
        
        :param term str: Name to search by
        :param page int: Which page are we requesting? Starts at 1.
        :param perpage int: How many results per page are we requesting?
        :return: Json object with returned results.
        :rtype: Json object with returned results.
        """
        query_string = """\
            query ($query: String, $page: Int, $perpage: Int) {
                Page (page: $page, perPage: $perpage) {
                    pageInfo {
                        total
                        currentPage
                        lastPage
                        hasNextPage
                    }
                    characters (search: $query) {
                        id
                        name {
                            first
                            last
                        }
                        image {
                            large
                        }
                    }
                }
            }
        """
        vars = {"query": term, "page": page, "perpage": perpage}
        r = requests.post(self.settings['apiurl'],
                          headers=self.settings['header'],
                          json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd
                    
    def anime(self, term, page = 1, perpage = 3):
        """
        Search for an anime by term.
        Results are paginated by default. Page specifies which page we're on.
        Perpage specifies how many per page to request. 3 is just the example from the API docs.
        
        :param term str: Name to search by
        :param page int: Which page are we requesting? starts at 1.
        :param perpage int: How many results per page? defaults to 3.
        :return: List of dictionaries which are anime objects or None
        :rtype: list of dict or NoneType
        """
        query_string = """\
            query ($query: String, $page: Int, $perpage: Int) {
                Page (page: $page, perPage: $perpage) {
                    pageInfo {
                        total
                        currentPage
                        lastPage
                        hasNextPage
                    }
                    media (search: $query, type: ANIME) {
                        id
                        title {
                            romaji
                            english
                        }
                        coverImage {
                            large
                        }
                        averageScore
                        popularity
                        episodes
                        season
                        hashtag
                        isAdult
                    }
                }
            }
        """
        vars = {"query": term, "page": page, "perpage": perpage}
        r = requests.post(self.settings['apiurl'],
                          headers=self.settings['header'],
                          json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd

    def manga(self, term, page = 1, perpage = 3):
        """
        Search for a manga by term.
        Results are paginated by default. Page specifies which page we're on.
        Perpage specifies how many per page to request. 3 is just the example from the API docs.
        
        :param term str: Name to search by
        :param page int: Which page are we requesting? Starts at 1.
        :param perpage int: How many results per page? defaults to 3.
        :return: List of dictionaries which are manga objects or None
        :rtype: list of dict or NoneType
        """
        query_string = """\
            query ($query: String, $page: Int, $perpage: Int) {
                Page (page: $page, perPage: $perpage) {
                    pageInfo {
                        total
                        currentPage
                        lastPage
                        hasNextPage
                    }
                    media (search: $query, type: ANIME) {
                        id
                        title {
                            romaji
                            english
                        }
                        coverImage {
                            large
                        }
                        averageScore
                        popularity
                        episodes
                        season
                        hashtag
                        isAdult
                    }
                }
            }
        """
        vars = {"query": term, "page": page, "perpage": perpage}
        r = requests.post(self.settings['apiurl'],
                          headers=self.settings['header'],
                          json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd
                    
    def staff(self, term, page = 1, perpage = 3):
        """
        Search for staff by term. Staff means actors, directors, etc.
        Results are paginated by default. Page specifies which page we're on.
        Perpage specifies how many per page to request. 3 is just the example from the API docs.
        
        :param term str: Name to search by
        :param page int: What page are we requesting? Starts at 1.
        :param perpage int: How many results per page? Defaults to 3.
        :return: List of dictionaries which are staff objects or None
        :rtype: list of dict or NoneType
        """
        query_string = """\
            query ($query: String, $page: Int, $perpage: Int) {
                Page (page: $page, perPage: $perpage) {
                    pageInfo {
                        total
                        currentPage
                        lastPage
                        hasNextPage
                    }
                    staff (search: $query) {
                        id
                        name {
                            first
                            last
                        }
                        image {
                            large
                        }
                    }
                }
            }
        """
        vars = {"query": term, "page": page, "perpage": perpage}
        r = requests.post(self.settings['apiurl'],
                          headers=self.settings['header'],
                          json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd
                    
    def studio(self, term, page = 1, perpage = 3):
        """
        Search for a studio by term.
        Results are paginated by default. Page specifies which page we're on.
        Perpage specifies how many per page to request. 3 is just the example from the API docs.
        
        :param term str: Name to search by
        :param page int: What page are we requesting? starts at 1.
        :param perpage int: How many results per page? defaults to 3.
        :return: List of dictionaries which are studio objects or None
        :rtype: list of dict or NoneType
        """
        query_string = """\
            query ($query: String, $page: Int, $perpage: Int) {
                Page (page: $page, perPage: $perpage) {
                    pageInfo {
                        total
                        currentPage
                        lastPage
                        hasNextPage
                    }
                    studios (search: $query) {
                        id
                        name
                    }
                }
            }
        """
        vars = {"query": term, "page": page, "perpage": perpage}
        r = requests.post(self.settings['apiurl'],
                          headers=self.settings['header'],
                          json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd
