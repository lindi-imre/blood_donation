__author__ = 'Imre'

import datetime

class donor_dates:
    @staticmethod
    def get_date(date_str):
        return datetime.datetime.strptime(date_str, "%Y.%m.%d.").date()

    @staticmethod
<<<<<<< HEAD
    def get_time(time_str):
        return datetime.datetime.strptime(time_str, "%H:%M").time()
=======
    def get_time():
        return datetime.datetime.strptime(input(" (hour.minutes.): "), "%H.%M.").time()
>>>>>>> 93931ceaee78379aaa5f7419f9241e274cd8187d
