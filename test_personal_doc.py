__author__ = 'Kozma Balazs'

import unittest
from donor_registration_basic_datas import Person

class PersonalDocument(unittest.TestCase):
    def test_invalid_passport(self):
        self.assertFalse(Person.get_personal_document_type("ggggg888"))

    def test_passport_plus_char(self):
        self.assertFalse(Person.get_personal_document_type("gggggg888"))

    def test_valid_passport(self):
        self.assertTrue(Person.get_personal_document_type("gggggg88"))

    def test_invalid_ID_card(self):
        self.assertFalse(Person.get_personal_document_type("88888ggg"))

    def test_ID_card_plus_char(self):
        self.assertFalse(Person.get_personal_document_type("gggggg888"))

    def test_valid_ID_card(self):
        self.assertTrue(Person.get_personal_document_type("gggggg88"))


if __name__ == '__main__':
    unittest.main()
