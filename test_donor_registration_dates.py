__author__ = 'Slezak Attila'

import unittest
from donor_registration_dates import donor_dates
from datetime import datetime

class TestDonorRegistrationDates(unittest.TestCase):
    def test_correct_date(self):
        datum = datetime.strptime("2015.01.02.", "%Y.%m.%d.").date()
        self.assertEqual(datum, donor_dates.get_date("2015.01.02."))

    # def test_correct_dateformat(self):
    #     self.assertIsInstance(donor_dates.get_date("2015.02.02."), datetime.date())

    def test_correct_time(self):
        checktime = datetime.strptime("12:34", "%H:%M").time()
        self.assertEqual(checktime, donor_dates.get_time("12:34"))

if __name__ == '__main__':
    unittest.main()
