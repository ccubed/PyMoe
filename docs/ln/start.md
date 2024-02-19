# Pymoe.LN

!!! note "What Does Default Mean?"

    Whenever the term default is used, it refers to the top level functions available at pymoe.type.operation.endpoint. So `pymoe.anime.get.show` or `pymoe.manga.search.series`.

This is the user guide for Pymoe.LN and its submodules. This page will go over the default methods available at pymoe.ln.get and pymoe.ln.search. Further information on the specifics of each module are in their own documents.

| Module          | Documentation Location                 |
| --------------- | -------------------------------------- |
| `DEFAULT`       | This Page                              |
| `BAKATSUKI`     | [Documentation](bakatsuki.md)          |
| `WLNUPDATES`    | [Documentation](wlnupdates.md)         |

## Default Methods

These default methods route through WLNUpdates.

### Overview

| Operation | Endpoints |
| --------- | --------- |
| `GET` | series, artist, author, group, publisher, genre, tag |
| `SEARCH` | series |

### GET Methods

!!! warning inline end "Genre and Tag"

    Be Warned! You might think that Genre and Tag simply return information about a given Genre or Tag ID. *You would be wrong*. Genre and Tag actually return *all* series with that genre or tag *along with* information about the genre or tag itself. 

| Endpoint | Description | Provider |
| -------- | ----------- | -------- |
| `SERIES` | Get information on a series given an ID | WLNUpdates |
| `ARTIST` | Get information on an artist given an ID | WLNUpdates |
| `AUTHOR` | Get information on an author given an ID | WLNUpdates |
| `PUBLISHER` | Get information on a publisher given an ID | WLNUpdates |
| `GENRE` | See Note | WLNUpdates |
| `TAG` | See Note | WLNUpdates |

!!! example "An Example"

    ```python
    import pymoe

    # Print information about our trusty test series Slam Dunk
    print(pymoe.ln.get.series(55665151734))
    ```

!!! tip "Return Formatting"

    This is gone over in more detail in the specific documents, but this uses WLNUpdates as the data provider. Luckily, WLNUpdates mostly does not wrap their content up in any special formatting. Your return will just be the json object you requested or a list of json objects matching your query. You can access returned attributes directly. The exception to this rule is searching by title which returns the results as a json object, but hides the list of actual results in the 'results' key. This is the only endpoint that operates slightly differently.

### SEARCH Methods

There's only one so this will be short.

| Endpoint | Description | Provider |
| -------- | ----------- | -------- |
| `SERIES` | Search for series by title | WLNUpdates |

!!! example "An Example"

    ```python
    import pymoe

    # Search for Dragon and print the title of each matching series
    for item in pymoe.ln.search.series("Dragon")['results']:
        print(item['title'])
    ```