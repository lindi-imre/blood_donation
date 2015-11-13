__author__ = 'Péter'
# -- coding: utf-8 --

from switch import Switch
from donor_validations import Validations
from save_menu_old import SaveMenuOldFashioned
import os
import time
import getpass

user_name = getpass.getuser()
if os.path.isfile("C:/Users/" + user_name + "/AppData/Local/Programs/Python/Python35-32/Lib/site-packages/colorama-0.3.3-py3.5.egg"):
    from save_menu import SaveMenu


class Person(object):
    @staticmethod
    def test_mod(test_data):
        test_variable = Switch.general_data_inputer(test_data)
        return test_variable

    @staticmethod
    def write_in_file(name,weight,gender,birth_date,last_donation,sick,uniqeid,expuniqeid,blood_type,hemoglobin,email,phone_number,suitable):
        file = open("Data/donors.csv", "a", encoding='utf-8')
        file.write(str(name) + "," + str(weight[0]) + "," + str(gender) + "," + str(birth_date[0]) + "," + str(last_donation[0]) + "," \
        + str(sick[0]) + "," + str(uniqeid[1]) + "," + str(expuniqeid[0]) + "," + str(blood_type) + "," + str(hemoglobin[0]) + "," \
        + str(email) + "," + str(phone_number) + "," + str(suitable[0]) + "\n")

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
        age_of_donor = Validations.count_age_of_donor(birth_date[0])
        hemoglobin = Validations.validate_hmg()
        suitable = Validations.donor_suitable([birth_date, weight, last_donation, sick, hemoglobin])

        os.system('cls')

        print("\n" + "-" * 32 + "\n")
        print("Donor's data:\n")
        print("Name:", name)
        print("Birth date: %s - %d years old" % (birth_date[0], age_of_donor))
        print("Weight:", weight[0], "kg")
        print("Gender:", gender)
        print("Type of donor's ID: %s\nNumber of donor's ID: %s" % (uniqeid[0], uniqeid[1]))
        print("Expiration of donor's ID: %s" % expuniqeid[0])
        print("Last donation date: %s" % last_donation[0])
        print("Were donor sick last month:", sick[0])
        print("Phone number:", phone_number)
        print("Email:", email)
        print("Hemoglobin level:", hemoglobin[0],"\n")
        print(suitable[1])
        print("\n" + "-" * 32)

        if os.path.isfile("C:/Users/" + user_name + "/AppData/Local/Programs/Python/Python35-32/Lib/site-packages/colorama-0.3.3-py3.5.egg"):
            save = SaveMenu.save_menu(2, 24)
        else:
            save = SaveMenuOldFashioned.save_menu(2, "Do you want to save?")
            print()
        if save:
            Person.write_in_file(name, weight, gender, birth_date, last_donation, sick, uniqeid, expuniqeid, blood_type\
                                 , hemoglobin, email, phone_number, suitable)
            print("Save was successful!")
            time.sleep(2)
