__author__ = 'Slezak Attila'

import unittest
from search import Search

class TestSearch(unittest.TestCase):
    def test_file(self):
        self.assertTrue(Search.search_in_file("../Data/donors.csv"))


if __name__ == '__main__':
    unittest.main()
