__author__ = 'Slezak Attila'
# -- coding: utf-8 --
from datetime import datetime

class DateTenDayBeforeEvent(object):
    @staticmethod
    def is_date_ten_day_before_event(get_date):
        date_difference = get_date-datetime.now().date()
        if date_difference.days > 9:
            return True
        else:
            print("Registration must occur before the event at least 10 days!")
            return False