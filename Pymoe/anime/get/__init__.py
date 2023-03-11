from datetime import date
from ..get import anilist
from ..get import kitsu
from ..get import mal

# Default Get Methods using Kitsu

def character(item_id : int):
    """
        Return a Character from Kitsu with the given ID
    """
    return anilist.character(item_id)

def show(item_id : int):
    """
        Return a Show from Kitsu with the given ID
    """
    return anilist.show(item_id)

def episode(item_id : int):
    """
        Return an Episode from Kitsu with the given ID
    """
    return anilist.episode(item_id)

def staff(item_id : int):
    """
        Return a Staff member from Kitsu with the given ID
    """
    return anilist.staff(item_id)

def studio(item_id : int):
    """
        Return a Studio from Kitsu with the given ID
    """
    return anilist.studio(item_id)