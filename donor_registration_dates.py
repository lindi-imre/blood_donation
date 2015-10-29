__author__ = 'Imre'

import datetime

class donor_dates:
    @staticmethod
    def get_date(date_str):
        return datetime.datetime.strptime(date_str, "%Y.%m.%d.").date()

    @staticmethod
    def get_time(time_str):
        return datetime.datetime.strptime(time_str, "%H:%M").time()
