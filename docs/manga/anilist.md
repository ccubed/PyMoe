# Pymoe.Manga - Anilist

This is the documentation for the Anilist module of Pymoe.Manga.

## Overview

| Operation  | Endpoints  |
| ---------- | -------------------------------------- |
| `GET`  | manga, character, staff |
| `SEARCH`   | manga, characters, staff |

Anilist mostly only supports getting a manga by ID and searching for a manga by title. Anilist does not separate characters and staff between Anime and Manga, so the character and staff functions here simply refer back to the functions in pymoe.anime.

## Return Formatting

The biggest piece of advice I can give you on this is to read the GraphQL strings in the source. For example, the GraphQL query for a specific manga is...

```graphql
query( $id: Int ) {
    Media( id: $id, type: MANGA ) {
        idMal
        title {
            romaji
            english
        }
        status
        description
        startDate {
            year
            month
            day
        }
        endDate {
            year
            month
            day
        }
        coverImage {
            extraLarge
            large
            medium
            color
        }
        chapters
        volumes
        genres
        synonyms
        averageScore
        isAdult
        siteUrl
        popularity
        characters {
            nodes {
                id
                name {
                    first
                    last
                }
                image {
                    large
                    medium
                }
                description
                gender
                age
                siteUrl
            }
        }
    }
}
```

This also defines the return formatting. For example, if you want the medium coverImage, then the you can get that by doing...
```python
import pymoe

# This is Berserk the Manga
result = pymoe.manga.get.anilist.manga(30002)
print(result['Media']['coverImage']['medium'])
```

As you can see, it directly follows the build of the query. One thing to be aware of is that nodes is a special keyword for GraphQL that indicates multiple results will be returned. So if we wanted to get the first name of every character attached to this manga, we would do...

!!! tip inline end "The Records Appear To Be Incomplete"

    Not all characters have a last name, an age, or a gender. Don't be surprised if these come back as None. 

```python
import pymoe

# This is Berserk the Manga
result = pymoe.manga.get.anilist.manga(30002)

for character in result['Media']['characters']['nodes']:
    print(character['name']['first'])
```

As a more complex example, let's say that we want to run a get request on each character from this manga. Then we can...

```python
import time
import pymoe

# This is Berserk the Manga
result = pymoe.manga.get.anilist.manga(30002)

myNewList = []
for item in result['Media']['characters']['nodes']:
    myNewList.append(pymoe.manga.get.anilist.character(item['id']))
    time.sleep(0.5)
```

Why the sleep call? Since this hits an API, you might want to add a slight pause between requests to avoid being rate limited. This library does not manage rate limiting for you. However, it does return the information you need to identify rate limiting.