__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from switch import Switch

class Event(object):
    @staticmethod
    def test_mod(test_data):
        test_variable = Switch.general_data_inputer(test_data)
        return test_variable

    @staticmethod
    def event_data():
        if not test_data:
            test_data = ["", ""]
        date_of_event = Switch.general_data_inputer(["Date of the event"])
        zip_code = Switch.general_data_inputer(["Zip code"])
        city = Switch.general_data_inputer(["City"])
        available_beds = Switch.general_data_inputer(["Available beds"])
        planned_donor_number = Switch.general_data_inputer(["Planned donor number"])