__author__ = 'Imre'

import datetime

class donor_dates:
    @staticmethod
    def get_date(date_str):
        date_str = str(date_str).replace(" ", "").replace("-", ".")
        if date_str[len(date_str)-1] == ".":
            date_str = date_str[0:len(date_str)-1]
        return datetime.datetime.strptime(date_str, "%Y.%m.%d").date()

    @staticmethod
    def get_time(time_str):
        time_str = str(time_str)
        time_parts = time_str.split(":")
        if len(time_parts) == 2:
            return datetime.datetime.strptime(time_str, "%H:%M").time()
        else:
            return datetime.datetime.strptime(time_str, "%H:%M:%S").time()