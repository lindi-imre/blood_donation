__author__ = 'Péter'

from switch import Switch
from donor_validations import Validations

class Person(object):
    @staticmethod
    def donor_register_app():
        name = Switch.general_data_inputer(["Name"])
        weight = Switch.general_data_inputer(["Weight"])
        gender = Switch.general_data_inputer(["Gender"])
        uniqeid = Switch.general_data_inputer(["Uniqeid"])

        sick = Switch.general_data_inputer(["Sick"])
        phone_number = Switch.general_data_inputer(["Phone number"])

        email = Switch.general_data_inputer(["Email"])
        hemoglobin = Validations.validate_hmg()

        print("\n" + "-" * 32 + "\n")
        print("Donor's data:\n")
        print("Name: ", name)
        print("Weight: ", weight)
        print("Gender: ", gender)
        print("Type of donor's ID: %s\nNumber of donor's ID: %s" % (uniqeid[0], uniqeid[1]))
        print("Were donor sick last month: ", sick)
        print("Phone number: ", phone_number)
        print("Email: ", email)
        print("Haemoglobin level: ", hemoglobin)
        print("\n" + "-" * 32)

