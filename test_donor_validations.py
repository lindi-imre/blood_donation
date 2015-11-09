__author__ = 'Slezak Attila'

import unittest
from donor_validations import Validations
from datetime import datetime, timedelta

class TestValidations(unittest.TestCase):
    def test_name_incorrect(self):
        self.assertFalse(Validations.check_name("123"))

    def test_name_one_name(self):
        self.assertFalse(Validations.check_name("John "))

    def test_name_correct(self):
        self.assertTrue(Validations.check_name(" Abraham  Lincoln "))

    def test_weight_alpha(self):
        self.assertFalse(Validations.check_weight("Fifty kilo"))

    def test_weight_fourtynine(self):
        with self.assertRaises(SystemExit):
            Validations.check_weight("49")

    def test_weight_fifty(self):
        self.assertTrue(Validations.check_weight("50"))

    def test_gender_incorrect(self):
        self.assertFalse(Validations.validate_gender("g"))

    def test_gender_number(self):
        self.assertFalse(Validations.validate_gender("12"))

    def test_gender_male(self):
        self.assertEqual("Male", Validations.validate_gender("male"))

    def test_gender_male_short(self):
        self.assertEqual("Male", Validations.validate_gender("m"))

    def test_gender_female_short(self):
        self.assertEqual("Female", Validations.validate_gender("f"))

    def test_uniqueid_incorrect(self):
        self.assertFalse(Validations.validate_uniqeid("never"))

    def test_uniqueid_id(self):
        self.assertEqual(["Identity card", "123456AB"], Validations.validate_uniqeid("123456AB"))

    def test_uniqueid_passport(self):
        self.assertEqual(["Passport", "ABCDEF12"], Validations.validate_uniqeid("ABCDEF12"))

    def test_exp_uniqueid_old(self):
        yesterday = datetime.now().date() - timedelta(days=1)
        with self.assertRaises(SystemExit):
            Validations.exp_uniqueid(yesterday)

    def test_exp_uniqueid_valid(self):
        today = datetime.now().date()
        self.assertTrue(Validations.exp_uniqueid(today))

    def test_last_donation_within_threemonth(self):
        eighty_eight_days_ago = datetime.now().date() - timedelta(days=88)
        with self.assertRaises(SystemExit):
            Validations.last_donation_more_than_three_month_ago(eighty_eight_days_ago)

    def test_last_donation_out_of_threemonth(self):
        ninetyfive_days_ago = datetime.now().date() - timedelta(days=95)
        self.assertTrue(Validations.last_donation_more_than_three_month_ago(ninetyfive_days_ago))

    def test_last_donation_today_is_dec31(self):
        last_donation_date = datetime.strptime("2015.09.30", "%Y.%m.%d").date()
        today_dec31 = datetime.strptime("2015.12.31", "%Y.%m.%d").date()
        self.assertTrue(Validations.last_donation_more_than_three_month_ago([last_donation_date, today_dec31]))

    def test_last_donation_today_is_may29(self):
        last_donation_date = datetime.strptime("2015.02.28", "%Y.%m.%d").date()
        today_may29 = datetime.strptime("2015.05.29", "%Y.%m.%d").date()
        self.assertTrue(Validations.last_donation_more_than_three_month_ago([last_donation_date, today_may29]))

    def test_last_donation_today_is_may31_exit(self):
        ninetyfive_days_ago = datetime.now().date() - timedelta(days=95)
        today_may31 = datetime.strptime("2015.05.31", "%Y.%m.%d").date()
        with self.assertRaises(SystemExit):
            Validations.last_donation_more_than_three_month_ago([ninetyfive_days_ago, today_may31])


    def test_sick_incorrect(self):
        self.assertFalse(Validations.check_arusicklastmonth("asdf"))

    def test_sick_no(self):
        self.assertTrue(Validations.check_arusicklastmonth("No"))

    def test_sick_yes(self):
        with self.assertRaises(SystemExit):
            Validations.check_arusicklastmonth("yes")

    def test_mobile_number_incorrect_one_letter(self):
        self.assertFalse(Validations.validate_mobil_number("a"))

    def test_mobile_number_incorrect(self):
        self.assertFalse(Validations.validate_mobil_number("abcdefghijk"))

    def test_mobile_number_little_mistake(self):
        self.assertFalse(Validations.validate_mobil_number("0670a234567"))

    def test_mobile_number_correct06(self):
        self.assertTrue(Validations.validate_mobil_number("06701234567"))

    def test_mobile_number_correct36(self):
        self.assertTrue(Validations.validate_mobil_number("+36701234567"))

    def test_hmg_generate80(self):
        self.assertLess(79, Validations.rnd_hmg_generate())

    def test_hmg_generate200(self):
        self.assertGreater(201, Validations.rnd_hmg_generate())

    def test_email_incorrect(self):
        self.assertFalse(Validations.validate_email("sadf"))

    def test_email_not_enough_charhu(self):
        self.assertFalse(Validations.validate_email("a@.hu"))

    def test_email_not_enough_charcom(self):
        self.assertFalse(Validations.validate_email("a@.com"))

    def test_email_correcthu(self):
        self.assertTrue(Validations.validate_email("asdf@dfgaf.hu"))

    def test_email_correctcom(self):
        self.assertTrue(Validations.validate_email("a@af.com"))

    def test_birthdate(self):
        test_date = datetime.strptime("1997.11.09", "%Y.%m.%d").date()
        self.assertTrue(Validations.validate_birthdate(test_date))

    def test_birthdate2(self):
        test_date = datetime.now().date().replace(year=datetime.now().date().year - 18)
        self.assertTrue(Validations.validate_birthdate(test_date))

    def test_birthdate3(self):
        test_date = datetime.now().date().replace(year=datetime.now().date().year - 18)
        test_date += timedelta(days=1)
        with self.assertRaises(SystemExit):
            Validations.validate_birthdate(test_date)

    def test_age_of_donor_one_day_to_eightteen(self):
        test_date = datetime.now().date().replace(year=datetime.now().date().year - 18)
        test_date += timedelta(days=1)
        self.assertEqual(17, Validations.count_age_of_donor(test_date))

    def test_age_of_donor_just_eightteen(self):
        test_date = datetime.now().date().replace(year=datetime.now().date().year - 18)
        self.assertEqual(18, Validations.count_age_of_donor(test_date))


    # def test_hmg_valid_yes(self):
    #     self.assertTrue(Validations.validate_hmg())

    # def test_hmg_valid_yes(self):
    #     with self.assertRaises(SystemExit):
    #         Validations.validate_hmg()

    # def test_hmg_valid_no(self):
    #     self.assertFalse(Validations.validate_hmg("109"))

if __name__ == '__main__':
    unittest.main()
