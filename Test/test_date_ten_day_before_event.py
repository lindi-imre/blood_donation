__author__ = 'Slezak Attila'

import unittest
from date_ten_day_before_event import DateTenDayBeforeEvent
from datetime import datetime, timedelta

class TestIsDateTenDayBeforeEvent(unittest.TestCase):
    def test_nine_day(self):
        test_date = datetime.now().date() + timedelta(days = 9)
        self.assertFalse(DateTenDayBeforeEvent.is_date_ten_day_before_event(test_date))

    def test_ten_day(self):
        test_date = datetime.now().date() + timedelta(days = 10)
        self.assertTrue(DateTenDayBeforeEvent.is_date_ten_day_before_event(test_date))

if __name__ == '__main__':
    unittest.main()
