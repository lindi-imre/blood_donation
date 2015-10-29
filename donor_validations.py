__author__ = 'Péter'

class Validations(object):
    @staticmethod
    def parse_name(name):
        splitted = name.split()
        full_name = []
        if not str.isalpha(name):
            print("Only strings is valid!")
            return False
        else:
            if len(splitted) > 0:
                full_name['first_name'] = splitted[0]
            if len(splitted) > 1:
                full_name['last_name'] = splitted[1]
        return True

    @staticmethod
    def check_weight():
        if not weight.isdigit():
             print("Weight should be numbers only!")
             return False
        else:
            if not weight > 50:
                print("You are too skinny!")
                return False
            return True

    @staticmethod
    def check_gender():
        pass