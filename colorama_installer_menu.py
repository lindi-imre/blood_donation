from msvcrt import getch
import os


class ColoramaMenu:
    @staticmethod
    def install_menu(menu):
        while True:
            os.system('cls')
            print("If You would like to use the colored menu, You should install Colorama.\nDo you want to install it?\n")
            if menu == 1:
                print("* 1. Yes, I want install Colorama")
                print("  2. No, I don't want to install Colorama")
            elif menu == 2:
                print("  1. Yes, I want install Colorama")
                print("* 2. No, I don't want to install Colorama")
            key = ord(getch())
            if key == 224:
                menu += 1
            elif key == 13:
                if menu == 1:
                    return True
                elif menu == 2:
                    return False
            if menu == 3:
                menu = 1

ColoramaMenu.install_menu(2)
