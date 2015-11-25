__author__ = 'Péter'

import csv
from donor_object import DonorObject
from event_object import DonationObject

class ChangeSearch(object):
   @staticmethod
   def search_in_ids(id):
      #id = input("Search ID: ")
      if id.isdigit():
         file = open("Data/donations.csv", "r", encoding="utf-8")
         reader = csv.reader(file)
         for line in reader:
            if id == line[0]:
               original = DonationObject(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9])
               changed = DonationObject(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9])
               return line
            else:
               return "Not included in the database."
      elif (id[:6].isdigit() and id[6:8].isalpha() and len(id) == 8) or (id[:6].isalpha() and id[6:8].isdigit() and len(id) == 8):
         file = open("Data/donors.csv", "r", encoding="utf-8")
         reader = csv.reader(file)
         for line in reader:
            if id == line[6]:
               original = DonorObject(line[0],line[3],line[1],line[2],line[6],line[7],line[8],line[4],line[5],line[11],line[9],line[12])
               changed = DonationObject(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9])
               return line
            else:
               return "Not included in the database."
      else:
         return ("The input is not correct.")


"""print(ChangeSearch.search_in_ids(id))"""
