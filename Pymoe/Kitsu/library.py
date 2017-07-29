import requests
from ..errors import *
from .helpers import SearchWrapper

class KitsuLib:
    def __init__(self, api, header):
        self.apiurl = api
        self.header = header

    def get(self, uid):
        """
        Get a user's list of library entries. This is a little annoying.
        The list of Library Entries by default doesn't name the item it relates
        to. Here's the other problem, it lists a relationship to all three
        types of items. And there's no indication of which type of item it is.
        I have no idea how to handle this and there's no way you can just make
        hundreds (and with some people thousands) of calls to see if it returns
        Null for the given item or until you get data back. Good Luck I guess.

        :param uid str: User ID to get library entries for
        :return: Results or ServerError
        :rtype: SearchWrapper or Exception
        """
        r = requests.get(self.apiurl + "/users/{}/library-entries".format(uid), headers=self.header)

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
