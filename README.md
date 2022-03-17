[![Documentation Status](https://readthedocs.org/projects/pymoe/badge/?version=latest)](http://pymoe.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/ccubed/PyMoe.svg?branch=master)](https://travis-ci.org/ccubed/PyMoe)
# PyMoe
Welcome to Pymoe, the only python lib you'll ever need if you need anime/manga on the python platform.
## Simplified Changelong
1.0.0
: This brings us to 1.0. A stable release for Pymoe. It supports the majority of my end goal websites and it has some good interfaces. This is a breaking change, thus the major bump. I cannot stress enough that you should not update unless you have taken the time to read through and note the differences. There are several.

1.0.4
: This fixes anilist. If you don't have this, anilist won't work.

1.0.6
:Some additions by starry69 to add streaming links on kitsu and to make VNDB filters a little easier to use.

2.0
: Second major release of Pymoe. This will be a breaking change. THe API is going to be unified. Instead of one interface for each service, the interfaces have been reduced down to categories. Note that document below represents a work in progress state.

## Design Philosophy for 2.0
- Quickest, Easiest way to get information about Anime, Manga, Light Novels, and Visual Novels
- User management isn't what this library is meant to cover, so we'll remove it
- List management isn't what this library is meant to cover, so we'll remove it
- Remove as much abstraction as possible
- Someone should be able to download the library, type `Pymoe.[type].search("Dragon")` and get back information about items that match the term 

### Important Note
Once the 2.0 update is completed, pip will transition to downloading 2.0 by default. I will keep 1.0.6 available on pip. Keep this in mind as you develop apps around the library going forward. Once the 2.0 update is on pip, you'll have to specify the specific version 1.0.6 in your requirements files or pip commands.

---

**Supported Services per category**
### Anime
- Kitsu
- Anilist
- MyAnimeList

### Manga
- Kitsu
- Anilist
- MyAnimeList

### Visual Novels (VN)
- VNDB

### Light Novels (LN)
- Bakatsuki

--- 

**Interface Usage**
### Anime
```python
anime.search(term : str, service : int = 1)
```
### Manga
```python
manga.search(term : str, service : int = 1)
```
### Visual Novels (VN)
```python
vn.search(term : str)
vn.search(term : str, stype : str)
vn.search(term : str, stype : str, flags : list = None, filters : str = None, options : dict = None)
vn.release(term : int)
```
### Light Novels (LN)
```python
ln.active()
ln.all(lang : str = "English")
```

---

### Removed Interfaces
vndb.set
: This is a user management function.

vndb.dbstats
: This is a simple command, but the information is not useful to most people

bakatsuki.teasers
: These are incomplete projects that only feature one or a few chapters.

bakatsuki.web_novels()
: This is included in all now.

bakatsuki.get_text()
: This library isn't meant to be a light novel reader, rather a way to get information about light novels that exist.

bakatsuki.chapters()
: See get_text above

bakatsuki.cover()
: This is included in all now.

Anidb (and all features)
: The AID search by Elyozard no longer works and managing a local copy of the anime_title dump isn't what this library is meant to do. As the intention of anidb is to catalog files in general (and using the HTTP API requires file hashing which is outside of the scope of this library), it was removed as the intention is outside of this library's scope.

### Note about Removed Interfaces
While I'm pairing down Pymoe to just focus on getting information as I originally intended (a lot of these were only added because I was just going down a list and adding all API features), you're welcome to grab any of my code and put it towards a new library or app. Have at it!
