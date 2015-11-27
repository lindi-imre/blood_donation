__author__ = 'Kozma Balazs'
from msvcrt import getch

import csv


class ListingDataBase(object):
    @staticmethod
    def listing_database(which_file):
        print("-" * 52)
        is_there_any_data = False
        with open(which_file, "r", encoding="utf-8") as csvfile:
            filereader = csv.reader(csvfile, delimiter=",", quotechar='"')
            is_first_row = True
            for i, row in enumerate(filereader):
                if is_first_row:
                    first_row = row
                    for i, header in enumerate(first_row):
                        header = header.replace("_", " ")
                        first_row[i] = header[0].upper() + header[1:]
                    is_first_row = False
                    continue

                is_there_any_data = True
                is_first_element = True
                for (header, one_element) in zip(first_row, row):
                    if is_first_element:
                        print(str(i) + "." + " " * (24 - len(str(i)) - len(header)) + header + ": " + one_element)
                        is_first_element = False
                    else:
                        print(" " * (25 - len(header)) + header + ": " + one_element)
                print("-" * 52)
                if i % 2 == 0 and i != 0:
                    getch()
            if not is_there_any_data:
                print("Sorry, the database is empty...")
