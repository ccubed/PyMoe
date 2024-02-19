import pymoe.manga.get.anilist as anilist
import pymoe.manga.get.kitsu as kitsu
import pymoe.manga.get.mangaupdates as mangaupdates

# Default Functions using Anilist


def manga(item_id: int):
    return anilist.manga(item_id)


def character(item_id: int):
    return anilist.character(item_id)


def staff(item_id: int):
    return anilist.staff(item_id)
