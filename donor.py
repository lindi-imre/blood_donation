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
        phone_number = Switch.general_data_inputer(["Phone_number"])

        email = Switch.general_data_inputer(["Email"])
        hemoglobin = Validations.validate_hmg()

        print(name)
        print(weight)
        print(gender)
        print(uniqeid)
        print(sick)
        print(phone_number)
        print(email)
        print(hemoglobin)

