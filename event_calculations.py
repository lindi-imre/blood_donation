__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from datetime import datetime, timedelta, time

class EventCalculations(object):
    @staticmethod
    def end_time_after_start_time(input_data, get_data):
        input_data = datetime.strptime(str(input_data), "%H:%M:%S")
        get_data = datetime.strptime(str(get_data), "%H:%M:%S")
        if input_data > get_data + timedelta(seconds=3599):
            return True
        else:
            print("End time must be at least 60 minutes later than start time!")
            return False
