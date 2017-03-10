import re
from .connection import *


class VNDB:
    """
        Start up a vndb instance. This instance allows you to communicate with the VNDB d11 api. If you pass a username
        and password it will log you in as that user automatically. Since there can only be one user per connection,
        you will need to call this multiple times to log in as more than one user. However, this is possible.
        Simply create multiple instances. However, keep in mind that you can only ever have 10 connections per IP
        and 200 commands per 10 minutes per IP and 1 second of SQL time per minute per IP, so I doubt that multiple
        connections will be very fruitful.

        :param username: The username to log in as
        :param password: The password for that username
        :ivar VNDBConnection connection: The connection manager instance
        :ivar SRE_Pattern helperpat: Helps me properly build filters in get
        :ivar list stypes: Used for error checking in get
    """

    def __init__(self, username=None, password=None):
        self.connection = VNDBConnection(username, password)
        self.helperpat = re.compile('[=|!=|~|>|>=|<=|<]')
        self.stypes = {
            'vn': 'basic,details,anime,relations,tags,stats,screens',
            'release': 'basic,details,vn,producers',
            'producer': 'basic,details,relations',
            'character': 'basic,details,meas,traits,vns',
            'user': 'basic',
            'votelist': 'basic',
            'vnlist': 'basic',
            'wishlist': 'basic'
        }

    def dbstats(self):
        """
            Get the dbstats
            
            :return: A dictionary containing the db stats.
        """
        return self.connection.send_command('dbstats')

    def get(self, what, term, page=0):
        """
            Perform a get query based on a search string. By default, this will return all fields for the given type. IE: It has all flags enabled by default.
        
            :param what str: The type of thing to query against.
            :param term str: The name to find.
            :param page int: A page number to start on
        """
        if what not in self.stypes.keys():
            raise SyntaxError("Need to pass a valid type. Got {} but we only accept the following: {}.".format(what, self.stypes.keys()))
            
        if page:
            return self.connection.send_command("get vn {} ({}) {}".format(self.stypes[what], "title = {}".format(what), ujson.dumps(options)))
        else:
            return self.connection.send_command("get vn {} ({})".format(self.stypes[what], "title = {}".format(what)))
            
        
        
    def restrict(self, data, fields):
        """
        
            Given a data return from the api, remove all fields but the ones listed.
            
            :param data dict: A dictionary of the json data
            :param fields list: A list of fields that we want to have in the final dictionary
        
        """
        pass