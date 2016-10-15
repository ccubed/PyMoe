Hummingbird
===========

The Hummingbird class exposes itself through three interfaces: anime, user, library. These interfaces provide all functionality available in the Hummingbird API.

Anime Interface
---------------

.. py:function:: id(aid : int, title=None)

    Search Anime by ID. The first parameter should be the Anime's ID. The second parameter specifies the title_language_preference option and defaults to None. The options are canonical, english or romanized.

.. py:function:: v2(clientid : string, kwargs)

    This searches Anime against the V2 Anime endpoint. This endpoint requires you to register for a Client ID on Hummingbird. You should pass that as the first parameter. Additionally, you should pass one of id or malid, but only one. Where id is the ID of the anime and malid is the anime's MAL id. The IDs should be ints.

.. py:function:: search(term : string)

    Search Anime by the term given.

User Interface
--------------

.. py:function:: authenticate(password : string, kwargs)

    Authenticate and login as the specified user. Returns the oauth token for that user. The first parameter is the user's password. You should additionally pass one and only one of username or email which are also strings.

.. py:function:: info(user : string)

    Get details about the given user. This returns the information available at /users/{user} as a dictionary.

.. py:function:: feed(user : string)

    Get a user's feed. Return a list of dictionaries which contain the data from the returned Story Objects.

.. py:function:: favorite_anime(user : string)

    Get a user's favorite anime. Return a list of anime object dictionaries.

Library Interface
-----------------

.. py:function:: get(user : string, status : string = None)

    Get a user's Anime list. Status is an optional parameter that defines which specific list you want. Status is one of: currently-watching, plan-to-watch, completed, on-hold or dropped

.. py:function:: set(aid : int, auth_token : string, kwargs)

    Add an anime to a user's list or update it. The first parameter is the id of the anime, The second parameter is the auth_token obtained from authorizing as the user. There are many kwargs.

    - status: currently-watching, plan-to-watch, completed, on-hold, dropped
    - privacy: public or private
    - rating: 0, 0.5, 1, 1.5 ... 5. Setting it to 0 or the current value will remove it
    - sane_rating_update: See above. Except with this one only setting it to 0 removes it.
    - rewatching: true or false (This is a str, not a bool)
    - rewatched_times: # of times rewatched
    - notes: Personal Notes
    - episodes_watched: Number of episodes watched. Between 0 and total_episodes. If equal to total_episodes, you must set status to complete or you'll get 500'd.
    - increment_episodes: If set to true will increment episodes_watched by 1. If used along with episodes_watched, will increment that value by 1. (this is a str, not a bool)

.. py:function:: remove(aid : int, auth_token : string)

    Remove an Anime from a user's list.