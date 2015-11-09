__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from datetime import datetime
import calendar

class CheckDateFormat(object):
    @staticmethod
    def check_date_format(get_date):
        date_parts = get_date.split(".")
        if len(date_parts) == 3:
            if date_parts[1] == 1:
                date_parts[1] = "0" + date_parts[1]
            elif date_parts[2] == 1:
                date_parts[2] = "0"+ date_parts[2]
            if len(date_parts[0]) == 4 and len(date_parts[1]) == 2 and len(date_parts[2]) == 2:
                for part in date_parts:
                    if not part.isdigit():
                        print("Bad date format ! It should be YYYY.MM.DD !")
                        return False
                if int(date_parts[1]) > 12 or int(date_parts[2]) > 31:
                    print("Bad date format! Month of the year is maximum 12 and day of the month is maximum 31!")
                    return False
                elif date_parts[1] in "04,06,09,11" and int(date_parts[2]) > 30:
                    given_month = calendar.month_name[int(date_parts[1])]
                    print(given_month, "is only 30 days long!")
                    return False
                elif date_parts[1] in "02" and int(date_parts[2]) >= 30:
                    print("February is only 29 days long!")
                    return False
                elif date_parts[1] in "02" and int(date_parts[0]) % 4 != 0 and int(date_parts[2]) == 29:
                    print("February is only 28 days long in the given year!")
                    return False
                else:
                    return True
        print("Bad date format ! It should be YYYY.MM.DD !")
        return False
