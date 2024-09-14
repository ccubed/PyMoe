from datetime import date

import pymoe.anime.search.anilist as anilist
import pymoe.anime.search.kitsu as kitsu
import pymoe.anime.search.mal as mal
from pymoe.anime.get.anilist import season as asg

# Default Search Methods using Anilist


def characters(term: str):
    """
    Search for characters that match term on anilist
    """
    return anilist.characters(term)


def shows(term: str):
    """
    Search for characters that match term on anilist
    """
    return anilist.shows(term)


def staff(term: str):
    """
    Search for characters that match term on anilist
    """
    return anilist.staff(term)


def studios(term: str):
    """
    Search for characters that match term on anilist
    """
    return anilist.studios(term)


def season(season: str = None, seasonYear: int = date.today().year):
    """
    Given a season and seasonYear, return the list of seasonal anime from Anilist.
    """
    return asg(season, seasonYear)
