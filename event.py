__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from switch import Switch
from event_calculations import EventCalculations
import os
from save_menu import SaveMenu

class Event(object):
    @staticmethod
    def test_mod(test_data):
        test_variable = Switch.general_data_inputer(test_data)
        return test_variable

    @staticmethod
    def write_in_file(date_of_event, start_time, end_time, available_beds, planned_donor_numbers,\
                      city, address, zip_code):
        file = open("Data/donations.csv", "a", encoding='utf-8')
        file.write(str(date_of_event) + "," + str(start_time) + "," + str(end_time) + "," + str(zip_code) + ","\
                   + str(city) + "," + str(address) + "," + str(available_beds) + "," + str(planned_donor_numbers) \
                   + "\n")
        file.close()
        return

    @staticmethod
    def event_data():
        print("Please enter the following informations!")
        date_of_event = Switch.general_data_inputer(["Date of the event", "Date of the event (YYYY.MM.DD)"])
        start_time = Switch.general_data_inputer(["Start time", "Start time"])
        end_time = Switch.general_data_inputer(["End time", "End time", start_time])
        zip_code = Switch.general_data_inputer(["Zip code", "Zip code"])
        city = Switch.general_data_inputer(["City", "City"])
        address = Switch.general_data_inputer(["Address","Address"])
        available_beds = Switch.general_data_inputer(["Available beds", "Available beds"])
        planned_donor_number = Switch.general_data_inputer(["Planned donor number", "Planned donor number"])
        event_duration_time = EventCalculations.duration_in_time(start_time, end_time)
        colon_in_duration_time = str(event_duration_time).find(":")
        max_donor_number = EventCalculations.maximum_donor_number(available_beds, start_time, end_time)
        success_rate = EventCalculations.success_rate(planned_donor_number, max_donor_number)
        success_text = EventCalculations.success_text(success_rate)

        Event.write_in_file(date_of_event, start_time, end_time, zip_code, city, address, available_beds,\
                            planned_donor_number)

        os.system('cls')

        print("\n" + "-" * 32 + "\n")
        print("Details of the planned event:\n")
        print("Date of the event:", date_of_event)
        print("Start time:", start_time)
        print("End time:", end_time)
        print("Event duration time: %s hour(s) %s minute(s)" % (str(event_duration_time)[:colon_in_duration_time],
                str(event_duration_time)[colon_in_duration_time+1:colon_in_duration_time+3]))
        print("Zip code:", zip_code)
        print("City:", city)
        print("Address:", address)
        print("Available beds:", available_beds)
        print("Planned donor number:", planned_donor_number)
        print("Maximum donor number:", max_donor_number)
        print("Percent of success:", success_rate, "%")
        print("Efficiency:", success_text)
        print("\n" + "-" * 32)

        save = SaveMenu.save_menu(1)
        if save:
            Event.write_in_file(city, address, zip_code)
            print("*** Save was successfull ***")
