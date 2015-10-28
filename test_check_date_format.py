__author__ = 'Slezak Attila'
# -- coding: utf-8 --

import unittest
from check_date_format import CheckDateFormat

class CheckDateFormatTest(unittest.TestCase):
    def test_alphabet(self):
        self.assertFalse(CheckDateFormat.check_date_format("Hihi"))

    def test_alphanumeric(self):
        self.assertFalse(CheckDateFormat.check_date_format("2014agd"))

    def test_too_much_number(self):
        self.assertFalse(CheckDateFormat.check_date_format("2014.123.12"))

    def test_too_big_month_number(self):
        self.assertFalse(CheckDateFormat.check_date_format("2014.13.03"))

    def test_too_big_day_number(self):
        self.assertFalse(CheckDateFormat.check_date_format("2014.02.32"))

    def test_correct(self):
        self.assertTrue(CheckDateFormat.check_date_format("2016.02.01"))


if __name__ == '__main__':
    unittest.main()