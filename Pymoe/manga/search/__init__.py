import pymoe.manga.search.anilist as anilist
import pymoe.manga.search.kitsu as kitsu
import pymoe.manga.search.mangaupdates as mangaupdates


def manga(title: str):
    return anilist.manga(title)
