__author__ = 'Slezak Attila'
# -- coding: utf-8 --

# from donor_validations import Validations
from check_date_format import CheckDateFormat
from donor_registration_dates import donor_dates
from address import Address
from check_if_positive_int import CheckIfPositiveInteger
from name_correct_form import NameFormat
from date_ten_day_before_event import DateTenDayBeforeEvent
from date_is_weekday import DateIsWeekday

class Switch(object):
    @staticmethod
    def general_data_inputer(get_data):
        input_data = ""
        while input_data == "":
            if len(get_data) > 2 and get_data[len(get_data)-1] == "Test":
                input_data = get_data[len(get_data)-2]
            else:
                input_data = input(get_data[0] + ": ")
            if input_data == "":
                Switch.empty_field_error_message(get_data[0])
            elif input_data != "":
                result = Switch.switcher(input_data, get_data)
                if type(result) != bool:
                    input_data = result
                elif not result and get_data[len(get_data)-1] != "Test":
                    input_data = ""
                elif not result and get_data[len(get_data)-1] == "Test":
                    input_data = result
        return input_data

    @staticmethod
    def switcher(input_data, get_data):
        if get_data[0] == "Date of the event":
            if CheckDateFormat.check_date_format(input_data):
                input_data = donor_dates.get_date(input_data)
                if DateIsWeekday.is_date_weekday(input_data) and DateTenDayBeforeEvent.is_date_ten_day_before_event(input_data):
                    return input_data
                else:
                    return False
        elif get_data[0] == "City":
            if Address.validate_city(input_data):
                return NameFormat.name_corr_format(input_data)
            else:
                return False
        elif get_data[0] == "Zip code":
            return Address.check_zip_code(input_data)
        # elif get_data[0] == "Start time":
        #     return check_time(input_data)
        # elif get_data[0] == "End time":
        #     return (check_time(input_data))
        elif get_data[0] == "Available beds" or get_data[0] == "Planned donor number":
            return CheckIfPositiveInteger.check_if_positive_integer(input_data)
        elif get_data[0] == "Address":
            if Address.validate_address(input_data):
                return NameFormat.name_corr_format(input_data)

    @staticmethod
    def empty_field_error_message(empty_field):
        print(empty_field, "field cannot be empty!")