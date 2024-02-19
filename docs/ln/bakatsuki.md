# Pymoe.LN - Bakatsuki

This is the documentation for the Bakatsuki module of Pymoe.LN.

## Overview

| Operation  | Endpoints  |
| ---------- | -------------------------------------- |
| `GET`  | cover, active, chapters |
| `SEARCH`   | lightNovels, teasers, webNovels |

Bakatsuki is actually a wiki and we get information from it by using the built in mediawiki api. This means it is slow. Even using the API, some information, such as chapters, has to be manually pulled from the HTML source. The searches and active endpoints are just getting lists of categories back from the API and formatting them into tuples, so those are fairly fast. If you do use cover or chapters, be prepared for it to take up to a few seconds to extract the data.

## Return Formatting

Thankfully, I have a lot of control over the return formatting due to how the data is gathered.

| Endpoint | Return Format |
| -------- | ------------- |
| `COVER` | A single str representing the URL of the cover image |
| `ACTIVE` | A list of tuples in the format (Title, ID) |
| `CHAPTERS` | An OrderedDict keyed by Chapter Numbers and containing a list of lists in the format (Chapter Link, Chapter Title If Any) |
| `LIGHTNOVELS` | A list of tuples in the format (Title, ID) |
| `TEASERS` | A list of tuples in the format (Title, ID) |
| `WEBNOVELS` | A list of tuples in the format (Title, ID) |

## Some Notes

### Cover versus Chapters

The `COVER` endpoint expects you to pass it the ID from one of the tuples above. The `CHAPTERS` endpoint expects you to pass it the Title from one of the tuples above. So `COVER` is ID, while `CHAPTERS` is Title. The reason for this is how it gathers the data. Chapters is an HTML scrape so we need the page title (Which is coincidentally the same as the series Title) whereas Cover is an API request for the first image on a given page ID.

### Cover Images

The `COVER` endpoint is very taxing on the API. It takes several different requests to actually get that data. I have to first query the details for each image on the page. Then find the specific one I need and generate the File ID. Then we have to send that back to the API to get the actual URL the image resides at. I say all this to say that you should add a slight pause between batch operations.

## Some Examples

```python
import time
import pymoe

# List all Active Projects and their IDs
for project in pymoe.ln.get.bakatsuki.active():
    print("{} with ID {}".format(project[0], project[1]))

# What if we wanted the cover image of each active project?
images = []
for project in pymoe.ln.get.bakatsuki.active():
    images.append(
        (
            project[0], # The Title
            pymoe.ln.get.bakatsuki.cover(project[1]) # The URL to the cover image given a page ID
        )
    )
    time.sleep(0.5)
print(images)
```