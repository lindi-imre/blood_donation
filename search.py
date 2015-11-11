# -- coding: utf-8 --
import csv

class Search(object):
    @staticmethod
    def search_in_file(which_file):
        term = input("Search term: ")
        print("-" * 40)
        found = False
        with open(which_file, "r", encoding="utf-8") as csvfile:
            filereader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in filereader:
                for one_element in row:
                    if one_element.find(term) >= 0:
                        found = True
                if found:
                    for one_element in row:
                        if type(one_element) == list:
                            for one_part in one_element:
                                print(one_part)
                        else:
                            print(one_element)
                    found = False
                    print("-" * 40)
        return True