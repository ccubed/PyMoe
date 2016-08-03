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
        self.stypes = ['vn', 'release', 'producer', 'character', 'votelist', 'vnlist', 'wishlist']

    def dbstats(self):
        """
        Get the dbstats

        :return: A dictionary containing the db stats.
        """
        return self.connection.send_command('dbstats')

    def get(self, stype, flags, filters, options=None):
        """
        Send a request to the API to return results related to Visual Novels.

        :param str stype: What are we searching for? One of: vn, release, producer, character, votelist, vnlist, wishlist
        :param flags: See the D11 docs. A comma separated list of flags for what data to return. Can be list or str.
        :param str filters: A string with the one filter to search by (apparently you only get one).
                            This is kind of special. You need to pass them in the form <filter><op>"<term>"
                            for strings or <filter><op><number> for numbers. This is counter intuitive.
                            Also, per the docs, <filter>=<number> doesn't do what we think, use >, >= or < and <=.
                            I will attempt to properly format this if not done so when called.
        :param dict options: A dictionary of options to customize the search by. Optional, defaults to None.
        :return dict: A dictionary containing a pages and data key. data contains a list of dictionaries with data on your results. If pages is true, you can call this command again with the same parameters and pass a page option to get more data. Otherwise no further results exist for this query.
        """
        if not isinstance(flags, str):
            if isinstance(flags, list):
                finflags = ",".join(flags)
            else:
                raise SyntaxError("Flags should be a list or comma separated string")
        else:
            finflags = flags
        if not isinstance(filters, str):
            raise SyntaxError("Filters needs to be a string in the format Filter<op>Value. The simplest form is search=\"<Term>\".")
        if stype not in self.stypes:
            raise SyntaxError("{} not a valid Search type.".format(stype))
        if '"' not in filters or "'" not in filters:
            newfilters = self.helperpat.split(filters)
            newfilters = [x.strip() for x in newfilters]
            newfilters[1] = '"' + newfilters[1] + '"'
            op = self.helperpat.search(filters)
            newfilters = op.group(0).join(newfilters)
            command = '{} {} ({}){}'.format(stype, finflags, newfilters,
                                            ' ' + ujson.dumps(options) if options is not None else '')
        else:
            command = '{} {} ({}){}'.format(stype, finflags, filters,
                                            ' ' + ujson.dumps(options) if options is not None else '')
        data = self.connection.send_command('get', command)
        pages = False
        if data['more']:
            pages = True
        return {'pages': pages, 'data': data['items']}
