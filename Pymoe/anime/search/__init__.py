from pymoe.anime.search import anilist
from pymoe.anime.search import kitsu
from pymoe.anime.search import mal

def characters(term : str):
    return kitsu.characters(term)

def shows(term : str):
    return kitsu.shows(term)

def staff(term : str):
    return kitsu.staff(term)

def studios(term : str):
    return kitsu.studios(term)