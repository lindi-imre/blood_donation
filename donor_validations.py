__author__ = 'Péter'

class Validations(object):
    @staticmethod
    def check_name(name):
        splitted = name.split()
        for i in splitted:
            if not splitted[i].isalpha:
                print("Enter valid name!")
                return False
            elif not splitted[i] > 1:
                print("Enter your full name again!")
                return False
            else:
                return True


    @staticmethod
    def check_weight(weight):
        if not weight.isdigit():
             print("Weight should be numbers only!")
             return False
        else:
            if not weight > 50:
                print("You are too skinny!")
                return False
            return True

    @staticmethod
    def validate_gender(gender):
        enable_genders = ["male", "m", "female", "f"]
        if not gender.lower() in enable_genders:
            print("Enter your gender like an example: 'm', 'male', 'f', 'female'")
            return False
        return True

    @staticmethod
    def validate_uniqeid(uniqeid):
        if uniqeid[:6].isdigit() and uniqeid[6:8].isalpha() and len(uniqeid) == 8:
            return ["Identity card", uniqeid]
        elif uniqeid[:6].isalpha() and uniqeid[6:8].isdigit() and len(uniqeid) == 8:
            return ["Passport", uniqeid]
        else:
            print("ID should contain 6 digits and 2 letters, the passport should contain 6 letters and 2 numbers.")
            return False

