__author__ = 'Péter'

from switch import Switch

class Person():
    name = Switch.general_data_inputer(["Name"])
    weight = Switch.general_data_inputer(["Weight"])
    gender = Switch.general_data_inputer(["Gender"])

    uniqeid = Switch.general_data_inputer(["Uniqeid"])

