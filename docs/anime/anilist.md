# Pymoe.Anime - Anilist

This is the documentation for the Anilist module of Pymoe.Anime.

## Overview

| Operation  | Endpoints  |
| ---------- | -------------------------------------- |
| `GET`  | character, show, season, episode, streaming, staff, studio |
| `SEARCH` | characters, shows, staff, studios, airingSchedule, dynamicRequest |

Anilist does not separate staff and studios by manga and anime. Otherwise, Anilist is one of the easiest APIs to work with. It provides predictable results with easily inferred structures. It also supports most anything you could possibly need to build any kind of app from streaming links to episode details to airingSchedules.

## Some Notes

### Streaming, airingSchedule and dynamicRequest

The only methods that really need notes are these three. The rest of the endpoints work exactly how you would expect them to. If you search for characters you're going to get back a list of characters matching your term. If you get a character, you get information back on that character. So on and so forth.

Streaming on the other hand essentially returns the list of episodes for a series ID that appears under the WATCH header on their website. If you've never clicked on these, they actually take you to a site where you can stream the episode. So for Frieren: Beyond Journey's End this returns a list of links to Crunchyroll where you can watch the episodes. This endpoint can be useful for other reasons as well since it also returns episode numbers, release dates, and titles.

AiringSchedule returns a list of episodes and the datetime on which they air. This will return all episodes for a given series so it is possible for the datetime to be negative to indicate it happened in the past. The datetime is passed by the timeUntilAiring attribute and it is simply a number of seconds to/since the airing time.

DynamicRequest allows you to run your own GraphQL queries against the Anilist API. We also handle grabbing the data and will even return it as an API Aware iterator if there are multiple results. Keep in mind that this only accepts one argument: A dictionary containing the data required to be posted to the API. That is it needs to have both a 'query' key with the GraphQL Query and a 'variables' key with the needed variables.

## Some Examples

```python
import pymoe

# Get streaming episodes for Frieren: Beyond Journey's End
pymoe.anime.get.anilist.streaming(154587)

# Example Dynamic Request
parameters = {
    'query': """\
        query ($query: String, $page: Int, $perPage: Int){
            Page (page: $page, perPage: $perPage) {
                pageInfo {
                    currentPage
                    hasNextPage
                }
                characters (search: $query) {
                    id
                }
            }
        }
    """,
    'variables': {"query": "Frieren", "page": 1, "perPage": 3}
}
pymoe.anime.search.anilist.dynamicRequest(parameters)
```