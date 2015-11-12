# -- coding: utf-8 --
import os
from msvcrt import getch
from donor import Person
from event import Event
from search import Search
from listing import ListingDataBase

clear = lambda: os.system('cls')


class MenuOld:
    @staticmethod
    def search_menu(menu):
        clear()
        print("******** Please choose from the searching options below ********")
        print("*" + 62 * " " + "*" + "\n* Please select:" + 47 * " " + "*" "\n*" + 62 * " " + "*")
        if menu == 1:
            print("*  --> 1. Donors" + " " * 47 + "*")
            print("*      2. Events" + " " * 47 + "*")
            print("*      3. Back to menu" + " " * 41 + "*")
        elif menu == 2:
            print("*      1. Donors" + " " * 47 + "*")
            print("*  --> 2. Events" + " " * 47 + "*")
            print("*      3. Back to menu" + " " * 41 + "*")
        elif menu == 3:
            print("*      1. Donors" + " " * 47 + "*")
            print("*      2. Events" + " " * 47 + "*")
            print("*  --> 3. Back to menu" + " " * 41 + "*")
        print("*" + 62 * " " + "*" + "\n****************************************************************")
        MenuOld.enter_menu("search", menu)

    @staticmethod
    def listing_menu(menu):
        clear()
        print("********* Please choose from the listing options below *********")
        print("*" + 62 * " " + "*" + "\n* Please select:" + 47 * " " + "*" "\n*" + 62 * " " + "*")
        if menu == 1:
            print("*  --> 1. List donors"  + " " * 42 + "*")
            print("*      2. List event locations"  + " " * 33 + "*")
            print("*      3. Back to menu"  + " " * 41 + "*")
        elif menu == 2:
            print("*      1. List donors"  + " " * 42 + "*")
            print("*  --> 2. List event locations"  + " " * 33 + "*")
            print("*      3. Back to menu"  + " " * 41 + "*")
        elif menu == 3:
            print("*      1. List donors"  + " " * 42 + "*")
            print("*      2. List event locations"  + " " * 33 + "*")
            print("*  --> 3. Back to menu"  + " " * 41 + "*")
        print("*" + 62 * " " + "*" + "\n****************************************************************")
        MenuOld.enter_menu("listing", menu)

    @staticmethod
    def select_menu(menu):
        clear()
        print("*** Welcome in blood donation and event register application ***")
        print("*" + 62 * " " + "*" + "\n* Please select:" + 47 * " " + "*" "\n*" + 62 * " " + "*")
        if menu == 1:
            print("*  --> 1. Add new donor" + " " * 40 + "*")
            print("*      2. Add new donation event" + " " * 31 + "*")
            print("*      3. Delete a donor" + " " * 39 + "*")
            print("*      4. Delete a donation event" + " " * 30 + "*")
            print("*      5. List donors or donation events" + " " * 23 + "*")
            print("*      6. Search" + " " * 47 + "*")
            print("*      7. Exit" + " " * 49 + "*")
        elif menu == 2:
            print("*      1. Add new donor" + " " * 40 + "*")
            print("*  --> 2. Add new donation event" + " " * 31 + "*")
            print("*      3. Delete a donor" + " " * 39 + "*")
            print("*      4. Delete a donation event" + " " * 30 + "*")
            print("*      5. List donors or donation events" + " " * 23 + "*")
            print("*      6. Search" + " " * 47 + "*")
            print("*      7. Exit" + " " * 49 + "*")
        elif menu == 3:
            print("*      1. Add new donor" + " " * 40 + "*")
            print("*      2. Add new donation event" + " " * 31 + "*")
            print("*  --> 3. Delete a donor" + " " * 39 + "*")
            print("*      4. Delete a donation event" + " " * 30 + "*")
            print("*      5. List donors or donation events" + " " * 23 + "*")
            print("*      6. Search" + " " * 47 + "*")
            print("*      7. Exit" + " " * 49 + "*")
        elif menu == 4:
            print("*      1. Add new donor" + " " * 40 + "*")
            print("*      2. Add new donation event" + " " * 31 + "*")
            print("*      3. Delete a donor" + " " * 39 + "*")
            print("*  --> 4. Delete a donation event" + " " * 30 + "*")
            print("*      5. List donors or donation events" + " " * 23 + "*")
            print("*      6. Search" + " " * 47 + "*")
            print("*      7. Exit" + " " * 49 + "*")
        elif menu == 5:
            print("*      1. Add new donor" + " " * 40 + "*")
            print("*      2. Add new donation event" + " " * 31 + "*")
            print("*      3. Delete a donor" + " " * 39 + "*")
            print("*      4. Delete a donation event" + " " * 30 + "*")
            print("*  --> 5. List donors or donation events" + " " * 23 + "*")
            print("*      6. Search" + " " * 47 + "*")
            print("*      7. Exit" + " " * 49 + "*")
        elif menu == 6:
            print("*      1. Add new donor" + " " * 40 + "*")
            print("*      2. Add new donation event" + " " * 31 + "*")
            print("*      3. Delete a donor" + " " * 39 + "*")
            print("*      4. Delete a donation event" + " " * 30 + "*")
            print("*      5. List donors or donation events" + " " * 23 + "*")
            print("*  --> 6. Search" + " " * 47 + "*")
            print("*      7. Exit" + " " * 49 + "*")
        elif menu == 7:
            print("*      1. Add new donor" + " " * 40 + "*")
            print("*      2. Add new donation event" + " " * 31 + "*")
            print("*      3. Delete a donor" + " " * 39 + "*")
            print("*      4. Delete a donation event" + " " * 30 + "*")
            print("*      5. List donors or donation events" + " " * 23 + "*")
            print("*      6. Search" + " " * 47 + "*")
            print("*  --> 7. Exit" + " " * 49 + "*")
        print("*" + 62 * " " + "*" + "\n****************************************************************")
        MenuOld.enter_menu("main", menu)

    @staticmethod
    def enter_menu(menu_type, menu):
        key = ord(getch())  #billentyuleutes

        if menu_type == "main":
            if key != 13:
                if key == 72:   #menuszam tulcsordulas ellen
                    menu -= 1
                elif key == 80:
                    menu += 1
                if menu == 0:
                    menu = 7
                if menu == 8:
                    menu = 1
            elif key == 13:
                if menu == 7:
                    #clear()         #print("Press any key to exit!")
                    exit()          #getch()
                if menu == 6:
                    MenuOld.search_menu(1)
                if menu == 1:
                    Person.donor_register_app()
                if menu == 2:
                    Event.event_data()
                if menu == 5:
                    MenuOld.listing_menu(1)
            MenuOld.select_menu(menu)

        elif menu_type == "search":
            if key != 13:
                if key == 72:
                    menu -= 1
                elif key == 80:
                    menu += 1
                if menu == 0:
                    menu = 3
                if menu == 4:
                    menu = 1
                MenuOld.search_menu(menu)
            elif key == 13:
                if menu == 1:
                    Search.search_in_file("Data/donors.csv")
                    waiting = input()
                elif menu == 2:
                    Search.search_in_file("Data/donations.csv")
                    waiting = input()
                elif menu == 3:
                    MenuOld.select_menu(1)
                MenuOld.search_menu(menu)

        elif menu_type == "listing":
            if key != 13:
                if key == 72:
                    menu -= 1
                elif key == 80:
                    menu += 1
                if menu == 0:
                    menu = 3
                if menu == 4:
                    menu = 1
                MenuOld.listing_menu(menu)
            elif key == 13:
                if menu == 3:
                    MenuOld.select_menu(1)
                if menu == 1:
                    ListingDataBase.listing_database("Data/donors.csv")
                    input()
                if menu == 2:
                    ListingDataBase.listing_database("Data/donations.csv")
                    input()
                MenuOld.listing_menu(menu)

MenuOld.select_menu(1)