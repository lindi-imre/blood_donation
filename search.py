# -- coding: utf-8 --
import csv
import os.path
import getpass
from msvcrt import getch

user_name = getpass.getuser()
if os.path.isfile("C:/Users/" + user_name + "/AppData/Local/Programs/Python/Python35-32/Lib/site-packages/colorama-0.3.3-py3.5.egg"):
    from colorama import Fore, Style


class Search(object):
    @staticmethod
    def search_in_file(which_file):
        num_of_find = 0
        first = True
        finder = 0
        search_term = input("Search term: ")
        print("-" * 52)
        found = {}
        j = 0
        with open(which_file, "r", encoding="utf-8") as csvfile:
            filereader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in filereader:
                if first:
                    first_row = row
                    for i, header in enumerate(first_row):
                        header = header.replace("_", " ")
                        first_row[i] = header[0].upper() + header[1:]
                    first = False
                    continue
                for (header, one_element) in zip(first_row, row):
                    one_element = one_element.lower()
                    search_term = search_term.lower()
                    while one_element.find(search_term, finder) >= 0:
                        if finder == 0:
                            found[header] = str(one_element.find(search_term))
                        else:
                            found[header] = found.get(header) + "," + str(one_element.find(search_term, finder))
                        finder += one_element.find(search_term, finder) - finder + 1
                    finder = 0
                if found:
                    num_of_find += 1
                    is_first_element = True
                    for (header, one_element) in zip(first_row, row):
                        if found.get(header) is not None and os.path.isfile("C:/Users/" + user_name + "/AppData/Local/Programs/Python/Python35-32/Lib/site-packages/colorama-0.3.3-py3.5.egg"):
                            results = found[header].split(",")
                            print_digit = 0
                            if is_first_element:
                                print(str(num_of_find) + "." + " " * (24-len(header)-len(str(num_of_find))) + header + ": ", end="")
                            else:
                                print(" " * (25-len(header)) + header + ": ", end="")
                            for next_result in results:
                                one_result = int(next_result)
                                print(one_element[print_digit:one_result] + Fore.RED + \
                                      one_element[one_result:one_result+len(search_term)] + Style.RESET_ALL, end="")
                                print_digit = one_result + len(search_term)
                            print(one_element[print_digit:])
                        else:
                            if is_first_element:
                                print(str(num_of_find) + "." + " " * (24-len(header)-len(str(num_of_find))) + header + ": " + one_element)
                            else:
                                print(" " * (25-len(header)) + header + ": " + one_element)
                        is_first_element = False
                    found = {}
                    print("-" * 52)
                    j += 1
                    if j % 2 == 0 and j != 0:
                        getch()
        if num_of_find == 0:
            print("There is no data corresponding to this query...")
        return True