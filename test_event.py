__author__ = 'Slezak Attila'

import unittest
from datetime import datetime, date
from donor_registration_dates import donor_dates
from event import Event

class TestEvent(unittest.TestCase):
    def test_date_of_event(self):
        self.assertIsInstance(Event.test_mod(["Date of the event", "2015.02.02", "Test"]), date)

    def test_zip_code(self):
        self.assertEqual("1234", Event.test_mod(["Zip code", "1234", "Test"]), date)

    def test_city(self):
        self.assertEqual("Miskolc", Event.test_mod(["City", "Miskolc", "Test"]), date)

    def test_address(self):
        self.assertEqual("Miskolc", Event.test_mod(["Address", "Miskolc", "Test"]), date)

    def test_available_beds(self):
        self.assertEqual("Miskolc", Event.test_mod(["Available beds", "Miskolc", "Test"]), date)

    def test_planned_donor_number(self):
        self.assertEqual("Miskolc", Event.test_mod(["Planned donor number", "Miskolc", "Test"]), date)

if __name__ == '__main__':
    unittest.main()
