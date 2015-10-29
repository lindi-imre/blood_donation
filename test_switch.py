__author__ = 'Slezak Attila'

import unittest
from switch import Switch
from datetime import datetime, date

class TestSwitch(unittest.TestCase):
    def test_date_of_the_event(self):
        self.assertIsInstance(Switch.general_data_inputer(["Date of the event", "2045.02.10", "Test"]), date)

    def test_city(self):
        self.assertEqual("Miskolc", Switch.general_data_inputer(["City", "Miskolc", "Test"]))

    def test_city2(self):
        self.assertEqual("Szerencs", Switch.general_data_inputer(["City", "szerencs", "Test"]))

    def test_zip_code(self):
        self.assertEqual("1234", Switch.general_data_inputer(["Zip code", "1234", "Test"]))

    def test_zip_code2(self):
        self.assertNotEqual("1234", Switch.general_data_inputer(["Zip code", "234", "Test"]))

    def test_zip_code_in_switcher(self):
        self.assertTrue(Switch.switcher("2234", ["Zip code"]))

    def test_zip_code_in_switcher2(self):
        self.assertFalse(Switch.switcher("0234", ["Zip code"]))

if __name__ == '__main__':
    unittest.main()
