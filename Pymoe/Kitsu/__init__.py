from .anime import *
from .user import *
from .library import *
from .manga import *
from .drama import *


class Kitsu:
    """
        :ivar HBirdAnime anime: Instance interface for the Kitsu Anime endpoints
        :ivar HBirdUser user: Instance interface for the Kitsu User endpoints
        :ivar HBirdLib library: Instance interface for the Kitsu Library endpoints.
        :ivar HBirdManga manga: Instance interface for the Kitsu Manga endpoints.
        :ivar HBirdDrama drama: Instsance interface for the Kitsu Drama endpoints.
        :ivar str cid: Client ID for oauth.
        :ivar str csecret: Client Secret for oauth.
    """
    def __init__(self):
        """
        Initialize a new Kitsu API instance.
        """
        api = "https://kitsu.io/api/edge"
        header = {
            'User-Agent': 'Pymoe (git.vertinext.com/ccubed/Pymoe)',
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }
        self.anime = HBirdAnime(api, header)
        self.manga = HBirdManga(api, header)
        self.drama = HBirdDrama(api, header)