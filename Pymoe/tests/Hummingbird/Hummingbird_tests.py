#Test apparatus and dependencies
import logging
import requests
import os
import unittest
from abc import ABCMeta

#Under test
from Pymoe import Hummingbird, errors


class HummingbirdTest(unittest.TestCase, metaclass=ABCMeta):
    """
    Abstracts functions common to all tests of the Hummingbird API.
    """
    @classmethod
    def setUpClass(self):
        """
        Initialize logging before the testCase runs. The logs will be output to
        a .log file in a test_logs directory, which will be created if it does
        not exist.
        """
        logging_folder_name = 'test_logs'
        if not (os.path.exists(logging_folder_name)):
            os.mkdir(logging_folder_name)

        #Note:testName is initialized in each setUp(), so this log must not be
        #   used in setUpClass() or tearDownClass()
        formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(testName)s:%(message)s')

        #The FileHandler creates the .log file. It is in self so it can be closed
        test_file_path = os.path.join(logging_folder_name, 'testing_' + self.__name__ + '.log')
        self.handler = logging.FileHandler(test_file_path, mode='w')
        self.handler.setFormatter(formatter)
        
        self.log = logging.getLogger('test_Hummingbird_' + self.__name__)
        self.log.addHandler(self.handler)
        self.log.setLevel(logging.DEBUG)

        self.api = 'https://hummingbird.me/api/v1'

    @classmethod
    def tearDownClass(self):
        """
        Close the logging handler after all tests complete.
        """
        self.handler.close()

    def setUp(self):
        """
        Initialize the Hummingbird instance and record the test name for logging
        before each test.
        """
        self.log = logging.LoggerAdapter(self.log, {'testName':self._testMethodName})

        #self.log.debug(self._testMethodName)
        self.instance = Hummingbird()

    def log_json_result(self, result, correct):
        """
        Common operation: Log both the correct value and the value returned by
        PyMoe.
        """
        self.log.debug('Result JSON:' + str(result))
        self.log.debug('Correct JSON:' +str(correct))

class HummingbirdAnimeV1Test(HummingbirdTest):
    def test_anime_search_by_id_exists(self):
        """
        instance.anime.id(id) with a valid id returns json representing the
        series. id is a number.
        """
        correct_json = requests.get(self.api + '/anime/11172').json()
        PyMoe_json = self.instance.anime.id(11172)
        self.log_json_result(PyMoe_json, correct_json)

        self.assertEqual(PyMoe_json, correct_json)

    def test_anime_search_by_id_not_exists(self):
        """
        instance.anime.id(id) with an invalid id throws ServerError exception.
        id is a number.
        """
        with self.assertRaises(errors.ServerError):
            PyMoe_json = self.instance.anime.id('9999999999999')

    def test_anime_search_by_name_exists(self):
        """
        instance.anime.id(id) with a valid id returns JSON representing the
        series. id is the anime title as a string.
        """
        #The [0] is there because HB's search is fuzzy. It returns a list of 1 here.
        correct_json = requests.get(self.api + '/search/anime?query=classicaloid').json()[0]
        PyMoe_json = self.instance.anime.id('classicaloid')
        self.log_json_result(PyMoe_json, correct_json)

        self.assertEqual(PyMoe_json, correct_json)

    def test_anime_search_by_name_not_exists(self):
        """
        instance.anime.id(id) with an invalid id throws ServerError exception.
        id is the anime title as a string.
        """
        with self.assertRaises(errors.ServerError):
            PyMoe_json = self.instance.anime.id('coryinthehouse')

class HummingbirdLibraryTest(HummingbirdTest):
    def test_library_get_valid(self):
        """
        instance.library.get(username) with a valid username returns JSON
        representing user's entire 
        """
        #TODO: Should have a designated user for the project.
        username = 'De1iriousKitten' #Arbitrary user with few entries. 

        correct_json = requests.get(self.api + '/users/' + username + "/library").json()
        PyMoe_json = self.instance.library.get(username)
        self.log_json_result(PyMoe_json, correct_json)

        self.assertEqual(PyMoe_json, correct_json)
