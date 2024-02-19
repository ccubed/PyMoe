import re
import requests
import ujson
from collections import OrderedDict
from bs4 import BeautifulSoup as soup
from pymoe.utils.errors import serverError, serializationFailed

settings = {
    "apiurl": "https://www.baka-tsuki.org/project/api.php",
    "header": {"User-Agent": "Pymoe (github.com/ccubed/Pymoe)"},
    "active": 56132,
    "compiledRegex": {
        "chapter": re.compile("volume|chapter", re.I),
        "separate": re.compile("(volume|chapter) (?P<chapter>[0-9]{1,2})", re.I),
    },
}


def cover(pageid: str):
    """
    Get a cover image given a page id.

    :param str pageid: The pageid for the light novel you want a cover image for
    :return str: the image url or None
    """
    r = requests.get(
        settings["apiurl"],
        params={
            "action": "query",
            "prop": "pageimages",
            "pageids": pageid,
            "format": "json",
        },
        headers=settings["header"],
    )

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        # pageid can be returned as an int
        if "pageimage" in jsd["query"]["pages"][str(pageid)]:
            image = "File:" + jsd["query"]["pages"][str(pageid)]["pageimage"]
            r = requests.get(
                settings["apiurl"],
                params={
                    "action": "query",
                    "prop": "imageinfo",
                    "iiprop": "url",
                    "titles": image,
                    "format": "json",
                },
                headers=settings["header"],
            )

            try:
                jsd = ujson.loads(r.text)
            except ValueError:
                return None
            else:
                return jsd["query"]["pages"][list(jsd["query"]["pages"].keys())[0]][
                    "imageinfo"
                ][0]["url"]
        else:
            return None


def active():
    """
    Get a list of active projects.

    :return list: A list of tuples containing a title and pageid in that order.
    """
    projects = []

    r = requests.get(
        settings["apiurl"],
        params={
            "action": "query",
            "list": "categorymembers",
            "cmpageid": settings["active"],
            "cmtype": "page",
            "cmlimit": "500",
            "format": "json",
        },
        headers=settings["header"],
    )

    if r.status_code == 200:
        jsd = ujson.loads(r.text)
        projects.append(
            [(x["title"], x["pageid"]) for x in jsd["query"]["categorymembers"]]
        )

        if "query-continue" in jsd:
            while True:
                r = requests.get(
                    settings["apiurl"],
                    params={
                        "action": "query",
                        "list": "categorymembers",
                        "cmpageid": settings["active"],
                        "cmtype": "page",
                        "cmlimit": "500",
                        "cmcontinue": jsd["query-continue"]["categorymembers"][
                            "cmcontinue"
                        ],
                        "format": "json",
                    },
                    headers=settings["header"],
                )

                if r.status_code == 200:

                    jsd = ujson.loads(r.text)
                    projects.append(
                        [
                            (x["title"], x["pageid"])
                            for x in jsd["query"]["categorymembers"]
                        ]
                    )

                    if "query-continue" not in jsd:
                        break

                else:
                    break

    return projects[0]


def chapters(title: str):
    """
    Get a list of chapters for a visual novel. Keep in mind, this can be slow. I've certainly tried to make it as fast as possible, but it's still pulling text out of a webpage.

    :param str title: The title of the novel you want chapters from
    :return OrderedDict: An OrderedDict which contains the chapters found for the visual novel supplied
    """
    r = requests.get(
        "https://www.baka-tsuki.org/project/index.php?title={}".format(
            title.replace(" ", "_")
        ),
        headers=settings["header"],
    )

    if r.status_code != 200:
        raise serverError(r.text, r.status_code)
    else:
        parsed = soup(r.text, "html.parser")
        dd = parsed.find_all("a")

        volumes = []
        for link in dd:
            if "class" in link.attrs:
                if "image" in link.get("class"):
                    continue

            if "href" in link.attrs:
                if re.search(
                    settings["compiledRegex"]["chapter"], link.get("href")
                ) is not None and not link.get("href").startswith("#"):
                    volumes.append(link)

        seplist = OrderedDict()
        for item in volumes:
            if "title" in item.attrs:
                result = re.search(
                    settings["compiledRegex"]["separate"], item.get("title").lower()
                )
            else:
                result = re.search(
                    settings["compiledRegex"]["separate"], item.text.lower()
                )

            if result and result.groups():
                if result.group("chapter").lstrip("0") in seplist:
                    seplist[result.group("chapter").lstrip("0")].append(
                        [
                            item.get("href"),
                            item.get("title") if "title" in item.attrs else item.text,
                        ]
                    )
                else:
                    seplist[result.group("chapter").lstrip("0")] = [
                        [
                            item.get("href"),
                            item.get("title") if "title" in item.attrs else item.text,
                        ]
                    ]

        return seplist
