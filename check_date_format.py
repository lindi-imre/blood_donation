__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from datetime import datetime

class CheckDateFormat(object):
    @staticmethod
    def check_date_format(get_date):
        date_parts = get_date.split(".")
        print(date_parts)
        if len(date_parts) == 3 and len(date_parts[0]) == 4 and len(date_parts[1]) == 2 and len(date_parts[2]) == 2:
            for part in date_parts:
                if not part.isdigit() or int(date_parts[1]) > 12 or int(date_parts[2]) > 31:
                    print("Bad date format ! It should be YYYY.MM.DD !")
                    return False
            return True
        print("Bad date format ! It should be YYYY.MM.DD !")
        return False