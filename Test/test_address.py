__author__ = 'Kozma Balazs'

import unittest
from address import Address

class input_validation(unittest.TestCase):
    def test_zip_first_zero(self):
        self.assertFalse(Address.check_zip_code("0123"))

    def test_zip_string(self):
        self.assertFalse(Address.check_zip_code("sdhg"))

    def test_zip_3_dig(self):
        self.assertFalse(Address.check_zip_code("123"))

    def test_zip_valid(self):
        self.assertTrue(Address.check_zip_code("1123"))

    def test_address_short(self):
        self.assertFalse(Address.validate_address("ba"))

    def test_address_long(self):
        self.assertFalse(Address.validate_address("hajsudjfhgjauqiekrjthfgghj"))

    def test_address_valid(self):
        self.assertTrue(Address.validate_address("sfdhdrhfh"))

    def test_city_not_valid(self):
        self.assertFalse(Address.validate_city("dunaujvaros"))

    def test_city_valid(self):
        self.assertTrue(Address.validate_city("miskolc"))


if __name__ == '__main__':
    unittest.main()
