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

    def test_april_thirtyone(self):
        self.assertFalse(CheckDateFormat.check_date_format("2014.04.31"))

    def test_september_thirtyone(self):
        self.assertFalse(CheckDateFormat.check_date_format("2014.09.31"))

    def test_february_thirty(self):
        self.assertFalse(CheckDateFormat.check_date_format("2012.02.30"))

    def test_february_twenty_nine_false(self):
        self.assertFalse(CheckDateFormat.check_date_format("2013.02.29"))

    def test_month_one_char(self):
        self.assertFalse(CheckDateFormat.check_date_format("2014.2.03"))

    def test_day_one_char(self):
        self.assertFalse(CheckDateFormat.check_date_format("2014.02.2"))

    def test_month_and_day_one_char(self):
        self.assertFalse(CheckDateFormat.check_date_format("2014.1.2"))

    def test_february_twenty_nine_true(self):
        self.assertTrue(CheckDateFormat.check_date_format("2012.02.29"))

    def test_correct(self):
        self.assertTrue(CheckDateFormat.check_date_format("2016.02.01"))



if __name__ == '__main__':
    unittest.main()