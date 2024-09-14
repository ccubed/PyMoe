from datetime import date

import pymoe.anime.get.anilist as anilist
import pymoe.anime.get.kitsu as kitsu
import pymoe.anime.get.mal as mal

# Default Get Methods using Anilist


def character(item_id: int):
    """
    Return a Character from Anilist with the given ID
    """
    return anilist.character(item_id)


def show(item_id: int):
    """
    Return a Show from Anilist with the given ID
    """
    return anilist.show(item_id)


def episode(item_id: int):
    """
    Return an Episode from Anilist with the given ID
    """
    return anilist.episode(item_id)


def staff(item_id: int):
    """
    Return a Staff member from Anilist with the given ID
    """
    return anilist.staff(item_id)


def studio(item_id: int):
    """
    Return a Studio from Anilist with the given ID
    """
    return anilist.studio(item_id)
