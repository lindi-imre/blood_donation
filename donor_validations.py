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
        if personal_document[:6].isdigit() and personal_document[6:8].isalpha() and len(personal_document) == 8:
            return ["Identity card", uniqeid]
        elif personal_document[:6].isalpha() and personal_document[6:8].isdigit() and len(personal_document) == 8:
            return ["Passport", uniqeid]
        else:
            return False

