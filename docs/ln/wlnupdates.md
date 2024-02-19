LN
GET
    WLNUpdates: series, artist, author, genre, group, publisher, tag
SEARCH
    WLNUpdates: series, tags, genres, parametric

# Pymoe.LN - WLNUpdates

This is the documentation for the WLNUpdates module of Pymoe.LN.

## Overview

| Operation  | Endpoints  |
| ---------- | -------------------------------------- |
| `GET`  | series, artist, author, genre, group, publisher, tag |
| `SEARCH`   | series, tags, genres, parametric |

## Return Formatting

Thankfully, WLNUpdates mostly doesn't format their returns. What you get back is either the json object itself or a list of json objects. The only exception to this is the series search method which returns the list of results hidden behind a 'results' key. So the return for search.series only looks like this.

```
{
    "results": [list of json objects],
    "cleaned_search": a string representing the cleaned search title
}
```

## Some Notes

### On Tag and Genre

As noted on the main page, tag and genre do not do what you think. When you *search* for tags or genres you are going to get back **every** tag and genre on the site along with associated statistics. When you *get* a tag or genre you are going to get back **every** series with that tag or genre along with the name of the tag or genre itself.

### Parametric Searching

Parametric is the advanced search endpoint and it requires you to specify at least one of either a list of tags or list of genres to search by. If you don't provide one or the other, you'll either be redirected to title search (assuming you provided a title) or get an error.

## Some Examples

```python
import pymoe

# Prints Death March kara Hajimaru Isekai Kyusoukyoku
print(pymoe.ln.get.wlnupdates.series(581)['title'])

# Parametric searching
results = pymoe.ln.get.wlnupdates.parametric(
    # Dictionary with Tags as Keys and included/excluded as value
    # genre_category is the same thing but with Genres as Keys
    tag_category={
        'ability-steal': 'included', 
        'virtual-reality': 'excluded'
    },
    # Tuple containing (min, max) chapters to search by. 0 means no limit.
    chapter_limits=(40,0),
    # Dictionary that can only include the keys Translated or Original English Language with value Included/Excluded
    series_type={
        'Translated': 'included'
    },
    # How to sort results. update, chapter-count or name (default) are possible. 
    sort_mode='update',
    # A list of strings that designates extra data to be included or excluded from the results. This adds cover links to the results.
    include_results=['covers']
)
```