__author__ = 'Slezak Attila'

import unittest
from check_time_format import CheckTimeFormat

class TestTimeFormat(unittest.TestCase):
    def test_string(self):
        self.assertFalse(CheckTimeFormat.check_time_form("a"))

    def test_string_format(self):
        self.assertFalse(CheckTimeFormat.check_time_form("aa:bb"))

    def test_too_big_hours(self):
        self.assertFalse(CheckTimeFormat.check_time_form("24:00"))

    def test_too_big_minutes(self):
        self.assertFalse(CheckTimeFormat.check_time_form("12:60"))

    def test_correct_format(self):
        self.assertTrue(CheckTimeFormat.check_time_form("12:34"))

    def test_bad_format(self):
        self.assertTrue(CheckTimeFormat.check_time_form("1:2"))

if __name__ == '__main__':
    unittest.main()
