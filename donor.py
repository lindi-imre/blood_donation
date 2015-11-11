__author__ = 'Péter'
# -- coding: utf-8 --

from switch import Switch
from donor_validations import Validations
import os
from save_menu import SaveMenu


class Person(object):
    @staticmethod
    def test_mod(test_data):
        test_variable = Switch.general_data_inputer(test_data)
        return test_variable

    @staticmethod
    def write_in_file(name,weight,gender,birth_date,last_donation,sick,uniqeid,expuniqeid,blood_type,hemoglobin,email,phone_number):
        file = open("Data/donors.csv", "a", encoding='utf-8')
        file.write(str(name) + "," + str(weight) + "," + str(gender) + "," + str(birth_date) + "," + str(last_donation) + "," \
        + str(sick) + "," + str(uniqeid[1]) + "," + str(expuniqeid) + "," + str(blood_type) + "," + str(hemoglobin) + "," \
        + str(email) + "," + str(phone_number) + "\n")
        file.close()
        return

    @staticmethod
    def donor_register_app():
        print("Please enter the following informations!")
        name = Switch.general_data_inputer(["Donor's name", "Enter your full name"])
        birth_date = Switch.general_data_inputer(["Birth date", "Birth date (YYYY.MM.DD)"])
        weight = Switch.general_data_inputer(["Weight", "Weight"])
        gender = Switch.general_data_inputer(["Gender", "Gender"])
        uniqeid = Switch.general_data_inputer(["Unique ID", "Unique identifier number"])
        expuniqeid = Switch.general_data_inputer(["Expiration of ID", "Expiration date of your ID"])
        blood_type = Switch.general_data_inputer(["Blood type", "Blood type (A, B, AB, 0 with +/-)"])
        last_donation = Switch.general_data_inputer(["Last donation date", "Last donation date (type 'never' if never before)"])
        sick = Switch.general_data_inputer(["Sickness", "Were you sick in the last month?"])
        phone_number = Switch.general_data_inputer(["Mobile number", "Mobile number"])
        email = Switch.general_data_inputer(["Email", "E-mail address"])
        age_of_donor = Validations.count_age_of_donor(birth_date)
        hemoglobin = Validations.validate_hmg()

        os.system('cls')
        #Useless prints actual moment
        """
        print("\n" + "-" * 32 + "\n")
        print("Donor's data:\n")
        print("Name:", name)
        print("Birth date: %s - %d years old" % (birth_date, age_of_donor))
        print("Weight:", weight, "kg")
        print("Gender:", gender)
        print("Type of donor's ID: %s\nNumber of donor's ID: %s" % (uniqeid[0], uniqeid[1]))
        print("Expiration of donor's ID: %s" % expuniqeid)
        print("Last donation date: %s" % last_donation)
        print("Were donor sick last month:", Validations.check_arusicklastmonth(sick))
        print("Phone number:", phone_number)
        print("Email:", email)
        print("Hemoglobin level:", Validations.validate_hmg())
        """
        print("\n" + "-" * 32)

        save = SaveMenu.save_menu(1)
        if save:
            Person.write_in_file(name,weight,gender,birth_date,last_donation,sick,uniqeid,expuniqeid,blood_type,hemoglobin,email,phone_number)
