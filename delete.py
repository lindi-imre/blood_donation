__author__ = 'Slezak Attila'
import os
from file_operator import FileOperator

class DeleteMenu(object):
    @staticmethod
    def delete_menu(which_file):
        os.system('cls')
        welcome_message= "Please give the id what you would like to delete in the " + which_file[5:] + " file!"
        print("*" * len(welcome_message))
        print(welcome_message + "\n")
        deleting_data = input(">> ")
        if which_file == "Data/donors.csv":
            FileOperator.delete_from_database(which_file,"unique_identifier", deleting_data)
        elif which_file == "Data/donations.csv":
            FileOperator.delete_from_database(which_file,"id", deleting_data)
