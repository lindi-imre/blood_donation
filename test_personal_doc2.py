__author__ = 'Kozma Balazs'

import unittest
from donor_validations import Validations

class ValidateGender(unittest.TestCase):
    def test_plus_char_male(self):
        self.assertFalse(Validations.validate_gender("malle"))

    def test_invalid_input_male(self):
        self.assertFalse(Validations.validate_gender("ferfi"))

    def test_valid_male(self):
        self.assertTrue(Validations.validate_gender("m"))

    def test_plus_char_female(self):
        self.assertFalse(Validations.validate_gender("femmale"))

    def test_invalid_input_female(self):
        self.assertFalse(Validations.validate_gender("no"))

    def test_valid_female(self):
        self.assertTrue(Validations.validate_gender("f"))

if __name__ == '__main__':
    unittest.main()
