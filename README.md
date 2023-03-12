[![Documentation Status](https://readthedocs.org/projects/pymoe/badge/?version=latest)](http://pymoe.readthedocs.io/en/latest/?badge=latest)
# PyMoe
Welcome to Pymoe, the only python lib you'll ever need if you need anime/manga on the python platform.

## Installation
If you are looking to install version 2 with the unified api:
```python
python -m pip install pymoe
```

If you are looking for version 1.0.6, the version prior to the unified api update:
```python
python -m pip install pymoe==1.0.6
```

You can also git clone this branch and install it that way:
```python
git clone https://github.com/ccubed/PyMoe.git .
python -m pip install -e .
```

Note that this project does not include a setup.py. This project uses flit, a modern build system. You will have to use a recent version of setuptools and pip that has support for pyproject.toml with a specified build pipeline. 

Assuming you have flit, you can also do:
```python
git clone https://github.com/ccubed/PyMoe.git .
flit install
```

## Simplified Changelong

1.0.0:
This brings us to 1.0. A stable release for Pymoe. It supports the majority of my end goal websites and it has some good interfaces. This is a breaking change, thus the major bump. I cannot stress enough that you should not update unless you have taken the time to read through and note the differences. There are several.

1.0.4:
This fixes anilist. If you don't have this, anilist won't work.

1.0.6:
Some additions by starry69 to add streaming links on kitsu and to make VNDB filters a little easier to use.

2.0:
Second major release of Pymoe. This will be a breaking change. The API is going to be unified. Instead of one interface for each service, the interfaces have been reduced down to categories. Note that document below represents a work in progress state.

## Design Philosophy for 2.0
- Quickest, Easiest way to get information about Anime, Manga, Light Novels, and Visual Novels
- User management isn't what this library is meant to cover, so we'll remove it
- List management isn't what this library is meant to cover, so we'll remove it
- Remove as much abstraction as possible
- Someone should be able to download the library, type `Pymoe.[type].search("Dragon")` and get back information about items that match the term 

### Important Note
Once the 2.0 update is completed, pip will transition to downloading 2.0 by default. I will keep 1.0.6 available on pip. Keep this in mind as you develop apps around the library going forward. Once the 2.0 update is on pip, you'll have to specify the specific version 1.0.6 in your requirements files or pip commands. Also take note that it's no longer Pymoe. Instead, it's pymoe to match snakecase.

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
- None

### Light Novels (LN)
- Bakatsuki

--- 

**Interface Usage**
```python
import pymoe

pymoe.anime.search.shows("Dragon")
pymoe.anime.get.show(13593)
pymoe.anime.search.characters("Sakura Haruno")
pymoe.anime.get.character(102522)

# Specifically kitsu
pymoe.anime.search.kitsu.shows("Dragon")

# specifically anilist
pymoe.anime.search.anilist.shows("Dragon")

# specifically myanimelist
pymoe.anime.search.mal.shows("Dragon")
```

```python
import pymoe

pymoe.ln.get.active()
pymoe.ln.search.web_novels()
pymoe.ln.get.cover(98771)
```

**API Aware Iterators**

All interfaces that return multiple pages of results return as an API Aware Search Iterator. That means you can call `pymoe.anime.search.kitsu.shows("Dragon")` and get back an iterator that automatically calls for new data from the API as you exhaust the items already in the list. All interfaces that only return one result will just return the result. 

So, for instance, this is a valid code segment:
```python
import pymoe

for item in pymoe.anime.search.shows("Dragon"):
    print(item)
```

**Get vs Search**

If it should return one item, it's in a get interface.

If it should return multiple items (or could), it's in a search interface.

If a search interface only returns one result, we just return that result. 

---

## Removed Interfaces
vndb
: The TCP X11 API was shut down and I haven't had the time or energy to test the new HTTP API.

bakatsuki.get_text
: This library isn't meant to be a light novel reader, rather a way to get information about light novels that exist.

bakatsuki.cover
: This is still included as a separate function under pymoe.ln.get.cover. Originally, the intention was to grab a cover whenever projects were requested, but that takes far too long and results in 166 api requests happening at once. If you need novel covers, please request them separately and hopefully in the background over time.

Anidb (and all features)
: The AID search by Elyozard no longer works and managing a local copy of the anime_title dump isn't what this library is meant to do. As the intention of anidb is to catalog files in general (and using the HTTP API requires file hashing which is outside of the scope of this library), it was removed as the intention is outside of this library's scope.

### Note about Removed Interfaces
While I'm pairing down Pymoe to just focus on getting information as I originally intended (a lot of these were only added because I was just going down a list and adding all API features), you're welcome to grab any of my code and put it towards a new library or app. Have at it!

### Note about defaults
Anime
: While Kitsu was originally the default source for anime, this has changed to Anilist for long term support. See note below.

Manga
: Anilist is the default for manga because it identified more random manga by multiple titles than the others did. For example, My Wife Is a Demon Queen / Wo Laopo Shi Mowang Daren / 我老婆是魔王大人 is a chinese manga. Anilist identified it by all three titles, Kitsu by two, and myanimelist didn't find it at all.

LN
: Well, there's only one source

## A Note About Kitsu
If you've been paying attention to what Kitsu is doing with their api, they appear to be moving to Algolia for searching. Algolia requires you to create an account on their website in order to access any member site's data. I'm not going to create an account just for a wrapper. They have a python api already anyways if you want to implement the search. I will continue to leave Kitsu searching in until this change actually happens. However, expect that one day, in the future, Kitsu search end points will no longer work.

SubNote: kitsu.season isn't actually a search even though it appears there. It's a get request with a filter. That will continue to work based on my understanding of the design. 

: You can get more information at https://github.com/hummingbird-me/api-docs