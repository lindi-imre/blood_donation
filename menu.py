# -- coding: utf-8 --
from colorama import Back, Fore, Style, init
import os
from msvcrt import getch
from donor import Person
from event import Event
from search import Search
from listing import ListingDataBase
from delete import DeleteMenu

init()

clear = lambda: os.system('cls')
pos = lambda y, x: '\x1b[%d;%dH' % (y, x)


class Menu:
    @staticmethod
    def search_menu(menu):
        clear()
        print("******** Please choose from the searching options below ********\n*\n* Please select:\n*")
        if menu == 1:
            print("*   " + Back.WHITE + Fore.BLACK + "1. Donors" + Back.RESET + Fore.RESET + "")
            print("*   2. Events")
            print("*   3. Back to menu")
        elif menu == 2:
            print("*   1. Donors")
            print("*   " + Back.WHITE + Fore.BLACK + "2. Events" + Back.RESET + Fore.RESET + "")
            print("*   3. Back to menu")
        elif menu == 3:
            print("*   1. Donors")
            print("*   2. Events")
            print("*   " + Back.WHITE + Fore.BLACK + "3. Back to menu" + Back.RESET + Fore.RESET + "")
        print("*\n****************************************************************")
        Menu.draw_menu("search")
        Menu.enter_menu("search", menu)

    @staticmethod
    def listing_menu(menu):
        clear()
        print("********* Please choose from the listing options below. ********\n*")
        if menu == 1:
            print("*   " + Back.WHITE + Fore.BLACK + "1. List donors" + Back.RESET + Fore.RESET + "")
            print("*   2. List event locations")
            print("*   3. Back to menu")
        elif menu == 2:
            print("*   1. List donors")
            print("*   " + Back.WHITE + Fore.BLACK + "2. List event locations" + Back.RESET + Fore.RESET + "")
            print("*   3. Back to menu")
        elif menu == 3:
            print("*   1. List donors")
            print("*   2. List event locations")
            print("*   " + Back.WHITE + Fore.BLACK + "3. Back to menu" + Back.RESET + Fore.RESET + "")
        print("*\n****************************************************************")
        Menu.draw_menu("listing")
        Menu.enter_menu("listing", menu)

    @staticmethod
    def select_menu(menu):
        clear()
        print("*** Welcome in blood donation and event register application ***\n*\n* Please select:\n*")
        if menu == 1:
            print("*   " + Back.WHITE + Fore.BLACK + "1. Add new donor" + Back.RESET + Fore.RESET + "")
            print("*   2. Add new donation event")
            print("*   3. Delete a donor")
            print("*   4. Delete a donation event")
            print("*   5. List donors or donation events")
            print("*   6. Search")
            print("*   7. Exit")
        elif menu == 2:
            print("*   1. Add new donor")
            print("*   " + Back.WHITE + Fore.BLACK + "2. Add new donation event" + Back.RESET + Fore.RESET + "")
            print("*   3. Delete a donor")
            print("*   4. Delete a donation event")
            print("*   5. List donors or donation events")
            print("*   6. Search")
            print("*   7. Exit")
        elif menu == 3:
            print("*   1. Add new donor")
            print("*   2. Add new donation event")
            print("*   " + Back.WHITE + Fore.BLACK + "3. Delete a donor" + Back.RESET + Fore.RESET + "")
            print("*   4. Delete a donation event")
            print("*   5. List donors or donation events")
            print("*   6. Search")
            print("*   7. Exit")
        elif menu == 4:
            print("*   1. Add new donor")
            print("*   2. Add new donation event")
            print("*   3. Delete a donor")
            print("*   " + Back.WHITE + Fore.BLACK + "4. Delete a donation event" + Back.RESET + Fore.RESET + "")
            print("*   5. List donors or donation events")
            print("*   6. Search")
            print("*   7. Exit")
        elif menu == 5:
            print("*   1. Add new donor")
            print("*   2. Add new donation event")
            print("*   3. Delete a donor")
            print("*   4. Delete a donation event")
            print("*   " + Back.WHITE + Fore.BLACK + "5. List donors or donation events" + Back.RESET + Fore.RESET + "")
            print("*   6. Search")
            print("*   7. Exit")
        elif menu == 6:
            print("*   1. Add new donor")
            print("*   2. Add new donation event")
            print("*   3. Delete a donor")
            print("*   4. Delete a donation event")
            print("*   5. List donors or donation events")
            print("*   " + Back.WHITE + Fore.BLACK + "6. Search" + Back.RESET + Fore.RESET + "")
            print("*   7. Exit")
        elif menu == 7:
            print("*   1. Add new donor")
            print("*   2. Add new donation event")
            print("*   3. Delete a donor")
            print("*   4. Delete a donation event")
            print("*   5. List donors or donation events")
            print("*   6. Search")
            print("*   " + Back.WHITE + Fore.BLACK + "7. Exit" + Back.RESET + Fore.RESET + "")
        print("*\n****************************************************************")
        Menu.draw_menu("main")
        Menu.enter_menu("main", menu)

    @staticmethod
    def draw_menu(menu_type):
        if menu_type == "main":
            i = 2
            while i < 13:
                print('%s%s%s%s' % (pos(i, 64), Fore.WHITE, Back.BLACK, Style.NORMAL), end='*')
                i += 1
            print('%s%s%s%s' % (pos(14, 1), Fore.WHITE, Back.BLACK, Style.NORMAL), end='')
        elif menu_type == "search":
            i = 2
            while i < 10:
                print('%s%s%s%s' % (pos(i, 64), Fore.WHITE, Back.BLACK, Style.NORMAL), end='*')
                i += 1
            print('%s%s%s%s' % (pos(10, 1), Fore.WHITE, Back.BLACK, Style.NORMAL), end='')
        elif menu_type == "listing":
            i = 2
            while i < 7:
                print('%s%s%s%s' % (pos(i, 64), Fore.WHITE, Back.BLACK, Style.NORMAL), end='*')
                i += 1
            print('%s%s%s%s' % (pos(12, 1), Fore.WHITE, Back.BLACK, Style.NORMAL), end='')


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
                elif menu == 1:
                    Person.donor_register_app()
                elif menu == 2:
                    Event.event_data()
                elif menu == 3:
                    DeleteMenu.delete_menu("Data/donors.csv")
                elif menu == 4:
                    DeleteMenu.delete_menu("Data/donations.csv")
                elif menu == 5:
                    Menu.listing_menu(1)
                elif menu == 6:
                    Menu.search_menu(1)
            Menu.select_menu(menu)

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
                Menu.search_menu(menu)
            elif key == 13:
                if menu == 1:
                    Search.search_in_file("Data/donors.csv")
                    waiting = input()
                elif menu == 2:
                    Search.search_in_file("Data/donations.csv")
                    waiting = input()
                elif menu == 3:
                    Menu.select_menu(1)
                Menu.search_menu(menu)

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
                Menu.listing_menu(menu)
            elif key == 13:
                if menu == 3:
                    Menu.select_menu(1)
                if menu == 1:
                    ListingDataBase.listing_database("Data/donors.csv")
                    input()
                if menu == 2:
                    ListingDataBase.listing_database("Data/donations.csv")
                    input()
                Menu.listing_menu(menu)

Menu.select_menu(1)
