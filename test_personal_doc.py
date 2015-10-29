__author__ = 'Kozma Balazs'

import unittest
from donor_validations import Validations

class PersonalDocument(unittest.TestCase):
    def test_invalid_passport(self):
        self.assertFalse(Validations.validate_uniqeid("ggggg888"))

    def test_passport_plus_char(self):
        self.assertFalse(Validations.validate_uniqeid("gggggg888"))

    def test_valid_passport(self):
        self.assertTrue(Validations.validate_uniqeid("gggggg88"))

    def test_invalid_ID_card(self):
        self.assertFalse(Validations.validate_uniqeid("88888ggg"))

    def test_ID_card_plus_char(self):
        self.assertFalse(Validations.validate_uniqeid("gggggg888"))

    def test_valid_ID_card(self):
        self.assertTrue(Validations.validate_uniqeid("gggggg88"))


if __name__ == '__main__':
    unittest.main()
