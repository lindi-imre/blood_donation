__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from datetime import datetime

class DateIsWeekday(object):
    @staticmethod
    def is_date_weekday(get_date):
        if get_date.isoweekday() < 6:
            return True
        else:
            print("The event must be on weekdays!")
            return False