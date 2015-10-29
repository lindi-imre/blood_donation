__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from datetime import datetime, timedelta

class EventCalculations(object):
    @staticmethod
    def end_time_after_start_time(input_data, get_data):
        if input_data > get_data[1]:
            return True
        else:
            print("End time must be at least 60 minutes later than start time!")
            return False
