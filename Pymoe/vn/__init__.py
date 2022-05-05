import re
import ujson
import pymoe.vn.connection
from pymoe.vn.get import *
from pymoe.vn.search import *
from pymoe.errors import serverError
from pymoe.helpers import vndbWrapper

helperpat = re.compile('[=|!=|~|>|>=|<=|<]')
stypes = ['vn', 'release', 'producer', 'character', 'votelist', 'vnlist', 'wishlist']

def manualGet(stype: str, flags, filters: str, options: dict = None):
    """
        Send a request to the API to return results related to Visual Novels. 
        This is for power users as it allows complete control over the command.

        :param str stype: What are we searching for? One of: vn, release, producer, character, votelist, vnlist, wishlist
        :param flags: See the D11 docs. A comma separated list of flags for what data to return. Can be list or str.
        :param str filters: A string with the one filter to search by (apparently you only get one).
                            This is kind of special. You need to pass them in the form <filter><op>"<term>"
                            for strings or <filter><op><number> for numbers. This is counter intuitive.
                            Also, per the docs, <filter>=<number> doesn't do what we think, use >, >= or < and <=.
                            I will attempt to properly format this if not done so when called.
        :param dict options: A dictionary of options to customize the search by. Optional, defaults to None.
        :return dict: A dictionary containing a pages and data key. data contains a list of dictionaries with data on your results. If pages is true, you can call this command again with the same parameters and pass a page option to get more data. Otherwise no further results exist for this query.
        :raises ServerError: Raises a ServerError if an error is returned.
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

    if stype not in stypes:
        raise SyntaxError("{} not a valid Search type.".format(stype))

    if '"' not in filters or "'" not in filters:
        newfilters = helperpat.split(filters)
        newfilters = [x.strip() for x in newfilters]
        newfilters[1] = '"' + newfilters[1] + '"'
        op = helperpat.search(filters)
        newfilters = op.group(0).join(newfilters)
        command = '{} {} ({}){}'.format(
            stype,
            finflags,
            newfilters,
            ' ' + ujson.dumps(options) if options is not None else ''
        )
    else:
        command = '{} {} ({}){}'.format(
            stype,
            finflags,
            filters,
            ' ' + ujson.dumps(options) if options is not None else ''
        )

    data = pymoe.vn.connection.mySock.send_command('get', command)

    if 'id' in data:
        raise serverError(data['msg'], data['id'])
    else:
        return vndbWrapper(
            data['items'],
            pymoe.vn.connection.mySock,
            2 if 'more' in data else None,
            command
        )


