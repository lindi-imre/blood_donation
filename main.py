__author__ = 'Slezak Attila'
import os
import time
import getpass

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