# -- coding: utf-8 --
import csv
import itertools
from colorama import Fore, Style

class Search(object):
    @staticmethod
    def search_in_file(which_file):
        first = True
        finder = 0
        search_term = input("Search term: ")
        print("-" * 40)
        found = {}
        with open(which_file, "r", encoding="utf-8") as csvfile:
            filereader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in filereader:
                if first:
                    first_row = row
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
                    for (header, one_element) in zip(first_row, row):
                        if found.get(header) is not None:
                            results = found[header].split(",")
                            print_digit = 0
                            print(header + ": ", end="")
                            for next_result in results:
                                one_result = int(next_result)
                                print(one_element[print_digit:one_result] + Fore.RED + \
                                      one_element[one_result:one_result+len(search_term)] + Style.RESET_ALL, end="")
                                print_digit = one_result + len(search_term)
                            print(one_element[print_digit:])
                        else:
                            print(header + ": " + one_element)
                    print(found)
                    found = {}
                    print("-" * 40)
        return True