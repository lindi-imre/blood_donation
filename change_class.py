__author__ = 'Péter'
# -- coding: utf-8 --

import os
import csv
from msvcrt import getch
from donor_object import DonorObject
from event_object import EventObject
from change_options_menu import ChangeOptionsMenu
from switch import Switch
from event_calculations import EventCalculations
from donor_validations import Validations


class ChangeClass(object):
    change_select_arrow = -1

    @staticmethod
    def search_in_ids(id):
        id = input("Search ID: ")
        original = []
        changed = []
        if id.isdigit():
            file = open("Data/donations.csv", "r", encoding="utf-8")
            reader = csv.reader(file)
            for line in reader:
                if len(line) != 0 and id == line[0]:
                    original.append(EventObject(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9]))
                    changed.append(EventObject(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9]))
            file.close()
            if original:
                ChangeClass.change_process_event(original,changed)
            else:
                print("Not included in the database.")
        elif (id[:6].isdigit() and id[6:8].isalpha() and len(id) == 8) or (id[:6].isalpha() and id[6:8].isdigit() and len(id) == 8):
            file = open("Data/donors.csv", "r", encoding="utf-8")
            reader = csv.reader(file)
            for line in reader:
                if len(line) != 0 and id.upper() == line[6].upper():
                    original.append(DonorObject(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]))
                    changed.append(DonorObject(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]))
            file.close()
            if original:
                ChangeClass.change_process_donor(original,changed)
            else:
                print("Not included in the database.")
        else:
            print("The input is not correct.")

    @staticmethod
    def change_process_event(original, changed):
        header = ["Date of the event","Start time","End time","Zip code","City","Address","Available beds",
                  "Planned donor number","Final donor number"]
        which_result = 0
        result_number = len(original)
        if result_number > 1:
            print("There are " + str(result_number) + " results:")
        else:
            print("The result:")
        print("-" * 52)
        for i in range(result_number):
            ChangeClass.print_preprocessor_event(original,0,header,i,-1)

        if result_number > 1:
            print("Which result would you like to change?")
            which_result = int(input("Please give the result serial number (or 0 if none):"))
            if which_result == 0:
                return False
            else:
                os.system('cls')
                print("-" * 52)
                which_result -= 1
                ChangeClass.print_preprocessor_event(original,0,header,which_result,-1)

        menu_number = 3
        while True:
            print("Would you like to change any of the data of this event?")
            select = ChangeOptionsMenu.change_options(2, "  ", menu_number)
            print()

            if select == 1:
                changed[which_result].date_of_event = Switch.general_data_inputer([header[0],\
                                "Date of the event (YYYY.MM.DD)",original[which_result].date_of_event,"Change"])
                changed[which_result].start_time = Switch.general_data_inputer([header[1],"Start time (hh:mm)",\
                                original[which_result].start_time,"Change"])
                changed[which_result].end_time = Switch.general_data_inputer([header[2],"End time (hh:mm)",\
                                changed[which_result].start_time,original[which_result].end_time,"Change"])
                changed[which_result].zip_code = Switch.general_data_inputer([header[3],\
                                header[3],original[which_result].zip_code,"Change"])
                changed[which_result].city = Switch.general_data_inputer([header[4],\
                                header[4],original[which_result].city,"Change"])
                changed[which_result].address = Switch.general_data_inputer([header[5],\
                                header[5],original[which_result].address,"Change"])
                changed[which_result].available_beds = Switch.general_data_inputer([header[6],\
                                header[6],original[which_result].available_beds,"Change"])
                changed[which_result].planned_donor_number = Switch.general_data_inputer([header[7],\
                                header[7],original[which_result].planned_donor_number,"Change"])
                changed[which_result].final_donor_number = EventCalculations.maximum_donor_number(\
                    changed[which_result].available_beds,changed[which_result].start_time,changed[which_result].end_time)
                ChangeClass.print_preprocessor_event(original,changed,header,which_result,-1)
            elif select == 2:
                os.system('cls')
                ChangeClass.print_preprocessor_event(original,changed,header,which_result,[0,7])
                if ChangeClass.change_select_arrow == 0:
                    changed[which_result].date_of_event = Switch.general_data_inputer([header[0],\
                                "Date of the event (YYYY.MM.DD)",original[which_result].date_of_event,"Change"])
                elif ChangeClass.change_select_arrow == 1:
                    changed[which_result].start_time = Switch.general_data_inputer([header[1],"Start time (hh:mm)",\
                                original[which_result].start_time,"Change"])
                elif ChangeClass.change_select_arrow == 2:
                    changed[which_result].end_time = Switch.general_data_inputer([header[2],"End time (hh:mm)",\
                                changed[which_result].start_time,original[which_result].end_time,"Change"])
                elif ChangeClass.change_select_arrow == 3:
                    changed[which_result].zip_code = Switch.general_data_inputer([header[3],\
                                header[3],original[which_result].zip_code,"Change"])
                elif ChangeClass.change_select_arrow == 4:
                    changed[which_result].city = Switch.general_data_inputer([header[4],\
                                header[4],original[which_result].city,"Change"])
                elif ChangeClass.change_select_arrow == 5:
                    changed[which_result].address = Switch.general_data_inputer([header[5],\
                                header[5],original[which_result].address,"Change"])
                elif ChangeClass.change_select_arrow == 6:
                    changed[which_result].available_beds = Switch.general_data_inputer([header[6],\
                                header[6],original[which_result].available_beds,"Change"])
                elif ChangeClass.change_select_arrow == 7:
                    changed[which_result].planned_donor_number = Switch.general_data_inputer([header[7],\
                                header[7],original[which_result].planned_donor_number,"Change"])
                changed[which_result].final_donor_number = EventCalculations.maximum_donor_number(\
                    changed[which_result].available_beds,changed[which_result].start_time,changed[which_result].end_time)
                ChangeClass.print_preprocessor_event(original,changed,header,which_result,-1)
            elif select == 3:
                print("Save")
            elif select == 4:
                break
            menu_number = ChangeClass.is_there_any_changes(original, changed, header, which_result, "Event")



    @staticmethod
    def change_process_donor(original, changed):
        header = ["Donor's name","Weight","Gender","Birth date","Last donation date","Sickness","Unique ID",
                  "Expiration of ID","Blood type","Hemoglobin","Email","Mobile number","Donor is suitable"]
        which_result = 0
        result_number = len(original)
        if result_number > 1:
            print("There are " + str(result_number) + " results:")
        else:
            print("The result:")
        print("-" * 52)
        for i in range(result_number):
            ChangeClass.print_preprocessor_donor(original,0,header,i,-1)

        if result_number > 1:
            print("Which result would you like to change?")
            which_result = int(input("Please give the result serial number (or 0 if none):"))
            if which_result == 0:
                return False
            else:
                os.system('cls')
                print("-" * 52)
                which_result -= 1
                ChangeClass.print_preprocessor_donor(original,0,header,which_result,-1)

        menu_number = 3
        while True:
            print("What would you like to change about this donor's data?\n")
            select = ChangeOptionsMenu.change_options(2, "  ", menu_number)
            print()

            if select == 1:
                changed[which_result].name = Switch.general_data_inputer([header[0],"Enter your full name",\
                                original[which_result].name,"Change"])
                changed[which_result].weight = Switch.general_data_inputer([header[1],header[1],\
                                original[which_result].weight,"Change"])
                changed[which_result].gender = Switch.general_data_inputer([header[2],header[2],\
                                original[which_result].gender,"Change"])
                changed[which_result].birth_date = Switch.general_data_inputer([header[3],"Birth date (YYYY.MM.DD)",\
                                original[which_result].birth_date,"Change"])
                changed[which_result].last_donation = Switch.general_data_inputer([header[4],\
                                "Last donation date (type 'never' if never before)",original[which_result].last_donation,\
                                "Change"])
                changed[which_result].sick = Switch.general_data_inputer([header[5],"Were you sick in the last month?",\
                                original[which_result].sick,"Change"])
                changed[which_result].uniqeid = Switch.general_data_inputer([header[6],"Unique identifier number",\
                                original[which_result].uniqeid,"Change"])
                changed[which_result].expuniqeid = Switch.general_data_inputer([header[7],"Expiration date of your ID",\
                                original[which_result].expuniqeid,"Change"])
                changed[which_result].blood_type = Switch.general_data_inputer([header[8],\
                                "Blood type (A, B, AB, 0 with +/-)",original[which_result].blood_type,"Change"])
                changed[which_result].hemoglobin = Switch.general_data_inputer([header[9],"Hemoglobin level",\
                                original[which_result].hemoglobin,"Change"])
                changed[which_result].email = Switch.general_data_inputer([header[10],"E-mail address",\
                                original[which_result].email,"Change"])
                changed[which_result].phone_number = Switch.general_data_inputer([header[11],header[11],\
                                original[which_result].phone_number,"Change"])
                changed[which_result].suitable = Validations.donor_suitable([changed[which_result].birth_date,\
                                changed[which_result].weight,changed[which_result].last_donation,\
                                changed[which_result].sick,changed[which_result].hemoglobin])
                ChangeClass.print_preprocessor_donor(original,changed,header,which_result,-1)

            elif select == 2:
                os.system('cls')
                ChangeClass.print_preprocessor_donor(original,changed,header,which_result,[0,11])
                if ChangeClass.change_select_arrow == 0:
                    changed[which_result].name = Switch.general_data_inputer([header[0],"Enter your full name",\
                                original[which_result].name,"Change"])
                elif ChangeClass.change_select_arrow == 1:
                    changed[which_result].weight = Switch.general_data_inputer([header[1],header[1],\
                                original[which_result].weight,"Change"])
                elif ChangeClass.change_select_arrow == 2:
                    changed[which_result].gender = Switch.general_data_inputer([header[2],header[2],\
                                original[which_result].gender,"Change"])
                elif ChangeClass.change_select_arrow == 3:
                    changed[which_result].birth_date = Switch.general_data_inputer([header[3],"Birth date (YYYY.MM.DD)",\
                                original[which_result].birth_date,"Change"])
                elif ChangeClass.change_select_arrow == 4:
                    changed[which_result].last_donation = Switch.general_data_inputer([header[4],\
                                "Last donation date (type 'never' if never before)",original[which_result].last_donation,\
                                "Change"])
                elif ChangeClass.change_select_arrow == 5:
                    changed[which_result].sick = Switch.general_data_inputer([header[5],"Were you sick in the last month?",\
                                original[which_result].sick,"Change"])
                elif ChangeClass.change_select_arrow == 6:
                    changed[which_result].uniqeid = Switch.general_data_inputer([header[6],"Unique identifier number",\
                                original[which_result].uniqeid,"Change"])
                elif ChangeClass.change_select_arrow == 7:
                    changed[which_result].expuniqeid = Switch.general_data_inputer([header[7],"Expiration date of your ID",\
                                original[which_result].expuniqeid,"Change"])
                elif ChangeClass.change_select_arrow == 8:
                    changed[which_result].blood_type = Switch.general_data_inputer([header[8],\
                                "Blood type (A, B, AB, 0 with +/-)",original[which_result].blood_type,"Change"])
                elif ChangeClass.change_select_arrow == 9:
                    changed[which_result].hemoglobin = Switch.general_data_inputer([header[9],"Hemoglobin level",\
                                original[which_result].hemoglobin,"Change"])
                elif ChangeClass.change_select_arrow == 10:
                    changed[which_result].email = Switch.general_data_inputer([header[10],"E-mail address",\
                                original[which_result].email,"Change"])
                elif ChangeClass.change_select_arrow == 11:
                    changed[which_result].phone_number = Switch.general_data_inputer([header[11],header[11],\
                                original[which_result].phone_number,"Change"])
                changed[which_result].suitable = Validations.donor_suitable([changed[which_result].birth_date,\
                                changed[which_result].weight,changed[which_result].last_donation,\
                                changed[which_result].sick,changed[which_result].hemoglobin])
                ChangeClass.print_preprocessor_donor(original,changed,header,which_result,-1)
                print(changed[which_result].suitable[1])
            elif select == 3:
                print("Save")
            elif select == 4:
                break
            menu_number = ChangeClass.is_there_any_changes(original, changed, header, which_result, "Donor")

    @staticmethod
    def is_there_any_changes(original,changed,header,i,arrow):
        if arrow == "Event":
            orig_val, change_val = ChangeClass.print_preprocessor_event(original,changed,header,i,"Is there any changes")
        elif arrow == "Donor":
            orig_val, change_val = ChangeClass.print_preprocessor_donor(original,changed,header,i,"Is there any changes")
        for one_orig, one_change in zip(orig_val, change_val):
            if type(one_change) == list:
                if one_change[0] == "Passport" or one_change[0] == "Identity card":
                    one_change = one_change[1]
                else:
                    one_change = one_change[0]
            if str(one_orig) != str(one_change):
                return 4
        return 3

    @staticmethod
    def print_preprocessor_event(original,changed,header,i,arrow):
        change_val = 0
        orig_val = [original[i].date_of_event,original[i].start_time,original[i].end_time,original[i].zip_code,\
                           original[i].city,original[i].address,original[i].available_beds,\
                           original[i].planned_donor_number,original[i].final_donor_number]
        if changed != 0:
            change_val = [changed[i].date_of_event,changed[i].start_time,changed[i].end_time,changed[i].zip_code,\
                           changed[i].city,changed[i].address,changed[i].available_beds,\
                           changed[i].planned_donor_number,changed[i].final_donor_number]
        if arrow == "Is there any changes":
            return orig_val, change_val
        else:
            ChangeClass.printer(orig_val,change_val,header,i,arrow)

    @staticmethod
    def print_preprocessor_donor(original,changed,header,i,arrow):
        change_val = 0
        orig_val = [original[i].name,original[i].weight,original[i].gender,original[i].birth_date,\
                           original[i].last_donation,original[i].sick,original[i].uniqeid,original[i].expuniqeid,\
                           original[i].blood_type,original[i].hemoglobin,original[i].email,original[i].phone_number,\
                           original[i].suitable]
        if changed != 0:
            change_val = [changed[i].name,changed[i].weight,changed[i].gender,changed[i].birth_date,\
                           changed[i].last_donation,changed[i].sick,changed[i].uniqeid,changed[i].expuniqeid,\
                           changed[i].blood_type,changed[i].hemoglobin,changed[i].email,changed[i].phone_number,\
                           changed[i].suitable]
        if arrow == "Is there any changes":
            return orig_val, change_val
        else:
            ChangeClass.printer(orig_val,change_val,header,i,arrow)

    @staticmethod
    def printer(orig_val, change_val, header, i, arrow):
        if change_val == 0:
            for j in range(len(orig_val)):
                if j == 0:
                    print(str(i+1) + "." + ((21-len(header[j])-len(str(i))) * " ") + header[j] + ": " + orig_val[j])
                else:
                    print((22-len(header[j])) * " " + header[j] + ": " + orig_val[j])
            print("-" * 52)
        else:
            print(8 * " " + "Data field" + 8 * " " + "Original" + 17 * " " + "Changed")
            print("-" * 64)
            for j in range(len(orig_val)):
                if type(change_val[j]) == list:
                    if change_val[j][0] == "Passport" or change_val[j][0] == "Identity card":
                        change_val[j] = change_val[j][1]
                    else:
                        change_val[j] = change_val[j][0]
                if type(arrow) is list and arrow[0] == j:
                    third_colomn = (22 - len(str(orig_val[j]))) * " "
                    print((22-len(header[j])) * " " + header[j] + ": " + str(orig_val[j]) + third_colomn + "--> "\
                          + str(change_val[j]))
                else:
                    third_colomn = (26 - len(str(orig_val[j]))) * " "
                    print((22-len(header[j])) * " " + header[j] + ": " + str(orig_val[j]) + third_colomn + str(change_val[j]))
            print("-" * 64)
            if type(arrow) is list:
                ChangeClass.select_enter_menu(orig_val,change_val,header,i,arrow)

    @staticmethod
    def select_enter_menu(orig_val,change_val,header,i,arrow):
        key = ord(getch())  #billentyuleutes

        if key != 13:
            if key == 72:
                arrow[0] -= 1
            elif key == 80:
                arrow[0] += 1
            if arrow[0] < 0:
                arrow[0] = arrow[1]
            elif arrow[0] > arrow[1]:
                arrow[0] = 0
            os.system('cls')
            ChangeClass.printer(orig_val,change_val,header,i,arrow)
        elif key == 13:
            ChangeClass.change_select_arrow = arrow[0]


ChangeClass.search_in_ids(id)
