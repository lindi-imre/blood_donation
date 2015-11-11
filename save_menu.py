from msvcrt import getch
from colorama import Fore, Style, Back, init

init()

pos = lambda y, x: '\x1b[%d;%dH' % (y, x)


class SaveMenu:
    @staticmethod
    def save_menu(select):
        while True:
            print('%s%s%s%s' % (pos(20, 1), Fore.WHITE, Back.BLACK, Style.NORMAL), end='')
            if select == 1:
                print("Do you want to save? " + "yes " + Back.WHITE + Fore.BLACK + "no" + Back.RESET + Fore.RESET + "")
            if select == 2:
                print("Do you want to save? " + Back.WHITE + Fore.BLACK + "yes" + Back.RESET + Fore.RESET + "" + " no")

            button = ord(getch())
            if button == 224:
                select += 1
                if select == 3:
                    select = 1
            elif button == 13:
                if select == 1:
                    return False
                elif select == 2:
                    return True
