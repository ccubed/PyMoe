import pymoe.anime.get
import pymoe.anime.search
import pymoe.anime.get.mal as mg
import pymoe.anime.search.mal as ms


def setMalClient(client_id: str):
    """
    This is a helper function to set the MyAnimeList Client ID at both endpoints.

    :param client_id: Your Client ID
    """
    mg.settings["header"]["X-MAL-CLIENT-ID"] = client_id
    ms.settings["header"]["X-MAL-CLIENT-ID"] = client_id
