__author__ = 'Kozma Balazs'

import unittest
from check_if_positive_int import CheckIfPositiveInteger


class TestPositiveInt(unittest.TestCase):
    def test_string(self):
        self.assertFalse(CheckIfPositiveInteger.check_if_positive_integer("b,ah"))

    def test_float(self):
        self.assertFalse(CheckIfPositiveInteger.check_if_positive_integer(3.5))

    def test_zero(self):
        self.assertFalse(CheckIfPositiveInteger.check_if_positive_integer(0))

    def test_digitstring(self):
        self.assertTrue(CheckIfPositiveInteger.check_if_positive_integer("2"))

    def test_int(self):
        self.assertTrue(CheckIfPositiveInteger.check_if_positive_integer(2))


if __name__ == '__main__':
    unittest.main()
