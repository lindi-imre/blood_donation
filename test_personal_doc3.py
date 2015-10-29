__author__ = 'Kozma Balazs'

import unittest
from donor_validations import Validations

class ValidateWeight(unittest.TestCase):
    def test_weight_string(self):
        self.assertFalse(Validations.check_weight("otven"))

    def test_below_50(self):
        self.assertFalse(Validations.check_weight(49))

    def test_equal_50(self):
        self.assertFalse(Validations.check_weight(50))

    def test_float(self):
        self.assertFalse(Validations.check_weight(55.6))

    def test_valid_weight(self):
        self.assertTrue(Validations.check_weight(60))


if __name__ == '__main__':
    unittest.main()
