[![Documentation Status](https://readthedocs.org/projects/pymoe/badge/?version=latest)](http://pymoe.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/ccubed/PyMoe.svg?branch=master)](https://travis-ci.org/ccubed/PyMoe)
# PyMoe
Welcome to PyMoe, the only python lib you'll ever need if you need the animu/mangu on the python platform.
## 1.0
This brings us to 1.0. A stable release for Pymoe. It supports the majority of my end goal websites and it has some good interfaces. This is a breaking change, thus the major bump.
I cannot stress enough that you should not update unless you have taken the time to read through and note the differences. There are several.
## 1.0.4
This fixes anilist. If you don't have this, anilist won't work.

## Kitsu
Kitsu is the new Hummingbird if you're wondering where Hummingbird went.
To create an instance do:
```python
from Pymoe import Kitsu
instance = Kitsu(client_id, client_secret)
```
You can get the client_id and client_secret off the forums. There's only one.
You have six interfaces: anime, manga, drama, auth, user, library
```python
instance.anime.get(id)  # Search anime by ID
instance.anime.search(term)  # Search anime by term
instance.manga.get(id)  # Search manga by ID
instance.manga.search(term)  # Search manga by term
instance.drama.get(id)  # Search drama by ID
instance.drama.search(term)  # Search drama by term
instance.auth.authenticate(username, password)  # Authenticate through oauth
instance.user.search(term)  # Search for users by name
instance.user.get(id)  # Search for user by ID
instance.user.update(id, dictionary, token)  # Update a user's attributes
instance.user.create(dictionary)  # Create a new user. I haven't tested this. Let me know how it works.
instance.library.get(id)  # Get a user's library entries (lol, see source notes)
```
Now supports mappings thanks to [Luna](https://github.com/ileyd)
```python
instance.mappings.get("myanimelist/anime", 31608) # return the anime object for Teekyuu 4 specials
```

## Anidb
Status: Not Started

## Anilist
To create an instance do:
```python
from Pymoe import Anilist
instance = Anilist()
```
From there you can get information from Anilist using their new GraphQL API using the old format.
For example, to get data on a known ID.
```python
instance.get.anime(21610) # Return data on Okusama ga Seitokaichou
instance.get.manga(64127) # Return data on Mahouka Koukou no Rettousei
instance.get.staff(121963) # Return data on Keisuke Nishijima (Nisizima)
instance.get.studio(94) # Return data on Telecom Animation Film
instance.get.review(2113, False) # Return review #2113 (A review on Orange) and don't format the review body in HTML
instance.get.review(2113) # Return review #2113 and format the review body in HTML
```
Searching is also making a return.
```python
instance.search.anime("King") # Anime search results for King.
instance.search.manga("King") # Manga search results for King.
instance.search.character("Kei") # Character search results for Kei.
instance.search.staff("Keisuke") # Staff search results for Keisuke.
instance.search.studio("Ghibli") # Studio search result for Ghibli. (There's only one)
```
A note about the searching. Each search function now has the signature:
```python
search(term, page = 1, perpage = 3)
```
Pagination is done automatically in the new API. I take care of that. By default you'll get 3 results per page. 
If you want more, just change the perpage value. pageInfo is always the first result in the returned data.
Pages start at 1 and if you want another page, just replace page with the next number. 

## Bakatsuki
To create an instance do:
```python
from Pymoe import Bakatsuki
instance = Bakatsuki()
```
From there you can get information on Bakatsuki's projects.
```python
instance.active()  # Return a tuple containing (title, pageid) of active projects
instance.chapters(title)  # return the chapters for a title
instance.get_text(title)  # return the text of a given page
instance.light_novels(language)  # Get a list of language's light novels
instance.teaser(language)  # Get a list of language's teaser projects
instance.web_novels(language)  # Get a list of language's web novels
```

## Mal - Currently Disabled 
### NOTE
Documentation remains here in case it's useful later, but for now the public API on My Anime List has been shut down.
Per Site Owners, It will not come back up until V2 of the API which has no ETA.
### This is only an archive, this does not work
To create an instance.
```python
from Pymoe import Mal
instance = Mal(username, password)  # Since every endpoint requires authentication, username/password isn't optional
```
This particular branch relies on a ton of abstractions and encapsulations. You should read up on them. However, ultimately, it makes your life as a programmer easier. Anime and Manga share the same 4 functions: search, add, update, delete.
```python
instance.anime.search(term)  # Return a list of Anime objects, sorted by status
instance.anime.search(term).completed # Example of getting completed anime
instance.manga.search(term)  # Return a list of Manga objects
instance.manga.search(term).publishing # Get currently publishing manga
instance.anime.update(Pymoe.Mal.Objects.Anime)  # Update a user's list with the given anime data
instance.manga.delete(Pymoe.Mal.Objects.Manga)  # Delete this manga from the user's list
instance.anime.add(Pymoe.Mal.Objects.Anime)  # Add the anime to the user's list
instance.user(username)  # Return a user object that contains user stats and a full anime, manga list
instance.user(username).anime.days # Return the number of days user has spent on anime
instance.user(username).anime.list.completed
instance.user(username).anime.list.watching
instance.user(username).anime.list.held
instance.user(username).anime.list.dropped
instance.user(username).anime.list.planned
instance.user(username).manga.days # return the number of days user has spent on manga
instance.user(username).manga.list.completed
instance.user(username).manga.list.reading
instance.user(username).manga.list.held
instance.user(username).manga.list.dropped
instance.user(username).manga.list.planned
```
### All these categories
Let me break it down. It uses the same categories as the MAL API, but as a refresher.
#### Anime Search
Airing, Finished, Unaired, Dropped, Planned
#### Manga Search
Publishing, Finished, Unpublished, Dropped, Planned
#### User Anime
Watching, Completed, Held, Dropped, Planned
#### User Manga
Reading, Completed, Held, Dropped, Planned

## VNDB
To create an instance.
```python
from Pymoe import Vndb
instance = Vndb(username, password)  # Username and password are optional, but allow you to login as a user
```
This allows you access to some of the VNDB database. Currently it's just the querying part.
```python
instance.dbstats()  # Return the list of Database stats as seen on the homepage
instance.get(stype, flags, filters, options)  # Query the DB. You have to read the VNDB API Docs and my Docs for this. No way around it. Their API is complicated.
instance.set(stype, sid, fields) # Modify the DB. See the API docs. This is for VNLists, Wishlists and Votelists.
```
