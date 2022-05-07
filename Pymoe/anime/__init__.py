from pymoe.anime import get
from pymoe.anime import search
import pymoe.anime.get.mal as gm
import pymoe.anime.search.mal as sm

def setKey(apikey: str):
    """
        MAL Requires a key to access the API. 
        This function sets the key in both submodules.
    """
    gm.settings['header']['X-MAL-CLIENT-ID'] = apikey
    sm.settings['header']['X-MAL-CLIENT-ID'] = apikey