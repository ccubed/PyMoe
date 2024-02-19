import time
import pytest
import pymoe.ln.get as ang
import pymoe.ln.search as ans

@pytest.fixture(autouse=True)
def dontHammerTheAPIs():
    yield
    time.sleep(2)

# test pymoe.ln.get
class Test_GET_Default:
    def test_GET_series(self):
        test = ang.series(581)
        assert test['id'] == 581
        assert test['title'] == "Death March kara Hajimaru Isekai Kyusoukyoku"

    def test_GET_artist(self):
        test = ang.artist(550)
        assert test['name'] == "Shri"

    def test_GET_author(self):
        test = ang.author(622)
        assert test['name'].lower() == "ainana hiro"

    def test_GET_group(self):
        test = ang.group(1)
        assert test['group'] == "Sousetsuka"

    def test_GET_genre(self):
        test = ang.genre(6005)
        assert test['genre'] == "action"
        assert 'id' in test['series'][0]

    def test_GET_publisher(self):
        test = ang.publisher(724)
        assert test['name'] == "Fujimi Shobo"

    def test_GET_tag(self):
        test = ang.tag(1632979)
        assert test['tag'] == "academy"
        assert 'id' in test['series'][0]

class Test_GET_Bakatsuki:
    def test_GET_active(self):
        ang.bakatsuki.active()

    def test_GET_chapters(self):
        ang.bakatsuki.chapters("Puppetmaster")

    def test_GET_cover(self):
        ang.bakatsuki.cover(104137)

class Test_GET_WLNUpdates:
    def test_GET_series(self):
        test = ang.wlnupdates.series(581)
        assert test['id'] == 581
        assert test['title'] == "Death March kara Hajimaru Isekai Kyusoukyoku"

    def test_GET_artist(self):
        test = ang.wlnupdates.artist(550)
        assert test['name'] == "Shri"

    def test_GET_author(self):
        test = ang.wlnupdates.author(622)
        assert test['name'].lower() == "ainana hiro"

    def test_GET_group(self):
        test = ang.wlnupdates.group(1)
        assert test['group'] == "Sousetsuka"

    def test_GET_genre(self):
        test = ang.wlnupdates.genre(6005)
        assert test['genre'] == "action"
        assert 'id' in test['series'][0]

    def test_GET_publisher(self):
        test = ang.wlnupdates.publisher(724)
        assert test['name'] == "Fujimi Shobo"

    def test_GET_tag(self):
        test = ang.wlnupdates.tag(1632979)
        assert test['tag'] == "academy"
        assert 'id' in test['series'][0]

# test pymoe.ln.search
class Test_SEARCH_Default:
    def test_SEARCH_Series(self):
        ans.series("Dragon")

class Test_SEARCH_Bakatsuki:
    def test_SEARCH_lightNovels(self):
        test = ans.bakatsuki.lightNovels()
        assert type(test[0]) is tuple
    
    def test_SEARCH_teasers(self):
        test = ans.bakatsuki.teasers()
        assert type(test[0]) is tuple

    def test_SEARCH_webNovels(self):
        test = ans.bakatsuki.webNovels()
        assert type(test[0]) is tuple

class Test_SEARCH_WLNUpdates:
    def test_SEARCH_titles(self):
        test = ans.wlnupdates.titles("Dragon")
        assert 'sid' in test['results'][0]

    def test_SEARCH_tags(self):
        test = ans.wlnupdates.tags()
        assert type(test) is list
        assert type(test[0]) is list

    def test_SEARCH_genres(self):
        test = ans.wlnupdates.genres()
        assert type(test) is list
        assert type(test[0]) is list

    def test_SEARCH_parametric(self):
        test = ans.wlnupdates.parametric(
            tag_category = {'ability-steal': 'included', 'virtual-reality': 'excluded'},
            chapter_limits = (40,0),
            series_type = {'Translated': 'included'},
            sort_mode = "update"
        )
        assert 'id' in test[0]