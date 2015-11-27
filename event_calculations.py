__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from datetime import datetime, timedelta, time


class EventCalculations(object):
    @staticmethod
    def end_time_after_start_time(input_data, get_data):
        input_data = EventCalculations.time_to_datetime(input_data)
        get_data = EventCalculations.time_to_datetime(get_data)
        if input_data > get_data + timedelta(seconds=3599):
            return True
        else:
            print("End time must be at least 60 minutes later than start time!")
            return False

    @staticmethod
    def duration_in_time(start_time, end_time):
        start_time = EventCalculations.time_to_datetime(start_time)
        end_time = EventCalculations.time_to_datetime(end_time)
        return end_time - start_time

    @staticmethod
    def maximum_donor_number(available_beds, start_time, end_time):
        start_time = EventCalculations.time_to_datetime(start_time)
        end_time = EventCalculations.time_to_datetime(end_time)
        round = 0
        while start_time <= end_time - timedelta(seconds=3600):
            round += 1
            end_time = end_time - timedelta(seconds=1800)
        return round * int(available_beds)

    @staticmethod
    def time_to_datetime(get_time):
        if type(get_time) is str and len(get_time.split(":")) == 2:
            return datetime.strptime(str(get_time), "%H:%M")
        else:
            return datetime.strptime(str(get_time), "%H:%M:%S")

    @staticmethod
    def success_rate(planned_donor_number, max_donor_number):
        return float(int(max_donor_number) / int(planned_donor_number) * 100)

    @staticmethod
    def success_text(success):
        texts = ["Unsuccessful, not worths to organise there again...", "Normal event.", "Successful!", "Outstanding!"]
        text_index = 0
        if success < 20:
            text_index = 0
        elif 20 <= success < 75:
            text_index = 1
        elif 75 <= success <= 110:
            text_index = 2
        elif success > 110:
            text_index = 3
        return texts[text_index]