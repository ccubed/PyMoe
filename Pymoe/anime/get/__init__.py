from datetime import date
from pymoe.anime.get import anilist
from pymoe.anime.get import kitsu
from pymoe.anime.get import mal

# Default Get Methods using Kitsu

def character(item_id : int):
    return kitsu.character(item_id)

def show(item_id : int):
    return kitsu.show(item_id)

def episode(item_id : int):
    return kitsu.episode(item_id)

def streaming(item_id : int):
    return kitsu.streaming(item_id)

def staff(item_id : int):
    return kitsu.staff(item_id)

def studio(item_id : int):
    return kitsu.studio(item_id)