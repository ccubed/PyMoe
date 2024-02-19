# Pymoe.Manga - Mangaupdates

This is the documentation for the MangaUpdates module of Pymoe.Manga.

## Overview

| Operation  | Endpoints                              |
| ---------- | -------------------------------------- |
| `GET`      | manga, review, publisher, group, author, mangaReleaseFeed, releasesFeed, mangaByAuthor, groupsByManga, genres                       |
| `SEARCH`   | categories, authors, groups, publishers, reviews, releases, manga                                  |

## GET Methods

| Endpoint | Description |
| -------- | ----------- |
| `MANGA`  | Return information about a manga given an ID |
| `REVIEW` | Return information about a review given an ID |
| `PUBLISHER` | Return information about a publisher given an ID |
| `GROUP` | Return information about a group given an ID |
| `AUTHOR` | Return information about an author given an ID |
| `MANGARELEASEFEED` | Given a Manga ID, return the Manga's Release RSS Feed |
| `RELEASESFEED` | Return the sitewide releases RSS Feed |
| `MANGABYAUTHOR` | Given an Author ID, return all content they authored |
| `GROUPSBYMANGA` | Given a Manga ID, return all groups with releases for that Manga |
| `GENRES` | Return all genres along with stats for them (Manga tagged, etc) |

## SEARCH Methods

| Endpoint | Description |
| -------- | ----------- |
| `MANGA`  | Search for a Manga by Title |
| `RELEASES` | Search for releases that match a given Manga Title |
| `REVIEWS` | Given a Series ID return all reviews |
| `PUBLISHERS` | Search for a publisher |
| `GROUPS` | Search for a Group (Scanlator, etc) |
| `AUTHORS` | Search for an Author |
| `CATEGORIES` | Search for categories that match a term |

## Return Formatting

Thankfully, MangaUpdates's API does not have any special handling requirements. They only return the data requested, sometimes in a list and other times as a single json object. As an example, if we want the title of the Slam Dunk Manga it is...

```python
import pymoe

print(pymoe.manga.get.mangaupdates.series(55665151734)['title'])
```

## Some Notes

### Groups

Groups are defined by MangaUpdates as any Scanlators, Translators, Raw Providers, etc. Any group of people that uploads releases can be found under groups.

### Reviews

Reviews are not comments. So you might go to a page on MangaUpdates with a lot of *User Comments* (At the bottom of the page), but it may have no *User Reviews*. Comments appear at the bottom while Reviews appear in the series information underneath the User Reviews headline.

Keep in mind that when you search for reviews you only get a small excerpt from the review. If you want the full body text for a review, you will have to get a review by ID. You can get review IDs by searching for reviews matching a series. Reviews are not included in the data returned when you get a series by ID.


### The Feed Endpoints

mangaReleaseFeed and releasesFeed both return XML data. They are simply convenience functions that build the required URL for you to get the XML data. I do not parse the XML data, it's returned as a string so you can push it into your XML parser of choice.

Also, you should know that the RSS feeds returned by MangaUpdates have no way to filter the content that is new. It does not use etag, dates, or even a hash to indicate new content. So you're on your own when it comes to parsing for new content and the releasesFeed can return wildly different results even if you call for it back to back. It just depends on how fast releases happen. The Series Release Feed does however return ALL releases for that series even if it's a large XML document.

### Manga By Author and Groups By Manga

Both of these take an ID and return either all manga related to that Author or all Groups with a release for that series ID. It does not return the groups releases. For that you want to use either the mangaReleaseFeed or the releases search endpoint.