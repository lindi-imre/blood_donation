__author__ = 'Péter'

from switch import Switch
from donor_validations import Validations

class Person(object):
    @staticmethod
    def donor_register_app():
        name = Switch.general_data_inputer(["Name", "Enter your full name"])
        weight = Switch.general_data_inputer(["Weight", "Weight"])
        gender = Switch.general_data_inputer(["Gender", "Gender"])
        uniqeid = Switch.general_data_inputer(["Uniqeid", "Unique identifier number"])
        sick = Switch.general_data_inputer(["Sick", "Were you sick in the last month?"])
        phone_number = Switch.general_data_inputer(["Phone number", "Mobile number"])
        email = Switch.general_data_inputer(["Email", "E-mail adress"])
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
        print("Hemoglobin level: ", hemoglobin)
        print("\n" + "-" * 32)

