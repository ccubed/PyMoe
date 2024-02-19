import time
import pytest
import pymoe.anime.get as ang
import pymoe.anime.search as ans
from tests.client import MAL_CLIENT_ID
from pymoe.utils.errors import methodNotSupported
from pymoe.anime import setMalClient as SMC

@pytest.fixture(autouse=True)
def dontHammerTheAPIs():
    yield
    time.sleep(2)

# The following tests are for pymoe.anime.get

class Test_GET_Default:
    """
        Test the functions at pymoe.anime.get
        Not Test: Episode
        Reason: Haven't been able to find an episode ID
    """
    def test_GET_Character(self):
        test = ang.character(176754)
        test = test['data']['Character']
        assert test['name']['full'] == 'Frieren'
        assert test['gender'] == 'Female'
        assert test['age'] == '1000+'
        assert test['media']['nodes'][0]['id'] == 118586
        assert test['media']['nodes'][0]['idMal'] == 126287

    def test_GET_Show(self):
        test = ang.show(154587)
        test = test['data']['Media']
        assert test['title']['english'] == "Frieren: Beyond Journey’s End"
        assert test['title']['native'] == "葬送のフリーレン"
        assert test['idMal'] == 52991

    def test_GET_Episode(self):
        assert 1 == 1

    def test_GET_Staff(self):
        test = ang.staff(122660)
        test = test['data']['Staff']
        assert test['name']['full'] == "Akiko Takase"
        assert test['languageV2'] == "Japanese"
        assert test['gender'] == "Female"

    def test_GET_Studio(self):
        test = ang.studio(11)
        assert test['data']['Studio']['name'] == "MADHOUSE"

class Test_GET_Anilist:
    """
        Test pymoe.anime.get.anilist
        GET Functions: character, show, season, episode, streaming, staff, studio
        Not Tested: Episode
        Reason: Haven't been able to find an episode ID
    """
    def test_GET_Season(self):
        test = ang.anilist.season()
        assert 'id' in test[0]
        assert 'idMal' in test[0]


    def test_GET_Streaming(self):
        test = ang.anilist.streaming(154587)
        test = test['data']['Media']['streamingEpisodes'][0]
        assert test['title'] == "Episode 18 - First-Class Mage Exam"
        assert test['site'] == "Crunchyroll"

    def test_GET_Character(self):
        test = ang.anilist.character(176754)
        test = test['data']['Character']
        assert test['name']['full'] == 'Frieren'
        assert test['gender'] == 'Female'
        assert test['age'] == '1000+'
        assert test['media']['nodes'][0]['id'] == 118586
        assert test['media']['nodes'][0]['idMal'] == 126287
    
    def test_GET_Show(self):
        test = ang.anilist.show(154587)
        test = test['data']['Media']
        assert test['title']['english'] == "Frieren: Beyond Journey’s End"
        assert test['title']['native'] == "葬送のフリーレン"
        assert test['idMal'] == 52991

    def test_GET_Episode(self):
        assert 1 == 1

    def test_GET_Staff(self):
        test = ang.anilist.staff(122660)
        test = test['data']['Staff']
        assert test['name']['full'] == "Akiko Takase"
        assert test['languageV2'] == "Japanese"
        assert test['gender'] == "Female"

    def test_GET_Studio(self):
        test = ang.anilist.studio(11)
        assert test['data']['Studio']['name'] == "MADHOUSE"

class Test_GET_Mal:
    """
        Test pymoe.anime.get.mal
        GET Functions: character, show, episode, streaming, staff, studio
        Also tested: Client ID Assertion, Client ID Setting
    """
    def test_GET_ClientIdAssert(self):
        with pytest.raises(ValueError):
            ang.mal.show(1)
    
    def test_GET_ClientIdSet(self):
        SMC(MAL_CLIENT_ID)
        assert ang.mal.settings['header']['X-MAL-CLIENT-ID'] == MAL_CLIENT_ID
    
    def test_GET_Nonsupported(self):
        # Just do all these in one because they should all return the same exception
        with pytest.raises(methodNotSupported):
            ang.mal.character(1)
            ang.mal.episode(1)
            ang.mal.streaming(1)
            ang.mal.staff(1)
            ang.mal.studio(1)

    def test_GET_Show(self):
        SMC(MAL_CLIENT_ID)
        test = ang.mal.show(52991)
        assert test['title'] == "Sousou no Frieren"
        assert test['nsfw'] == "white"

class Test_GET_Kitsu:
    """
        Test pymoe.anime.get.kitsu
        GET Functions: studio, staff, episode, show, character
        Not currently tested: Studio, Staff
        Reason: There's no search endpoint and I haven't been able to find a show with either attached
    """
    def test_GET_Character(self):
        test = ang.kitsu.character(85849)
        test = test['data']
        assert test['id'] == '85849'
        assert test['type'] == "characters"
        assert test['attributes']['slug'] == "freezen"

    def test_GET_Show(self):
        test = ang.kitsu.show(46474)
        test = test['data']
        assert test['id'] == '46474'
        assert test['type'] == "anime"
        assert test['attributes']['slug'] == "sousou-no-frieren"

    def test_GET_Episode(self):
        test = ang.kitsu.episode(353471)
        test = test['data']
        assert test['id'] == '353471'
        assert test['type'] == "episodes"
        assert test['attributes']['titles']['en'] == "The Journey's End"

# These tests are for pymoe.anime.search
class Test_SEARCH_Default:
    """
        Test the functions at pymoe.anime.search
        Not Test: Episode
        Reason: Haven't been able to find an episode ID
    """
    def test_SEARCH_Characters(self):
        test = ans.characters("Goku")
        assert 'id' in test[0]

    def test_SEARCH_Staff(self):
        test = ans.staff("Akiko Takase")
        assert 'id' in test[0]

    def test_SEARCH_Shows(self):
        test = ans.shows("Frieren")
        assert 'id' in test[0]
        assert 'idMal' in test[0]

    def test_SEARCH_Studios(self):
        test = ans.studios("MADHOUSE")
        assert 'id' in test[0]

    def test_SEARCH_Season(self):
        test = ans.season()
        assert 'id' in test[0]
        assert 'idMal' in test[0]

class Test_SEARCH_Anilist:
    """
        Test pymoe.anime.search.anilist
        SEARCH Functions: characters, staff, shows, studios, airingSchedule
        Not Tested: Episode
        Reason: Haven't been able to find an episode ID
    """
    def test_SEARCH_Characters(self):
        test = ans.anilist.characters("Goku")
        assert 'id' in test[0]

    def test_SEARCH_Staff(self):
        test = ans.anilist.staff("Akiko Takase")
        assert 'id' in test[0]

    def test_SEARCH_Shows(self):
        test = ans.anilist.shows("Frieren")
        assert 'id' in test[0]
        assert 'idMal' in test[0]

    def test_SEARCH_Studios(self):
        test = ans.anilist.studios("MADHOUSE")
        assert 'id' in test[0]

    def test_SEARCH_AiringSchedule(self):
        test = ans.anilist.airingSchedule(154587)
        assert 'id' in test[0]


class Test_SEARCH_Mal:
    """
        Test pymoe.anime.search.mal
        SEARCH Functions: characters, shows, staff, studios, season
        Not Supported: characters, staff, studios
        Also tested: Client ID Assertion, Client ID Setting
    """    
    def test_SEARCH_ClientIdSet(self):
        SMC(MAL_CLIENT_ID)
        assert ans.mal.settings['header']['X-MAL-CLIENT-ID'] == MAL_CLIENT_ID

    def test_SEARCH_NotSupported(self):
        # Just do all these at once
        with pytest.raises(methodNotSupported):
            ans.mal.characters('1')
            ans.mal.staff('1')
            ans.mal.studios('1')

    def test_SEARCH_shows(self):
        SMC(MAL_CLIENT_ID)
        test = ans.mal.shows("Frieren")
        assert 'id' in test[0]


    def test_SEARCH_season(self):
        SMC(MAL_CLIENT_ID)
        test = ans.mal.season()
        assert 'id' in test[0]

class Test_SEARCH_Kitsu:
    """
        This is only here to document that we don't run tests against search endpoints on kitsu as they are in the process of being deprecated by kitsu.
    """
    pass