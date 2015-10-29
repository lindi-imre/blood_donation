__author__ = 'Imre'

from donor_registration_basic_datas import Person
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(80, Person.checkweight(80))


if __name__ == '__main__':
    unittest.main()
