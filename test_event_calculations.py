__author__ = 'Slezak Attila'

import unittest
from datetime import datetime
from event_calculations import EventCalculations

class TestEventCalculations(unittest.TestCase):
    def test_too_early(self):
        test_start_time = datetime.strptime("10:00", "%H:%M").time()
        test_end_time = datetime.strptime("10:59", "%H:%M").time()
        self.assertFalse(EventCalculations.end_time_after_start_time(test_start_time, test_end_time))

    def test_correct(self):
        test_start_time = datetime.strptime("10:00", "%H:%M").time()
        test_end_time = datetime.strptime("11:00", "%H:%M").time()
        self.assertTrue(EventCalculations.end_time_after_start_time(test_start_time, test_end_time))


if __name__ == '__main__':
    unittest.main()
