__author__ = 'Slezak Attila'
import os
import csv
import time
from save_menu_old import SaveMenuOldFashioned

class FileOperator(object):
    @staticmethod
    def delete_from_database(which_file, where, value):
        num_of_deletion = False
        result_lines = []
        with open(which_file, "r", encoding="utf-8") as csvfile:
            filereader = csv.reader(csvfile, delimiter=",", quotechar='"')

            is_first_row = True
            for i, row in enumerate(filereader):
                if is_first_row:
                    first_row = row
                    is_first_row = False
                    continue
                for (header, one_element) in zip(first_row, row):
                    if header == where and one_element.upper() == value.upper():
                        result_lines.append(i)
                        num_of_deletion += 1

        if num_of_deletion != 0:
            with open(which_file, "r", encoding="utf-8") as csvfile:
                filereader = csv.reader(csvfile, delimiter=",", quotechar='"')

                if num_of_deletion == 1:
                    print("There is " + str(num_of_deletion) + " result:")
                elif num_of_deletion > 1:
                    print("There are " + str(num_of_deletion) + " results:")
                print("-" * 52)
                is_first_row = True
                find_num = 1
                for i, row in enumerate(filereader):
                    if is_first_row:
                        first_row = row
                        is_first_row = False
                        continue
                    elif i in result_lines:

                        is_first_element = True
                        for (header, one_element) in zip(first_row, row):
                            if is_first_element:
                                print(str(find_num) + "." + " " * (24 - len(str(find_num)) - len(header)) + header + ": " + one_element)
                                is_first_element = False
                            else:
                                print(" " * (25 - len(header)) + header + ": " + one_element)
                        print("-" * 52)
                        find_num += 1

            select = SaveMenuOldFashioned.save_menu(2, "Do you really want to delete?")
            if select:
                with open(which_file, "r", encoding="utf-8") as csvfile:
                    filereader = csv.reader(csvfile, delimiter=",", quotechar='"')
                    file = open("Data/temporary.csv", "w", encoding='utf-8')
                    for i, row in enumerate(filereader):
                        if i not in result_lines:
                            is_first_element = True
                            for one_element in row:
                                if is_first_element:
                                    file.write(one_element)
                                    is_first_element = False
                                else:
                                    file.write("," + one_element)
                            file.write("\n")
                    file.close()
                os.remove(which_file)
                os.rename("Data/temporary.csv", which_file)
                print("\nDeletion has been successfully finished.")
                time.sleep(2)
        else:
            print("There is no data corresponding to this query...")
            print("The deletion was unsuccessful.")
            time.sleep(2)


    @staticmethod
    def save_changes(file_path, file_line_number, changed_obj):

        if file_path == "Data/donations.csv":
            change_val = [changed_obj.id, str(changed_obj.date_of_event), str(changed_obj.start_time),
                          str(changed_obj.end_time), changed_obj.zip_code, changed_obj.city, changed_obj.address,
                          changed_obj.available_beds, changed_obj.planned_donor_number, changed_obj.final_donor_number]
            for j in range(len(change_val)):
                if j == 1:
                    change_val[j] = str(change_val[j]).replace("-", ".")
                elif j in [2, 3] and len(str(change_val[j])) > 5:
                    change_val[j] = str(change_val[j])[:len(str(change_val[j]))-3]

        elif file_path == "Data/donors.csv":
            change_val = [changed_obj.name,changed_obj.weight,changed_obj.gender,changed_obj.birth_date,
                          changed_obj.last_donation,changed_obj.sick,changed_obj.uniqeid,
                          changed_obj.expuniqeid, changed_obj.blood_type,changed_obj.hemoglobin,
                          changed_obj.email,changed_obj.phone_number, changed_obj.suitable]
            for j in range(len(change_val)):
                if type(change_val[j]) == list:
                    if change_val[j][0] == "Passport" or change_val[j][0] == "Identity card":
                        change_val[j] = change_val[j][1]
                    else:
                        change_val[j] = change_val[j][0]
                if j in [3, 4, 7]:
                    change_val[j] = str(change_val[j]).replace("-", ".")

        file = open(file_path, "r", encoding='utf-8')
        reader = csv.reader(file)
        lines_in_file = []
        for i, line in enumerate(reader):
            if i == file_line_number:
                lines_in_file.append(change_val)
            else:
                lines_in_file.append(line)
        file.close()

        file = open(file_path, "w", encoding='utf-8', newline="")
        for i, line in enumerate(lines_in_file):
            first = True
            for one_data in line:
                if first:
                    file.write(str(one_data))
                    first = False
                else:
                    file.write("," + str(one_data))
            file.write("\n")
        file.close()
