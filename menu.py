from colorama import Back, Fore, Style, init
import os
from msvcrt import getch
from donor import Person
from event import Event

init()

clear = lambda: os.system('cls')
pos = lambda y, x: '\x1b[%d;%dH' % (y, x)


class Menu:
    @staticmethod
    def select_menu(menu):
        clear()
        print("*** Welcome in blood donation and event register application ***\n*")
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
        i = 2
        while i < 11:
            print('%s%s%s%s' % (pos(i, 64), Fore.WHITE, Back.BLACK, Style.NORMAL), end='*')
            i += 1
        print('%s%s%s%s' % (pos(12, 1), Fore.WHITE, Back.BLACK, Style.NORMAL), end='')

        #billentyuleutes
        key = ord(getch())

        #menuszam tulcsordulas ellen
        if key == 72:
            menu -= 1
        elif key == 80:
            menu += 1
        if menu == 0:
            menu = 7
        if menu == 8:
            menu = 1

        if key == 13:
            if menu == 7:
                clear()
                #print("Press any key to exit!")
                #getch()
                exit()
            if menu == 6:
                pass
            if menu == 1:
                Person.donor_register_app()
            if menu == 2:
                Event.event_data()

        Menu.select_menu(menu)



Menu.select_menu(1)