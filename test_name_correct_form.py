__author__ = 'Kozma Balazs'

import unittest
from name_correct_form import NameFormat

class NameFormatTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(NameFormat.name_corr_format("sdheh"))


if __name__ == '__main__':
    unittest.main()
