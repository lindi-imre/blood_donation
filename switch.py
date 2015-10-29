__author__ = 'Slezak Attila'
# -- coding: utf-8 --



def general_data_inputer(get_data):
    while input_data == "":
        input_data = input(get_data[0] + ": ")
        if input_data == "":
            empty_field_error_message(get_data[0])
        elif input_data != "":
            result = switcher(input_data, get_data)
            if type(result) != bool:
                input_data = result
            elif not result:
                input_data = ""
    return input_data

def switcher(input_data, get_data):
    if get_data[0] == "Date of the event":
        return check_date_format(input_data):
    elif get_data[0] == "City":
        return address(input_data)
    elif get_data[0] == "Zip code":
        return (check_zip_code(input_data) and validate_zip_code(input_data))
    # elif get_data[0] == "Start time":
    #     return check_time(input_data)
    # elif get_data[0] == "End time":
    #     return (check_time(input_data))
    # elif get_data[0] == "Available beds":
    #     return check_available_beds(input_data)
    # elif get_data[0] == "Address":
    #     return validate_address(input_data)
    # elif get_data[0] == "Planned donor number":
    #     return check_planned_donor_number(input_data)

def empty_field_error_message(empty_field):
    print(empty_field, "cannot be empty!")