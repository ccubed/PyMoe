# PyMoe
![Python Versions](https://img.shields.io/pypi/pyversions/pymoe?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.2-blue?style=for-the-badge)
[![PyPi](https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/PyMoe/)
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ccubed/pymoe)

Welcome to PyMoe. PyMoe is a general purpose Python library that wraps APIs for several large websites that offer information about Anime, Manga, Light Novels, and Web Novels. Currently six different APIs are supported with plans for more in the future (Especially looking at MangaDex integration).

You can find the documentation for this on [Github Pages](https://ccubed.github.io/PyMoe/).

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

2.2: 
A major upgrade to existing code. Refactored the code to be more thin and better organized. Switched to the Poetry build engine. Switched to Taskfile.dev for task running. Switched to mkdocs and github pages for documentation. Added MangaUpdates and WLNUpdates as data sources.

## Supported Services per category

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

## A few Examples

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

Further examples are available in the documentation.