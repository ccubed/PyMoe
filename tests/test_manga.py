import pytest
import time
import pymoe.manga.get as ang
import pymoe.manga.search as ans

@pytest.fixture(autouse=True)
def dontHammerTheAPIs():
    yield
    time.sleep(2)

# This will test pymoe.manga.get
    
class Test_GET_Default:
    def test_GET_manga(self):
        test = ang.manga(97722)
        assert test['data']['Media']['idMal'] == 102750

    def test_GET_character(self):
        test = ang.character(129928)
        assert test['data']['Character']['name']['full'] == 'Jin-U Seong'
        assert test['data']['Character']['gender'] == 'Male'

class Test_GET_Kitsu:
    def test_GET_manga(self):
        test = ang.kitsu.manga(24147)
        assert test['data']['id'] == '24147'
        assert test['data']['attributes']['slug'] == "one-punch-man"

class Test_GET_Anilist:
    def test_GET_manga(self):
        test = ang.manga(97722)
        assert test['data']['Media']['idMal'] == 102750

    def test_GET_character(self):
        test = ang.anilist.character(129928)
        assert test['data']['Character']['name']['full'] == 'Jin-U Seong'
        assert test['data']['Character']['gender'] == 'Male'

    def test_GET_staff(self):
        test = ang.anilist.staff(122660)
        test = test['data']['Staff']
        assert test['name']['full'] == "Akiko Takase"
        assert test['languageV2'] == "Japanese"
        assert test['gender'] == "Female"


class Test_GET_Mangaupdates:
    def test_GET_series(self):
        test = ang.mangaupdates.manga(55665151734)
        assert test['series_id'] == 55665151734
        assert test['title'] == "Slam Dunk"

    def test_GET_review(self):
        test = ang.mangaupdates.review(305)
        assert test['id'] == 305
        assert test['author']['user_id'] == 46921921505

    def test_GET_publisher(self):
        test = ang.mangaupdates.publisher(21785245567)
        assert test['name'] == "Shueisha"
        assert test['type'] == "Japanese"

    def test_GET_group(self):
        test = ang.mangaupdates.group(51193206100)
        assert test['name'] == "Z Quality Scans"
        assert test['active'] == False

    def test_GET_author(self):
        test = ang.mangaupdates.author(60531410036)
        assert test['name'] == "INOUE Takehiko"
        assert test['bloodtype'] == "B"

    def test_GET_seriesReleaseFeed(self):
        test = ang.mangaupdates.mangaReleaseFeed(55665151734)
        assert test.startswith("<?xml")

    def test_GET_releasesFeed(self):
        test = ang.mangaupdates.releasesFeed()
        assert test.startswith("<?xml")

    def test_GET_seriesByAuthor(self):
        test = ang.mangaupdates.mangaByAuthor(60531410036)
        assert 'total_series' in test
        assert 'series_id' in test['series_list'][0]

    def test_GET_groupsBySeries(self):
        test = ang.mangaupdates.mangaBySeries(55665151734)
        assert 'group_list' in test
        assert 'group_id' in test['group_list'][0]

    def test_GET_genres(self):
        test = ang.mangaupdates.genres()
        assert 'id' in test[0]
        assert 'genre' in test[0]

# this will test pymoe.manga.search
class Test_SEARCH_Default:
    def test_SEARCH_manga(self):
        test = ans.manga("Dragon")
        assert 'id' in test[0]
        assert 'idMal' in test[0]

class Test_SEARCH_Kitsu:
    """
        This is only here to document that we don't run tests against search endpoints on kitsu as they are in the process of being deprecated by kitsu.
    """
    pass

class Test_SEARCH_Anilist:
    def test_SEARCH_manga(self):
        test = ans.anilist.manga("Dragon")
        assert 'id' in test[0]
        assert 'idMal' in test[0]

class Test_SEARCH_Mangaupdates:
    def test_SEARCH_categories(self):
        test = ans.mangaupdates.categories("Academy")
        assert 'record' in test[0]
        assert 'usage' in test[0]['record']

    def test_SEARCH_authors(self):
        test = ans.mangaupdates.authors("Inoue")
        assert 'record' in test[0]
        assert 'id' in test[0]['record']

    def test_SEARCH_groups(self):
        test = ans.mangaupdates.groups("Asura")
        assert 'record' in test[0]
        assert 'group_id' in test[0]['record']

    def test_SEARCH_publishers(self):
        test = ans.mangaupdates.publishers("Kadokawa")
        assert 'record' in test[0]
        assert 'publisher_id' in test[0]['record']

    def test_SEARCH_reviews(self):
        test = ans.mangaupdates.reviews(55665151734)
        assert 'record' in test[0]
        assert 'author' in test[0]['record']

    def test_SEARCH_releases(self):
        test = ans.mangaupdates.releases(55665151734)
        assert 'record' in test[0]
        assert 'groups' in test[0]['record']
        
    def test_SEARCH_series(self):
        test = ans.mangaupdates.manga("Dragon")
        assert 'record' in test[0]
        assert 'series_id' in test[0]['record']