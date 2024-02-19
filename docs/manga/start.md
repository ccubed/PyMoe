# Pymoe.Manga

!!! note "What Does Default Mean?"

    Whenever the term default is used, it refers to the top level functions available at pymoe.type.operation.endpoint. So `pymoe.anime.get.show` or `pymoe.manga.search.series`.

This is the user guide for Pymoe.Manga and its submodules. This page will go over the default methods available at pymoe.manga.get and pymoe.manga.search. Further information on the specifics of each module are in their own documents.

| Module          | Documentation Location                 |
| --------------- | -------------------------------------- |
| `DEFAULT`       | This Page                              |
| `ANILIST`       | [Documentation](anilist.md)      |
| `KITSU`         | [Documentation](kitsu.md)        |
| `MANGAUPDATES`  | [Documentation](mangaupdates.md) |

## The Default Methods

These default methods use Anilist.

### Overview
| Operation  | Endpoints                              |
| ---------- | -------------------------------------- |
| `GET`      | manga, character                       |
| `SEARCH`   | manga                                  |

### GET Methods

| Endpoint | Description | Provider |
| -------- | ----------- | -------- |
| `MANGA`  | Return information about a manga given an ID | Anilist |
| `CHARACTER` | Return information about a character given an ID | Anilist |

!!! example "Some Examples"

    ```python
    # For Manga information from Anilist Manga ID 97722
    # This manga is Yami ni Hau Mono Lovecraft Kessakushuu
    print(pymoe.manga.get.manga(97722))

    # For information on manga character 129928
    # This is Jin-U Seong, the MC from Solo Leveling
    print(pymoe.manga.get.character(129928))
    ```

!!! tip "Return Formatting"

    This is gone over in more detail in the specific documents, but this uses Anilist as the data provider. Anilist returns data that matches the GraphQL query used to build the request. In this case, the actual data is inside 'Media' in the returned dictionary.

### SEARCH Methods

| Endpoint | Description | Provider |
| -------- | ----------- | -------- |
| `manga`  | Search for the manga that matches the provided title | Anilist |

!!! example "Some Examples"

    ```python
    # Search for the Manga named Toradora on Anilist
    # This will print the dictionary for each returned result
    for item in pymoe.manga.search.manga("Toradora"):
        print(item)

    # Regarding the warning below, this is a way you could build a list with all the results in one list
    myNewList = []
    for item in pymoe.manga.search.manga("Toradora"):
        myNewList.append(item)
    ```

!!! warning "API Aware Lists"

    When using a search module, we return a custom API aware list. This means that whether or not you use the generator structure, the result is a custom list that contains multiple dictionaries of data with each one representing a result from the search term. This list automatically refills itself with more results as you iterate through it. This does mean however that the list never contains the entirity of the results.