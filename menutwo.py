from colorama import Back, Fore, Style, init
import os
from msvcrt import getch
from donor import Person
from event import Event

init()

clear = lambda: os.system('cls')
pos = lambda y, x: '\x1b[%d;%dH' % (y, x)


class MenuTwo:
    @staticmethod
    def select_menu_two(menu):
        clear()
        print("********* Please choose from the listing options below. ********\n*")
        if menu == 1:
            print("*   " + Back.WHITE + Fore.BLACK + "1. List donors" + Back.RESET + Fore.RESET + "")
            print("*   2. List event locations")
            print("*   3. Cancel")
        elif menu == 2:
            print("*   1. List donors")
            print("*   " + Back.WHITE + Fore.BLACK + "2. List event locations" + Back.RESET + Fore.RESET + "")
            print("*   3. Cancel")
        elif menu == 3:
            print("*   1. List donors")
            print("*   2. List event locations")
            print("*   " + Back.WHITE + Fore.BLACK + "3. Cancel" + Back.RESET + Fore.RESET + "")
        print("*\n****************************************************************")
        i = 2
        while i < 7:
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
            menu = 3
        if menu == 8:
            menu = 1

        if key == 13:
            if menu == 3:
                return
            if menu == 1:
                pass
            if menu == 2:
                pass


        MenuTwo.select_menu_two(menu)



MenuTwo.select_menu_two(1)