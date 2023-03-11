from . import anilist
from . import kitsu

# Default Functions using Anilist

def manga(term : str):
    return anilist.manga(term)