from .anime import *
from .user import *
from .library import *


class Hummingbird:
    """
        :ivar HBirdAnime \aanime: Instance interface for the Hummingbird Anime endpoints
        :ivar HBirdUser \uuser: Instance interface for the Hummingbird User endpoints
        :ivar HBirdLib \llibrary: Instance interface for the Hummingbird Library endpoints.
    """
    def __init__(self):
        """
        Initialize a new hummingbird API instance.
        """
        api = "https://hummingbird.me/api/v1"
        header = {'User-Agent': 'Pymoe (git.vertinext.com/ccubed/Pymoe)'}
        self.anime = HBirdAnime(api, header)
        self.user = HBirdUser(api, header)
        self.library = HBirdLib(api, header)
