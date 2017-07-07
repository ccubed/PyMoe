[![Documentation Status](https://readthedocs.org/projects/pymoe/badge/?version=latest)](http://pymoe.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/ccubed/PyMoe.svg?branch=master)](https://travis-ci.org/ccubed/PyMoe)
# PyMoe
Welcome to PyMoe, the only python lib you'll ever need if you need the animu/mangu on the python platform.
## 1.0
This brings us to 1.0. A stable release for Pymoe. It supports the majority of my end goal websites and it has some good interfaces. This is a breaking change, thus the major bump.
I cannot stress enough that you should not update unless you have taken the time to read through and note the differences. There are several.

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

## Anidb
Status: Not Started

## Anilist
Ready to go! My specific implementation will handle your readonly credentials.
Specific user credentials are an exercise for the programmer.
To create an interface:
```python
from Pymoe import Anilist
instance = Anilist(client_id, client_secret)
```
You get a client_id and client_secret by going to your user settings and clicking developer. There you can make a new app.
Afterwards, Anilist has four interfaces. Get, Search, Library and Users. At the moment, Get and Search work.
```python
# get
alist.get.anime(49) # get anime with the id of 49
alist.get.manga(30014) # get manga with the id of 30014
alist.get.staff(95004) # get staff with the id of 95004
alist.get.studio(2) # get studio with the id of 2
alist.get.character(11) # get character with the id of 11

# search
alist.search.character("Cecil") # Search characters for cecil
alist.search.anime("Bleach") # Search anime for bleach
alist.search.manga("Bleach") # Search manga for bleach
alist.search.staff("Miyuki") # Search staff for Miyuki
alist.search.studio("go") # Search studios for go

# reviews
alist.get.reviews(21049, "anime", False, 2174) # Get reviews for anime 21049. In this case, get the review with an id of 2174
alist.get.reviews(21049, "anime", True) # Get reviews for anime 21049. In this case, get all reviews.
alist.get.reviews("Remiak", "user") # Get the reviews user Remiak has written
```
### Reviews quick and dirty
Just a quick side about reviews.
The reviews function works in this way.
```python
alist.get.reviews(from what, what is this thing, do you want all of them, if you don't want all of them which one do you want)
```
The first argument is what you want to get reviews from. It could be an ID for an anime or manga or it could be a username.
The second argument is what type of thing it is. This should be one of anime, manga or user. This helps the review function know which endpoint to call.
The third argument is a boolean that tells us whether you want all the reviews for that item or just one. A user will always get all the reviews.
The fourth argument is optional and only applies when you just want one review. It should be the ID of the review you want.


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

## Mal
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
