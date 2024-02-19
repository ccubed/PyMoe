# Pymoe.Anime - Kitsu

This is the documentation for the Kitsu module of Pymoe.Anime.

## Overview

| Operation  | Endpoints  |
| ---------- | -------------------------------------- |
| `GET`  | character, show, episode, staff, studio |
| `SEARCH` | characters, shows, staff, studios, season, streaming |

!!! warning "End of Life"

    Just a reminder that eventually the Search endpoints for Kitsu will be removed and I heavily suggest moving to MAL or Anilist. Get endpoints will remain here until they stop working though my understanding is they will not.

## Return Formatting

It's everywhere. It's pretty apparent they used one of those tools that automatically generates a swagger API based on data models and the data returned mirrors that. There's no standard return formatting. Your best bet is to test the functions and look at the return data structure. You can also use their apiary documentation to send test requests to get returns.

## Some Notes

### Unsupported Endpoints

The only endpoints that actually work here are character(s), show(s), season, episode, and streaming. The others remain here because I make efforts to maintain parity between all the modules of a specific type.

## Some Examples

```python

# Apparently this is a character called Freezen
pymoe.anime.get.kitsu.character(85849)

# This is the last episode of Frieren: Beyond Journey's End
pymoe.anime.get.kitsu.episode(353471)

```