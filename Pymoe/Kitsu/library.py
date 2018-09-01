import requests
from ..errors import *
from .helpers import SearchWrapper

class KitsuLib:
    def __init__(self, api, header):
        self.apiurl = api
        self.header = header

    def get(self, uid, filters=None):
        """
        Get a user's list of library entries. While individual entries on this
        list don't show what type of entry it is, you can use the filters provided
        by the Kitsu API to only select which ones you want

        :param uid: str: User ID to get library entries for
        :param filters: dict: Dictionary of filters for the library
        :return: Results or ServerError
        :rtype: SearchWrapper or Exception
        """
        filters = self.__format_filters(filters)

        r = requests.get(self.apiurl + "/users/{}/library-entries".format(uid), headers=self.header, params=filters)

        if r.status_code != 200:
            raise ServerError

        jsd = r.json()

        if jsd['meta']['count']:
            return SearchWrapper(jsd['data'], jsd['links']['next'] if 'next' in jsd['links'] else None, self.header)
        else:
            return None

    def create(self, user_id, media_id, item_type, token, data):
        """
        Create a library entry for a user. data should be just the attributes.
        Data at least needs a status and progress.

        :param user_id str: User ID that this Library Entry is for
        :param media_id str: ID for the media this entry relates to
        :param item_type str: anime, drama or manga depending
        :param token str: OAuth token for user
        :param data dict: Dictionary of attributes for the entry
        :return: New Entry ID or ServerError
        :rtype: Str or Exception
        """
        final_dict = {
            "data": {
                "type": "libraryEntries",
                "attributes": data,
                "relationships":{
                    "user":{
                        "data":{
                            "id": user_id,
                            "type": "users"
                        }
                    },
                    "media":{
                        "data":{
                            "id": media_id,
                            "type": item_type
                        }
                    }
                }
            }
        }
        final_headers = self.header
        final_headers['Authorization'] = "Bearer {}".format(token)

        r = requests.post(self.apiurl + "/library-entries", json=final_dict, headers=final_headers)

        if r.status_code != 201:
            raise ConnectionError(r.text)

        jsd = r.json()

        return jsd['data']['id']

    def update(self, eid, data, token):
        """
        Update a given Library Entry.

        :param eid str: Entry ID
        :param data dict: Attributes
        :param token str: OAuth token
        :return: True or ServerError
        :rtype: Bool or Exception
        """
        final_dict = {"data": {"id": eid, "type": "libraryEntries", "attributes": data}}
        final_headers = self.header
        final_headers['Authorization'] = "Bearer {}".format(token)

        r = requests.patch(self.apiurl + "/library-entries/{}".format(eid), json=final_dict, headers=final_headers)

        if r.status_code != 200:
            raise ConnectionError(r.text)

        return True

    def delete(self, eid, token):
        """
        Delete a library entry.

        :param eid str: Entry ID
        :param token str: OAuth Token
        :return: True or ServerError
        :rtype: Bool or Exception
        """
        final_headers = self.header
        final_headers['Authorization'] = "Bearer {}".format(token)

        r = requests.delete(self.apiurl + "/library-entries/{}".format(eid), headers=final_headers)

        if r.status_code != 204:
            print(r.status_code)
            raise ConnectionError(r.text)

        return True

    @staticmethod
    def __format_filters(filters):
        """
        Format filters for the api query (to filter[<filter-name>])

        :param filters: dict: can be None, filters for the query
        :return: the formatted filters, or None
        """
        if filters is not None:
            for k in filters:
                if 'filter[' not in k:
                    filters['filter[{}]'.format(k)] = filters.pop(k)
        return filters
