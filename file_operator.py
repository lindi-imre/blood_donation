__author__ = 'Slezak Attila'
import os
import csv
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
                    if header == where and one_element == value:
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
                print("Delete is successfully finished.")
        else:
            print("There is no data corresponding to this query...")
            print("The deletion was unsuccessful.")

        input()

    @staticmethod
    def save_changes(file_path, changed_obj):