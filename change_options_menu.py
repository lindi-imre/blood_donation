__author__ = 'Slezak Attila'

from msvcrt import getch


class ChangeOptionsMenu(object):
    @staticmethod
    def change_options(select, question, menu_number):
        while True:
            if menu_number == 3:
                if select == 1:
                    print("\r" + question + " --> Change all" + "      Change select" + "      Cancel", end='')
                elif select == 2:
                    print("\r" + question + "     Change all" + "  --> Change select" + "      Cancel", end='')
                elif select == 3:
                    print("\r" + question + "     Change all" + "      Change select" + "  --> Cancel", end='')

            if menu_number == 4:
                if select == 1:
                    print("\r" + question + " --> Change all" + "      Change select" + "      Confirm changes" + "      Cancel", end='')
                elif select == 2:
                    print("\r" + question + "     Change all" + "  --> Change select" + "      Confirm changes" + "      Cancel", end='')
                elif select == 3:
                    print("\r" + question + "     Change all" + "      Change select" + "  --> Confirm changes" + "      Cancel", end='')
                elif select == 4:
                    print("\r" + question + "     Change all" + "      Change select" + "      Confirm changes" + "  --> Cancel", end='')


            button = ord(getch())
            # print(button)
            if button == 72  or button == 75:
                select -= 1
            elif button == 80  or button == 77:
                select += 1
            if select > menu_number:
                select = 1
            elif select < 1:
                select = menu_number
            if button == 13:
                if select == 1:
                    return 1
                elif select == 2:
                    return 2
                elif select == menu_number:
                    return 4
                elif select == 3:
                    return 3