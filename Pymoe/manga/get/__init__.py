from . import anilist
from . import kitsu

# Default Functions using Anilist

def manga(item_id : int):
    return anilist.manga(item_id)

def character(item_id : int):
    return anilist.character(item_id)