MyAnimeList
===========
This module, named Mal, encapsulates and abstracts EVERYTHING. This means two things. One, it takes some getting used to. Two, once you get used to it, it's the greatest thing since sliced bread. The major encapsulations here are Anime and Manga, but many smaller ones exist.

Encapsulations
--------------
These have their very own document located at :doc:`MAL Encapsulations<malencap>`. Read there for an explanation of what each one holds.

Basic Operation
---------------
You will interface with the Mal functions only through the Anime and Manga abstractions. These exist as a way to make it easier on the programmer to update values and for the system to build necessary XML statements for the server. Anime and Manga share the same operations (Asides from stylistic differences like read versus watched, which are the same as the website).
There are four main operations you can perform on the anime and manga fields of a Mal object. Please note that you must pass a username and password upon object instantation, since the API requires it for every call.

.. py:function:: search(term : string)

    Search for a given term within Anime or Manga.

.. py:function:: add(item)

    Where item is an instance of PyMoe.Mal.Objects.Anime or PyMoe.Mal.Objects.Manga, this will add the given Anime or Manga to the user's list with the given parameters.

.. py:function:: update(item)

    Where item is an instance of PyMoe.Mal.Objects.Anime or PyMoe.Mal.Objects.Manga, this will update the given Anime or Manga on the user's list with the new data.

.. py:function:: delete(item)

    Where item is an instance of PyMoe.Mal.Objects.Anime or PyMoe.Mal.Objects.Manga, this will remove the given Anime or Manga from a user's list.

Users
-----
PyMoe's MyAnimeList implementation does support grabbing user profiles. Rather than separating this into different calls, this makes two requests and returns to you an ecapsulated user object that includes user stats and a full anime and manga list. This can be slow, but it's two requests and then parsing a giant glob of XML data. I've tried to make it as fast as possible and on some users with smaller lists it's in the microseconds. On larger users it can take seconds. I'll look at ways to speed it up. But the biggest bottleneck here is not having one API to call for both lists.

.. py:function:: user(name : string)

    Given a proper username, retrieve a user's watched statistics and their full anime and manga data inside an encapsulated user object.

    The user endpoint does not have average score data available for any anime or manga. It only has the user score data available. The average scores will be populated with None.

Encapsulations Again
--------------------
You should probably go read :doc:`MAL Encapsulations<malencap>` now. These encapsulations are very important to the way PyMoe works and having a good knowledge of them will allow you to do impressive things within PyMoe. What you ask?

- Use list comprehension to build a list of currently watching anime on a user's list
- Get anime with a score of 5 or more
- Use list comprehension to build a list of anime that begin with A in a user's list
- Use any to test if a user has even bothered to rate anime/manga ever