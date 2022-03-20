import time
import requests
from .get import *
from .search import *

class anilist:
    """
        Initialize a new instance to the Anilist API.
        This instance will handle read only credentials.

        :ivar dict settings: Various settings used across the module
    """
    def __init__(self):
        """
        :param cid: Client ID
        :param csecret: Client Secret
        :param credentials: If provided, a JWT token for auth requests
        """
        self.settings = {
            'header': {
                'Content-Type': 'application/json',
                'User-Agent': 'Pymoe (github.com/ccubed/PyMoe)',
                'Accept': 'application/json'
            },
            'apiurl': 'https://graphql.anilist.co'
        }

    def get(self, id : int):
        """
        The function to retrieve an anime's details.

        :param id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """
        query_string = """\
            query ($id: Int) {
                Media(id: $id, type: ANIME) {
                    title {
                        romaji
                        english
                    }
                    startDate {
                        year
                        month
                        day
                    }
                    endDate {
                        year
                        month
                        day
                    }
                    coverImage {
                        large
                    }
                    bannerImage
                    format
                    status
                    episodes
                    season
                    description
                    averageScore
                    meanScore
                    genres
                    synonyms
                    nextAiringEpisode {
                        airingAt
                        timeUntilAiring
                        episode
                    }
                }
            }
        """
        vars = {"id": item_id}
        r = requests.post(self.settings['apiurl'],
                         headers=self.settings['header'],
                         json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd