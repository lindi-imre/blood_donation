__author__ = 'Péter'

from random import randint

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
            return False

    @staticmethod
    def check_arusicklastmonth(sick):
        sick_words = ["y","yes"]
        if sick.lower() in sick_words:
            print("Not suitable because you are sick at last month.")
            return exit()
        return True

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

        if not is_valid:
            print("Mobil number is not valid!")

    @staticmethod
    def rnd_hmg_generate(hmg_lvl):
        hmg_lvl = random.randint(80, 200)
        return hmg_lvl

    @staticmethod
    def validate_hmg():
        if not rnd_hmg_generate(hmg_lvl) > 110:
            print("Our hemogoblin level " + rnd_hemogoblin_generate(hmg_lvl) + " not suitable!")
            return False
        return True

    @staticmethod
    def validate_email(email):
        is_valid = (email.find("@") == 1) and (email.endswith(".hu") or email.endswith(".com"))
        if not is_valid:
            print("Email address is not valid!")
            return False
        return True





