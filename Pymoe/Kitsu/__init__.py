from .anime import *
from .user import *
from .library import *
from .manga import *
from .drama import *
from .auth import *


class Kitsu:
    """
        :ivar KitsuAnime anime: Instance interface for the Kitsu Anime endpoints
        :ivar KitsuUser user: Instance interface for the Kitsu User endpoints
        :ivar KitsuLib library: Instance interface for the Kitsu Library endpoints.
        :ivar KitsuManga manga: Instance interface for the Kitsu Manga endpoints.
        :ivar KitsuDrama drama: Instance interface for the Kitsu Drama endpoints.
        :ivar KitsuAuth auth: Instance interface for the Kitsu Auth endpoints / storage engine.
    """
    def __init__(self, cid, csecret):
        """
        Initialize a new Kitsu API instance.
        """
        api = "https://kitsu.io/api/edge"
        header = {
            'User-Agent': 'Pymoe (git.vertinext.com/ccubed/Pymoe)',
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }
        self.anime = KitsuAnime(api, header)
        self.manga = KitsuManga(api, header)
        self.drama = KitsuDrama(api, header)
        self.library = KitsuLib(api, header)
        self.user = KitsuUser(api, header)
        self.auth = KitsuAuth(header, cid, csecret)
