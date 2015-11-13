# -- coding: utf-8 --
from donor import Person
from event import Event
from msvcrt import getch
import os
import time

class MainOld:
    @staticmethod
    def select_menu():
        while True:
            os.system('cls')
            print("<~~~~~~~~----------------------^^^^^^^----------------------~~~~~~~>")
            print("Welcome in the blood donor and event location register application!")
            print("Please select what would you like to register:\n1 - Donor registration\n2 - Donor event location registration"
                  "\n3 - Exit")
            menu = input(">> ")
            if menu == "1":
                Person.donor_register_app()
                print("\n")
                break
            elif menu == "2":
                Event.event_data()
                print("\n")
                break
            elif menu == "3":
                exit()
            else:
                print("Please select a valid menu number!")
                time.sleep(1.4)

MainOld.select_menu()