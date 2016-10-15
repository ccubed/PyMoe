[![Documentation Status](https://readthedocs.org/projects/pymoe/badge/?version=latest)](http://pymoe.readthedocs.io/en/latest/?badge=latest)
# PyMoe
Welcome to PyMoe, the only python lib you'll ever need if you need the animu/mangu on the python platform.

## Hummingbird
Ready to use as of version 0.1.
To create an instance do:
```python
from Pymoe import Hummingbird
instance = Hummingbird()
```
You have three interfaces: anime, user, library.
```python
instance.anime.id(id)  # Search anime by ID
instance.anime.search(term)  # Search anime by term
instance.anime.v2(clientid, id)  # Search anime by the V2 endpoint
instance.user.authenticate(password, kwargs)  # Authenticate user for auth_token. Give either email or username
instance.user.favorite_anime(username)  # Grab a user's favorite anime
instance.user.feed(username)  # Get a user's feed
instance.user.info(username)  # Get user information
instance.library.get(username, status)  # Get a user's library entries. Status is an optional status type to filter against.
instance.library.remove(id, auth_token)  # Remove anime referred to by ID from the user's library.
instance.library.set(id, auth_token, kwargs)  # There are a lot of params here. Add the anime referred to by ID to the user's library.
```

## Anidb
Status: Not Started

## Anilist
Status: Not Started

## Bakatsuki
Status: Finished as of 0.2
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

## Mal
Status: Finished as of 0.3
To create an instance.
```python
from Pymoe import Mal
instance = Mal(username, password)  # Since every endpoint requires authentication, un/pw isn't optional
```
This particular branch relies on a ton of abstractions and encapsulations. You should read up on them. However, ultimately, it makes your life as a programmer easier. Anime and Manga share the same 4 functions: search, add, update, delete.
```python
instance.anime.search(term)  # Return a list of Anime objects
instance.manga.search(term)  # Return a list of Manga objects
instance.anime.update(Pymoe.Mal.Objects.Anime)  # Update a user's list with the given anime data
instance.manga.delete(Pymoe.Mal.Objects.Manga)  # Delete this manga from the user's list
instance.anime.add(Pymoe.Mal.Objects.Anime)  # Add the anime to the user's list
instance.user(username)  # Return a user object that contains user stats and a full anime, manga list
```

## VNDB
Status: Partially written as of 0.3. You can query the DB.
To create an instance.
```python
from Pymoe import Vndb
instance = Vndb(username, password)  # Username and password are optional, but allow you to login as a user
```
This allows you access to some of the VNDB database. Currently it's just the querying part.
```python
instance.dbstats()  # Return the list of Database stats as seen on the homepage
instance.get(stype, flags, filters, options)  # Query the DB. You have to read the VNDB API Docs and my Docs for this. No way around it. Their API is complicated.
```