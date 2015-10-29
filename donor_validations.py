__author__ = 'Péter'

from random import randint

class Validations(object):
    @staticmethod
    def check_name(name):
        splitted = name.split( )
        if len(splitted) < 2:
            print("Please enter your full name!")
            return False
        for one_name in splitted:
            if one_name.isalpha():
                return True
            else:
                print("Please enter valid name!")
                return False


    @staticmethod
    def check_weight(weight):
        if not weight.isdigit():
             print("Weight should be numbers only!")
             return False
        else:
            if not int(weight) >= 50:
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

    @staticmethod
    def check_arusicklastmonth(sick):
        sick_words = ["y","yes"]
        healthy_words = ["n", "no"]
        if sick.lower() in sick_words:
            print("Not suitable because you were sick at last month.")
            exit()
        elif sick.lower() in healthy_words:
            return True
        else:
            print("Please give a correct answer like yes or no!")
            return False

    @staticmethod
    def validate_mobil_number(phone_number):
        providers = ["20", "30", "70"]
        start_is_valid = False
        provider_index = 2

        if phone_number.startswith("06"):
            start_is_valid = True
        elif phone_number.startswith("+36"):
            start_is_valid = True
            provider_index = 3

        provider_is_valid = phone_number[provider_index:provider_index+2] in providers
        ending_is_digit = phone_number[provider_index+2:].isdigit()

        is_valid = start_is_valid and \
                   provider_is_valid and \
                   len(phone_number) in [11, 12] \
                   and ending_is_digit

        if is_valid:
            return True
        else:
            print("Mobil number is not valid!")
            return False


    @staticmethod
    def rnd_hmg_generate():
        hmg_lvl = randint(80, 201)
        return hmg_lvl

    @staticmethod
    def validate_hmg():
        hmg_lvl = Validations.rnd_hmg_generate()
        if hmg_lvl <= 110:
            print("Your hemogoblin level is %s which is not suitable!" % hmg_lvl)
            exit()
        else:
            return hmg_lvl

    @staticmethod
    def validate_email(email):
        is_valid = (email.find("@") == 1) and email[0].isalpha() and \
                   ((email.endswith(".hu") and len(email) > 5) or (email.endswith(".com") and len(email) > 6))
        if not is_valid:
            print("Email address is not valid!")
            return False
        return True





