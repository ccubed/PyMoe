from ..anime import get
from ..anime import search
from ..anime.get import mal as gm
from ..anime.search import mal as sm

def setKey(apikey: str):
    """
        MAL Requires a key to access the API. 
        This function sets the key in both submodules.
    """
    gm.settings['header']['X-MAL-CLIENT-ID'] = apikey
    sm.settings['header']['X-MAL-CLIENT-ID'] = apikey