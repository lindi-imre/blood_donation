__author__ = 'Kozma Balazs'

import csv


class ListingDonors(object):
    @staticmethod
    def open_donors(which_file):
        with open(which_file, "r", encoding="utf-8") as csvfile:
            donours = csv.reader(csvfile, delimiter="|", quotechar='|')
            for row in donours:
                print(row)

    @staticmethod
    def open_donations(which_file):
        with open(which_file, "r", encoding="utf-8") as csvfile:
            donours = csv.reader(csvfile, delimiter="|", quotechar='|')
            for row in donours:
                print(row)
