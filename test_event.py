__author__ = 'Slezak Attila'

import unittest
from datetime import datetime, date, timedelta
from donor_registration_dates import donor_dates
from event import Event

class TestEvent(unittest.TestCase):
    def test_date_of_event(self):
        self.assertIsInstance(Event.test_mod(["Date of the event", "2045.02.10", "Test"]), date)

    def test_nine_day(self):
        test_date = datetime.now().date() + timedelta(days = 9)
        self.assertFalse(Event.test_mod(["Date of the event", str(test_date).replace("-","."), "Test"]))

    def test_ten_day(self):
        test_date = datetime.now().date() + timedelta(days = 11)
        self.assertTrue(Event.test_mod(["Date of the event", str(test_date).replace("-","."), "Test"]))

    def test_weekday(self):
        self.assertTrue(Event.test_mod(["Date of the event", "2045.02.10", "Test"]))

    def test_weekend(self):
        self.assertFalse(Event.test_mod(["Date of the event", "2045.02.11", "Test"]))

    def test_zip_code(self):
        self.assertEqual("1234", Event.test_mod(["Zip code", "1234", "Test"]))

    def test_city(self):
        self.assertEqual("Miskolc", Event.test_mod(["City", "mIskolc", "Test"]))

    def test_address(self):
        self.assertEqual("Aaa", Event.test_mod(["Address", "aaa", "Test"]))

    def test_available_beds(self):
        self.assertEqual("20", Event.test_mod(["Available beds", "20", "Test"]))

    def test_planned_donor_number(self):
        self.assertEqual("31", Event.test_mod(["Planned donor number", "31", "Test"]))

if __name__ == '__main__':
    unittest.main()
