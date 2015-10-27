__author__ = 'Slezak Attila'
# -- coding: utf-8 --

import unittest
from check_date_format import CheckDateFormat

class CheckDateFormatTest(unittest.TestCase):
    def test_alphabet(self):
        self.assertTrue(CheckDateFormat.check_date_format("Hihi"))

    def test_correct(self):
        self.assertTrue(CheckDateFormat.check_date_format("2016.02.01"))

    # def test_fourteen(self):
    #     self.assertEqual([2, 7], PrimeFactor.generate(14))


if __name__ == '__main__':
    unittest.main()