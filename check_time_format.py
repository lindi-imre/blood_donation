__author__ = 'Slezak Attila'
# -- coding: utf-8 --

class CheckTimeFormat(object):
    @staticmethod
    def check_time_form(get_time):
        time_parts = get_time.split(":")
        for part in time_parts:
            if not part.isdigit():
                print("Bad time format! It should be 'hh:mm'!")
                return False
        if len(time_parts) == 2 and len(time_parts[0]) < 3 and len(time_parts[1]) < 3:
            if int(time_parts[0]) < 24 and int(time_parts[1]) < 60:
                return True
            else:
                print("Hours can be maximum 23 and minutes can be maximum 59!")
                return False
        elif len(time_parts) == 3 and len(time_parts[0]) < 3 and len(time_parts[1]) < 3 and len(time_parts[2]) < 3:
            if int(time_parts[0]) < 24 and int(time_parts[1]) < 60 and int(time_parts[2]) < 60:
                return True
            else:
                print("Hours can be maximum 23, minutes and seconds can be maximum 59!")
                return False
        print("Bad time format! It should be 'hh:mm'!")
        return False
