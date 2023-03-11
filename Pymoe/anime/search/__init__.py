from datetime import date
from ..search import anilist
from ..search import kitsu
from ..search import mal

# Default Search Methods using Kitsu

def characters(term : str):
    return anilist.characters(term)

def shows(term : str):
    return anilist.shows(term)

def staff(term : str):
    return anilist.staff(term)

def studios(term : str):
    return anilist.studios(term)

def season(season : str = None, seasonYear : int = date.today().year):
    return kitsu.season(season, seasonYear)