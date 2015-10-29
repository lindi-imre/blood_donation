__author__ = 'Kozma Balazs'

import unittest
from name_correct_form import NameFormat


class NameFormatTest(unittest.TestCase):
    def test_variable(self):
        self.assertEqual("Sdheh", NameFormat.name_corr_format("sdheh"))

    def test_list(self):
        self.assertEqual(["Sdheh", "Maa", "Ukja"], NameFormat.name_corr_format(["sdheh", "maa", "ukja"]))

    def test_something(self):
        self.assertEqual("12", NameFormat.name_corr_format("12"))

if __name__ == '__main__':
    unittest.main()
