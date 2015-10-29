__author__ = 'Kozma Balazs'
# -- coding: UTF-8 --


class Address(object):

    @staticmethod
    def validate_city(city):
        available_cities = ('miskolc', 'szerencs', 'sarospatak', 'kazincbarcika')
        if city.lower() in available_cities:
            return True
        else:
            print("Invalid city name. You can only choose from 'Miskolc', 'Szerencs', 'Sarospatak' or 'Kazincbarcika'")
            return False

    @staticmethod
    def check_zip_code(zip_code):
        if (len(zip_code) == 4) and (zip_code.isdigit()) and (int(zip_code[0]) != 0):
            return True
        else:
            print("Invalid ZIP code. It should contain 4 digits (the first one can't be '0')")
            return False

    @staticmethod
    def validate_address(address):
        if (len(address) <= 25) and (len(address) > 3):
            return True
        else:
            print("Invalid street name. It should contain at least 3, maximum 25 characters.")
            return False
