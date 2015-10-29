__author__ = 'Slezak Attila'

import unittest
from datetime import datetime, date
from date_is_weekday import DateIsWeekday

class TestIsWeekday(unittest.TestCase):
    def test_weekday(self):
        test_date = datetime.strptime("2015.10.29", "%Y.%m.%d").date()
        self.assertTrue(DateIsWeekday.is_date_weekday(test_date))

    def test_weekend(self):
        test_date = datetime.strptime("2015.10.31", "%Y.%m.%d").date()
        self.assertFalse(DateIsWeekday.is_date_weekday(test_date))


if __name__ == '__main__':
    unittest.main()
