__author__ = 'Péter'
# -- coding: utf-8 --

from switch import Switch
from donor_validations import Validations

class Person(object):
    @staticmethod
    def test_mod(test_data):
        test_variable = Switch.general_data_inputer(test_data)
        return test_variable

    @staticmethod
    def donor_register_app():
        name = Switch.general_data_inputer(["Donor's name", "Enter your full name"])
        weight = Switch.general_data_inputer(["Weight", "Weight"])
        gender = Switch.general_data_inputer(["Gender", "Gender"])
        uniqeid = Switch.general_data_inputer(["Unique ID", "Unique identifier number"])
        sick = Switch.general_data_inputer(["Sickness", "Were you sick in the last month?"])
        phone_number = Switch.general_data_inputer(["Mobile number", "Mobile number"])
        email = Switch.general_data_inputer(["Email", "E-mail address"])
        hemoglobin = Validations.validate_hmg()

        print("\n" + "-" * 32 + "\n")
        print("Donor's data:\n")
        print("Name: ", name)
        print("Weight: ", weight, "kg")
        print("Gender: ", gender)
        print("Type of donor's ID: %s\nNumber of donor's ID: %s" % (uniqeid[0], uniqeid[1]))
        print("Were donor sick last month: ", sick)
        print("Phone number: ", phone_number)
        print("Email: ", email)
        print("Hemoglobin level: ", hemoglobin)
        print("\n" + "-" * 32)

