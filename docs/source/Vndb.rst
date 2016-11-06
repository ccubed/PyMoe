Visual Novel DB
===============

This implementation allows you to access the VNDB D11 API. Have fun. It's going to require you to read the D11 Docs, this API isn't forgiving and I can't abstract it any further than I have. I've made as many utility functions and helpers as I could.

Interface
---------
The interface is done by initializing a connection with or without a username and password. If given, I'll log you in automatically and handle securing the connection. Afterwards, you can use dbstats to get a dictionary of dbstats like on the main page or get to query the db.

.. py:function:: dbstats

    Get the DBstats as seen on the front page. Returned in a dictionary.

.. py:function:: get(self, stype : string, flags : list or string, filters : string, options : dictionary = None)

    Send a request to the API to get results back. Stype should be one of vn, release, producer, character, votelist, vnlist or wishlist.

    flags is a comma separated list of items that should be returned. It can be a list or string.

    filters is odd. For strings it should be formatted <filter><op>"<term>" and for numbers <filter><op><number>. Also, per the docs, <filter>=<number> doesn't do what we think, so use anything else.

    Options is defined on the API docs, but if any of them are provided by way of the options Dictionary we will send them on with the request.

    .. py:exception:: ServerError(message, code)

        This will be raised on an error returned from the server.

.. py:function:: set(self, stype : string, sid : int, fields : dictionary )

    Send a request to the API to modify something in the database if logged in.

    Stype is what we're modifying. It can be one of: votelist, vnlist or wishlist.

    Sid is the ID of the thing we're changing.

    Fields is a dictionary containing the fields for that specific type and their new values.

    .. py:exception:: ServerError(message, code)

        This will be raised on an error returned from the server.

