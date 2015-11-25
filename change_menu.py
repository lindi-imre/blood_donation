# -- coding: utf-8 --
from colorama import Back, Fore, Style, init
import os
from msvcrt import getch
from decode import menu
from change_class import ChangeSearch

init()
clear = lambda: os.system('cls')
pos = lambda y, x: '\x1b[%d;%dH' % (y, x)


class ChangeMenu:
    @staticmethod
    def change_menu():
        clear()

        print("************ Please enter a donor or donation ID ************\n*\n*   ID:\n*")
        print("*************************************************************")
        i = 2
        while i < 5:
                print('%s%s%s%s' % (pos(i, 61), Fore.WHITE, Back.BLACK, Style.NORMAL), end='*')
                i += 1
        print('%s%s%s%s' % (pos(3, 9), Fore.WHITE, Back.BLACK, Style.NORMAL), end='')

        getkey = True
        id = ""
        while getkey:
            button = getch()
            if ord(button) == 13:
                getkey = False
            elif ord(button) == 27:
                menu()
            else:
                id += button

        ChangeSearch.search_in_ids(id)
