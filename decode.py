import sys
from msvcrt import getch


class Accents:
    @staticmethod
    def letter_decode(letter):
        if letter == 139:
            return "ő"
        elif letter == 138:
            return "Ő"
        elif letter == 163:
            return "ú"
        elif letter == 233:
            return "Ú"
        elif letter == 130:
            return "é"
        elif letter == 144:
            return "É"
        elif letter == 160:
            return "á"
        elif letter == 181:
            return "Á"
        elif letter == 251:
            return "ű"
        elif letter == 235:
            return "Ű"
        elif letter == 148:
            return "ö"
        elif letter == 153:
            return "Ö"
        elif letter == 129:
            return "ü"
        elif letter == 154:
            return "Ü"
        elif letter == 162:
            return "ó"
        elif letter == 224:
            return "Ó"
        elif letter == 161:
            return "í"
        elif letter == 214:
            return "Í"
        else:
            return chr(letter)


