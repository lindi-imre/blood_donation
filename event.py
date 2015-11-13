__author__ = 'Slezak Attila'
# -- coding: utf-8 --

import os.path
from switch import Switch
from event_calculations import EventCalculations
from save_menu_old import SaveMenuOldFashioned
import os
import time
import getpass

user_name = getpass.getuser()
if os.path.isfile("C:/Users/" + user_name + "/AppData/Local/Programs/Python/Python35-32/Lib/site-packages/colorama-0.3.3-py3.5.egg"):
    from save_menu import SaveMenu


class Event(object):
    @staticmethod
    def test_mod(test_data):
        test_variable = Switch.general_data_inputer(test_data)
        return test_variable

    @staticmethod
    def write_in_file(every_file_data):
        header = "id,date_of_event,start_time,end_time,zip_code,city,address,number_of_available_beds,"
        header += "planned_donor_number,final_donor_number\n"
        header_exists = True
        next_id = 1
        id_s = []
        file = open("Data/donations.csv", "r", encoding='utf-8')
        one_line = file.readline()
        for line in file:
            first_colon = line.find(",")
            id_s.append(line[0:first_colon])
        while str(next_id) in id_s:
            next_id += 1
        file.seek(0)
        whole_file = file.read()
        file.close()
        if one_line != header:
            header_exists = False
        if not header_exists:
            file = open("Data/donations.csv", "w", encoding='utf-8')
            file.write(header)
            file.write(whole_file)
            file.close()
        file = open("Data/donations.csv", "a", encoding='utf-8')
        first = True
        for one_data in every_file_data:
            if first:
                file.write("\n" + str(next_id) + "," + str(one_data))
                first = False
            else:
                file.write("," + str(one_data))
        # file.write("\n")
        file.close()
        return


    @staticmethod
    def event_data():
        print("Please enter the following informations!")
        date_of_event = Switch.general_data_inputer(["Date of the event", "Date of the event (YYYY.MM.DD)"])
        start_time = Switch.general_data_inputer(["Start time", "Start time (hh:mm)"])
        end_time = Switch.general_data_inputer(["End time", "End time (hh:mm)", start_time])
        zip_code = Switch.general_data_inputer(["Zip code", "Zip code"])
        city = Switch.general_data_inputer(["City", "City"])
        address = Switch.general_data_inputer(["Address", "Address"])
        available_beds = Switch.general_data_inputer(["Available beds", "Available beds"])
        planned_donor_number = Switch.general_data_inputer(["Planned donor number", "Planned donor number"])
        event_duration_time = EventCalculations.duration_in_time(start_time, end_time)
        colon_in_duration_time = str(event_duration_time).find(":")
        final_donor_number = EventCalculations.maximum_donor_number(available_beds, start_time, end_time)
        success_rate = EventCalculations.success_rate(planned_donor_number, final_donor_number)
        success_text = EventCalculations.success_text(success_rate)

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
        print("Maximum donor number:", final_donor_number)
        print("Percent of success:", success_rate, "%")
        print("Efficiency:", success_text)
        print("\n" + "-" * 32)

        if os.path.isfile("C:/Users/" + user_name + "/AppData/Local/Programs/Python/Python35-32/Lib/site-packages/colorama-0.3.3-py3.5.egg"):
            save = SaveMenu.save_menu(2,21)
        else:
            save = SaveMenuOldFashioned.save_menu(2,21)
            print()
        if save:
            every_file_data = [str(date_of_event).replace("-", "."), str(start_time)[:len(str(start_time))-3],\
                               str(end_time)[:len(str(end_time))-3], zip_code, city, address, available_beds, \
                               planned_donor_number, final_donor_number]
            Event.write_in_file(every_file_data)
            print("Save was successful!")
            time.sleep(3)

