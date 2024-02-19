# Pymoe.Anime - MAL

This is the documentation for the MyAnimeList (MAL) module of Pymoe.Anime.

## Overview

| Operation  | Endpoints  |
| ---------- | -------------------------------------- |
| `GET`  | character, show, episode, streaming, staff, studio |
| `SEARCH` | shows, staff, studios, season |

## Supported Interfaces

It's just show(s) and season. You can search shows, you can get shows, and you can grab a seasonal listing. That's it. 

## Return Formatting

It returns without any special formatting. It's a very straightforward API. 

## Some Examples

```python
import pymoe

# Get Frieren: Beyond Journey's End
pymoe.anime.get.mal.show(52991)

# Get a seasonal list for the current season
pymoe.anime.search.mal.season()
```