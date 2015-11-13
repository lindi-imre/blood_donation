__author__ = 'Slezak Attila'
import os
import time
import getpass
from msvcrt import getch

os.system('cls')

user_name = getpass.getuser()
if not os.path.isfile("C:/Users/" + user_name + "/AppData/Local/Programs/Python/Python35-32/Lib/site-packages/colorama-0.3.3-py3.5.egg"):

    print("You have to install the colorama module first!")
    save = input("Do you want it? ('Yes' or 'No'): ")
    if save.lower() == "yes" or save.lower() == "y":
        os.chdir('colorama-0.3.3')
        os.system("python setup.py install")
        print("\nInstallation has been successfully finished!")
        time.sleep(3)
        os.chdir('..')
        os.system('cls')
        os.system("python menu.py")
    else:
        os.system('cls')
        os.system("python main_old.py")
else:
    os.system('cls')
    os.system("python menu.py")

class Main:
    @staticmethod
    def main(menu):
        user_name = getpass.getuser()
        chosen = ""
        if not os.path.isfile("C:/Users/" + user_name + "/AppData/Local/Programs/Python/Python35-32/Lib/site-packages/colorama-0.3.3-py3.5.egg"):
            while True:
                os.system('cls')
                print("-" * 77)
                print("If You would like to use the colored menu, You should install Colorama first!\nDo you want to install it?\n")
                if menu == 1:
                    print(" --> 1. Yes, I want to install Colorama.")
                    print("     2. No, I do not want to install it.")
                elif menu == 2:
                    print("     1. Yes, I want to install Colorama.")
                    print(" --> 2. No, I do not want to install it.")
                key = ord(getch())
                if key == 224:
                    menu += 1
                elif key == 13:
                    if menu == 1:
                        chosen = "yes"
                    elif menu == 2:
                        chosen = "no"
                if menu == 3:
                    menu = 1

                if chosen == "yes":
                    os.chdir('colorama-0.3.3')
                    os.system("python setup.py install")
                    print("\nInstallation has been successfully finished!")
                    time.sleep(2.4)
                    os.chdir('..')
                    os.system('cls')
                    os.system("python menu.py")
                    break
                elif chosen == "no":
                    os.system('cls')
                    os.system("python menu_old.py")
                    break
        else:
            os.system('cls')
            os.system("python menu.py")

Main.main(1)

