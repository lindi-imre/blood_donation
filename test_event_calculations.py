__author__ = 'Slezak Attila'

import unittest
from datetime import datetime, timedelta
from event_calculations import EventCalculations

class TestEventCalculations(unittest.TestCase):
    def test_too_early(self):
        test_start_time = datetime.strptime("10:00", "%H:%M").time()
        test_end_time = datetime.strptime("10:59", "%H:%M").time()
        self.assertFalse(EventCalculations.end_time_after_start_time(test_end_time, test_start_time))

    def test_correct(self):
        test_start_time = datetime.strptime("10:00", "%H:%M").time()
        test_end_time = datetime.strptime("11:00", "%H:%M").time()
        self.assertTrue(EventCalculations.end_time_after_start_time(test_end_time,test_start_time))

    def test_duration_is_thirtyminutes(self):
        test_start_time = datetime.strptime("10:00", "%H:%M").time()
        test_end_time = datetime.strptime("10:30", "%H:%M").time()
        self.assertEqual(timedelta(seconds=1800), EventCalculations.duration_in_time(test_start_time, test_end_time))

    def test_duration_is_one_hour(self):
        test_start_time = datetime.strptime("10:00", "%H:%M").time()
        test_end_time = datetime.strptime("11:00", "%H:%M").time()
        self.assertEqual(timedelta(seconds=3600), EventCalculations.duration_in_time(test_start_time, test_end_time))

    def test_time_to_datetime(self):
        test_time = datetime.strptime("10:00", "%H:%M").time()
        self.assertIsInstance(EventCalculations.time_to_datetime(test_time), datetime)

    def test_time_to_datetime(self):
        test_start_time = datetime.strptime("10:00", "%H:%M").time()
        test_end_time = datetime.strptime("11:30", "%H:%M").time()
        self.assertEqual(50, EventCalculations.maximum_donor_number(25, test_start_time, test_end_time))

    def test_time_to_datetime(self):
        test_start_time = datetime.strptime("10:00", "%H:%M").time()
        test_end_time = datetime.strptime("15:40", "%H:%M").time()
        self.assertEqual(300, EventCalculations.maximum_donor_number(30, test_start_time, test_end_time))

    def test_success_rate(self):
        self.assertEqual(40, EventCalculations.success_rate("100", "40"))

    def test_success_rate_two(self):
        self.assertEqual(210, EventCalculations.success_rate("20", "42"))

    def test_success_text_one(self):
        self.assertEqual("Unsuccessful, not worths to organise there again...", EventCalculations.success_text(19))

    def test_success_text_two(self):
        self.assertEqual("Normal event.", EventCalculations.success_text(20))

    def test_success_text_three(self):
        self.assertEqual("Successful!", EventCalculations.success_text(75))

    def test_success_text_four(self):
        self.assertEqual("Outstanding!", EventCalculations.success_text(110.1))

if __name__ == '__main__':
    unittest.main()
