# Pymoe.Anime

!!! note "What Does Default Mean?"

    Whenever the term default is used, it refers to the top level functions available at pymoe.type.operation.endpoint. So `pymoe.anime.get.show` or `pymoe.manga.search.series`.

This is the user guide for Pymoe.Anime and its submodules. This page will go over the default methods available at pymoe.anime.get and pymoe.anime.search. Further information on the specifics of each module are in their own documents.

| Module          | Documentation Location                 |
| --------------- | -------------------------------------- |
| `DEFAULT`       | This Page                              |
| `ANILIST`       | [Documentation](anilist.md)      |
| `KITSU`         | [Documentation](kitsu.md)        |
| `MAL`  | [Documentation](mal.md) |

## Default Methods

These default methods route through Anilist.

### Overview

| Operation | Endpoints |
| --------- | --------- |
| `GET` | character, show, episode, staff, studio |
| `SEARCH` | characters, shows, staff, studios, season |

### GET Methods

| Endpoint | Description | Provider |
| -------- | ----------- | -------- |
| `CHARACTER` | Get information on a character given an ID | Anilist |
| `SHOW` | Get information on a show given an ID | Anilist |
| `EPISODE` | Get information on a specific episode given an ID | Anilist |
| `STAFF` | Get information on a given staff member given an ID | Anilist |
| `STUDIO` | Get information on a given studio given an ID | Anilist |

!!! example "An Example"

    ```python

    # Get info on Frieren: Beyond Journey's End
    pymoe.anime.get.show(154587)

    # Get info on Frieren of Frieren: Beyond Journey's End
    pymoe.anime.get.character(176754)
    ```

### Search Methods

| Endpoint | Description | Provider |
| -------- | ----------- | -------- |
| `CHARACTERS` | Search for characters by name | Anilist |
| `SHOWS` | Search for shows by name | Anilist |
| `STAFF` | Search for staffers by name | Anilist |
| `STUDIOS` | Search for studios by name | Anilist |
| `SEASON` | Get seasonal anime | Anilist |

!!! example "An Example"

    ```python

    # Search for shows matching Toradora
    pymoe.anime.search.shows("Toradora")

    # Get the latest seasonal anime
    pymoe.anime.search.season()

    # Get a list of anime from winter season in 2021
    pymoe.anime.search.season(
        theSeason = "winter",
        year = 2021
    )
    ```

### Return Formatting

Since Anilist uses GraphQL the return formatting matches exactly to the GraphQL queries being ran. For example, take the following excerpt.

```graphql
query ($id: Int){
            Staff (id: $id){
                name {
                    full
                }
```

This is an excerpt from the pymoe.anime.get.anilist.staff function. The return formatting of this function is going to be exactly as it appears in this query wrapped in a data key. If you want the full name of the staffer being requested from the returned results it would be:
```python
results['data']['Staff']['name']['full']
```

Search endpoints work the same way, but there's a catch. Since the search endpoints are generally always going to return multiple pages of results, you're most likely to get back an API Aware iterator than the data itself. With our API Aware iterators you do not need to worry about extracting the data and can simply directly access elements. In other words, if the above query had returned as an API Aware iterator instead of a single result you would be able to simply:
```python
results[0]['name']['full']
```

If a search endpoint only returns one page of results, we return that list of results directly so the previous code would still work.

