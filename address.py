__author__ = 'Kozma Balazs'
# -- coding: UTF-8 --


class Address(object):

    @staticmethod
    def validate_city(city):
        available_cities = ('miskolc', 'szerencs', 'sarospatak', 'kazincbarcika')
        if city.lower() in available_cities:
            return True
        else:
            return False

    @staticmethod
    def check_zip_code(zip_code):
        if (len(zip_code) == 4) and (zip_code.isdigit()) and (int(zip_code[0]) != 0):
            return True
        else:
            return False

    @staticmethod
    def validate_address(address):
        if (len(address) <= 25) and (len(address) > 3):
            return True
        else:
            return False
