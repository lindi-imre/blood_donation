__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from switch import Switch
from event_calculations import EventCalculations

class Event(object):
    @staticmethod
    def test_mod(test_data):
        test_variable = Switch.general_data_inputer(test_data)
        return test_variable

    @staticmethod
    def event_data():
        date_of_event = Switch.general_data_inputer(["Event date", "Date of the event (YYYY.MM.DD)"])
        start_time = Switch.general_data_inputer(["Start time", "Start time"])
        end_time = Switch.general_data_inputer(["End time", "End time", start_time])
        zip_code = Switch.general_data_inputer(["Zip code", "Zip code"])
        city = Switch.general_data_inputer(["City", "City"])
        available_beds = Switch.general_data_inputer(["Available beds", "Available beds"])
        planned_donor_number = Switch.general_data_inputer(["Planned donor num", "Planned donor number"])
        event_duration_time = EventCalculations.duration_in_time(start_time, end_time)
        colon_in_duration_time = str(event_duration_time).find(":")
        max_donor_number = EventCalculations.maximum_donor_number(available_beds, start_time, end_time)
        success_rate = EventCalculations.success_rate(planned_donor_number, max_donor_number)
        success_text = EventCalculations.success_text(success_rate)

        print("\n" + "-" * 32 + "\n")
        print("Details of the planned event:\n")
        print("Date of the event: ", date_of_event)
        print("Start time: ", start_time)
        print("End time: ", end_time)
        print("Event duration time: %s hour(s) %s minute(s)" % (str(event_duration_time)[:colon_in_duration_time],
                str(event_duration_time)[colon_in_duration_time+1:colon_in_duration_time+3]))
        print("Zip code: ", zip_code)
        print("City: ", city)
        print("Available beds: ", available_beds)
        print("Planned donor number: ", planned_donor_number)
        print("Maximum donor number: ", max_donor_number)
        print("Percent of success: ", success_rate, "%")
        print("Efficiency: ", success_text)
        print("\n" + "-" * 32)