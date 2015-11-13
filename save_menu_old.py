from msvcrt import getch


class SaveMenuOldFashioned:
    @staticmethod
    def save_menu(select):
        while True:
            if select == 1:
                print("\rDo you want to save? " + "    yes"+ "  --> no ", end='')
            elif select == 2:
                print("\rDo you want to save? " + "--> yes" + "      no", end='')

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
