__author__ = 'Imre'

import datetime

class donor_dates:
    @staticmethod
    def get_date():
        return datetime.datetime.strptime(input(" (year.month.day): "), "%Y.%m.%d.").date()

    @staticmethod
    def get_time():
        return datetime.datetime.strptime(input(" (hour.minutes.): "), "%H.%M.").time()
