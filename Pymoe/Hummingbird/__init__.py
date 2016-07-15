from .anime import *
from .user import *
from .library import *


class Hummingbird:
    def __init__(self):
        """
        Initialize a new hummingbird API instance.
        """
        api = "https://hummingbird.me/api/v1"
        header = {'User-Agent': 'Pymoe (git.vertinext.com/ccubed/Pymoe)'}
        self.anime = HBirdAnime(api, header)
        self.user = HBirdUser(api, header)
        self.library = HBirdLib(api, header)
