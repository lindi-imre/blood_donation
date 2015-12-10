__author__ = 'Slezak Attila'

import unittest
from file_operator import FileOperator

class TestFileOperator(unittest.TestCase):
    # def test_csv_or_db_if_db(self):
    #     self.assertEqual('db', FileOperator.csv_or_db('../app.config'))

    # You have to begin file = open() paths with '../' in File.Operator.create_database() to get work this:
    # def test_create_db(self):
    #     self.assertTrue(FileOperator.create_database())

    # def test_save_event_db(self):
    #     header = "id,date_of_event,start_time,end_time,zip_code,city,address,number_of_available_beds," + \
    #                 "planned_donor_number,final_donor_number\n"
    #     self.assertTrue(FileOperator.save_new_data_db(["'2015-12-01'", "'10:00'", "'12:00'", "'1234'", "'Miskolc'", "'Egy Utca'", "'30'", "'80'", "'60'"], header, "../Data/donations.csv"))
    #
    # def test_save_donor_db(self):
    #     header = "name,weight,gender,date_of_birth,last_donation,last_month_sickness,unique_identifier," + \
    #                  "expiration_of_id,blood_type,hemoglobin,email,mobil,is_suitable"
    #     self.assertTrue(FileOperator.save_new_data_db(["'Nevem Senki'", "'77'", "'Male'", "'1971-04-03'", "'2014-03-03'", "'No'", "'444557SA'", "'2017-03-05'", "'A+'", "'140'", "'mynameis@nobody.com'", "'06701122112'", "'Yes'"], header, "../Data/donors.csv"))
    #
    # def test_save_event_csv(self):
    #     header = "id,date_of_event,start_time,end_time,zip_code,city,address,number_of_available_beds," + \
    #                 "planned_donor_number,final_donor_number\n"
    #     self.assertTrue(FileOperator.save_new_data_csv(["2015.12.01", "10:00", "12:00", "1234", "Miskolc", "Egy Utca", "30", "80", "60"], header, "../Data/donations.csv"))
    #
    # def test_save_donor_csv(self):
    #     header = "name,weight,gender,date_of_birth,last_donation,last_month_sickness,unique_identifier," + \
    #                  "expiration_of_id,blood_type,hemoglobin,email,mobil,is_suitable"
    #     self.assertTrue(FileOperator.save_new_data_csv(["Nevem Senki", "77", "Male", "1971.04.03", "2014.03.03", "No", "444557SA", "2017.03.05", "A+", "140", "mynameis@nobody.com", "06701122112", "Yes"], header, "../Data/donors.csv"))

if __name__ == '__main__':
    unittest.main()
