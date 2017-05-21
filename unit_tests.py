import os
import unittest
import Pymoe
import requests
from collections import OrderedDict
from Pymoe.Kitsu.helpers import SearchWrapper  # Needed for Instance Comparisons
from Pymoe.Mal.Abstractions import NT_SEARCH_ANIME, NT_SEARCH_MANGA  # Needed for instance Comparisons


class TestPymoe(unittest.TestCase):
    def test_baka(self):
        baka = Pymoe.Bakatsuki()
        self.assertIsInstance(baka.active(), list)
        self.assertIsInstance(baka.light_novels(), list)
        self.assertIsInstance(baka.teaser(), list)
        self.assertIsInstance(baka.web_novels(), list)

        test_novel = baka.active()[0]

        self.assertIsInstance(baka.chapters(test_novel[0]), OrderedDict)
        self.assertIsInstance(baka.cover(test_novel[1]), str)
        self.assertIsInstance(baka.get_text(test_novel[0]), str)

        del test_novel

    def test_kitsuAnime(self):
        kitsu = Pymoe.Kitsu("dd031b32d2f56c990b1425efe6c42ad847e7fe3ab46bf1299f05ecd856bdb7dd", "54d7307928f63414defd96399fc31ba847961ceaecef3a5fd93144e960c0e151")
        test_search = kitsu.anime.get(244)
        self.assertIsInstance(test_search, dict)
        self.assertEqual(test_search['data']['attributes']['canonicalTitle'], "Bleach")
        del test_search

        test_search = kitsu.anime.search("Bleach")
        self.assertIsInstance(test_search, SearchWrapper)
        self.assertEqual(test_search[0]['attributes']['canonicalTitle'], "Bleach")
        del test_search

    def test_kitsuManga(self):
        kitsu = Pymoe.Kitsu("dd031b32d2f56c990b1425efe6c42ad847e7fe3ab46bf1299f05ecd856bdb7dd", "54d7307928f63414defd96399fc31ba847961ceaecef3a5fd93144e960c0e151")
        test_search = kitsu.manga.get(20463)
        self.assertIsInstance(test_search, dict)
        self.assertEqual(test_search['data']['attributes']['canonicalTitle'], "Good Luck, Demon King!")
        del test_search

        test_search = kitsu.manga.search("King")
        self.assertIsInstance(test_search, SearchWrapper)
        self.assertEqual(test_search[0]['attributes']['canonicalTitle'], "Good Luck, Demon King!")
        del test_search

    def test_kitsuDrama(self):
        pass  # There are 0 Dramas in the edge server

    def test_kitsuAuth(self):
        kitsu = Pymoe.Kitsu("dd031b32d2f56c990b1425efe6c42ad847e7fe3ab46bf1299f05ecd856bdb7dd", "54d7307928f63414defd96399fc31ba847961ceaecef3a5fd93144e960c0e151")
        kitsu.auth.set_remember(True)
        tokens = kitsu.auth.authenticate("ccubed.techno@gmail.com", os.environ['KITSU_PW'])
        self.assertIsInstance(tokens, tuple)
        self.assertEqual(tokens[0], kitsu.auth.get("ccubed.techno@gmail.com"))

    def test_kitsuUser(self):
        kitsu = Pymoe.Kitsu("dd031b32d2f56c990b1425efe6c42ad847e7fe3ab46bf1299f05ecd856bdb7dd", "54d7307928f63414defd96399fc31ba847961ceaecef3a5fd93144e960c0e151")
        test_search = kitsu.user.search("CCubed")
        self.assertIsInstance(test_search, SearchWrapper)
        self.assertEqual("119864", test_search[0]['id'])
        self.assertEqual(1, len(test_search))
        self.assertEqual("CCubed", test_search[0]['attributes']['name'])
        del test_search

        test_search = kitsu.user.get(119864)
        self.assertIsInstance(test_search, dict)
        self.assertEqual("119864", test_search['id'])
        self.assertEqual("CCubed", test_search['attributes']['name'])
        del test_search

        tokens = kitsu.auth.authenticate("ccubed.techno@gmail.com", os.environ['KITSU_PW'])

        update_dict = {"about": "A Computer Programmer, Coder and Future Teacher."}
        self.assertTrue(kitsu.user.update(119864, update_dict, tokens[0]))
        del update_dict

    def test_kitsuLibrary(self):
        kitsu = Pymoe.Kitsu("dd031b32d2f56c990b1425efe6c42ad847e7fe3ab46bf1299f05ecd856bdb7dd", "54d7307928f63414defd96399fc31ba847961ceaecef3a5fd93144e960c0e151")
        test_search = kitsu.library.get(119864)
        self.assertIsInstance(test_search, SearchWrapper)
        del test_search

        tokens = kitsu.auth.authenticate("ccubed.techno@gmail.com", os.environ['KITSU_PW'])

        new_entry = {"status": "current", "progress": 4}
        lib_entry_id = kitsu.library.create(119864, 244, "anime", tokens[0], new_entry)

        self.assertTrue(kitsu.library.update(lib_entry_id, {"progress": 5}, tokens[0]))
        self.assertTrue(kitsu.library.delete(lib_entry_id, tokens[0]))

    def test_Mal(self):
        mal = Pymoe.Mal("TeshiKO", os.environ['MAL_PW'])
        test_search = mal.anime.search("Bleach")
        self.assertIsInstance(test_search, NT_SEARCH_ANIME)
        self.assertEqual(test_search.finished[0].title, "Bleach")
        self.assertEqual(test_search.finished[0].id, "269")
        test_anime = test_search.finished[0]
        del test_search

        test_search = mal.manga.search("King")
        self.assertIsInstance(test_search, NT_SEARCH_MANGA)
        self.assertEqual(test_search.finished[0].title, "Kareshi Kanojo no Jijou")
        self.assertEqual(test_search.finished[0].id, "17")
        test_manga = test_search.finished[0]
        del test_search

        test_anime.status.user = "Currently Watching"
        test_anime.episodes.current = 1
        self.assertTrue(mal.anime.add(test_anime))
        test_anime.episodes.current = 2
        self.assertTrue(mal.anime.update(test_anime))
        self.assertTrue(mal.anime.delete(test_anime))
        del test_anime

        test_manga.status.user = "Currently Reading"
        test_manga.chapters.current = 1
        test_manga.volumes.current = 1
        self.assertTrue(mal.manga.add(test_manga))
        test_manga.chapters.current = 2
        self.assertTrue(mal.manga.update(test_manga))
        self.assertTrue(mal.manga.delete(test_manga))

    def test_VNDB(self):
        vndb = Pymoe.VNDB()
        self.assertIsInstance(vndb.dbstats(), dict)

    def test_Anilist(self):
        alist = Pymoe.Anilist(os.environ['ANILIST_CSECRET'], os.environ['ANILIST_CID'])

        # Search
        self.assertIsInstance(alist.search.character("Cecil"), list)
        self.assertIsInstance(alist.search.anime("Bleach"), list)
        self.assertIsInstance(alist.search.manga("Bleach"), list)
        self.assertIsInstance(alist.search.staff("Miyuki"), list)
        self.assertIsInstance(alist.search.studio("go"), list)

        # Get
        self.assertIsInstance(alist.get.anime(49), dict)
        self.assertIsInstance(alist.get.manga(30014), dict)
        self.assertIsInstance(alist.get.staff(95004), dict)
        self.assertIsInstance(alist.get.studio(2), dict)
        self.assertIsInstance(alist.get.character(11), dict)

        # Get reviews
        self.assertIsInstance(alist.get.reviews(21049, "anime", False, 2174), dict)
        self.assertIsInstance(alist.get.reviews(21049, "anime", True), dict)
        self.assertIsInstance(alist.get.reviews("Remiak", "user"), dict)
