__author__ = 'Imre'

import datetime

class donor_dates:
    @staticmethod
    def get_date():
        return datetime.datetime.strptime(input(" (year.month.day): "), "%Y.%m.%d.").date()

    @staticmethod
    def get_last_donation_date():
        return datetime.datetime.strptime(input(" (year.month.day): "), "%Y.%m.%d.").date()
