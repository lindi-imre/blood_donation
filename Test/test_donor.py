__author__ = 'Slezak Attila'

import unittest
from donor import Person
from sys import exit

class TestDonor(unittest.TestCase):
    def test_name(self):
        self.assertEqual("Mikes Kelemen", Person.test_mod(["Donor's name", "", "miKes keLemen", "Test"]))

    def test_weight(self):
        self.assertEqual("52", Person.test_mod(["Weight", "", "52", "Test"]))

    def test_weight_exit(self):
        with self.assertRaises(SystemExit):
            Person.test_mod(["Weight", "", "49", "Test"])

if __name__ == '__main__':
    unittest.main()
