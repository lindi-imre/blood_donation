__author__ = 'Péter'

from random import randint
from check_date_format import CheckDateFormat
from datetime import datetime, timedelta
from name_correct_form import NameFormat
from file_operator import FileOperator
import mysql.connector as sql
import csv


class Validations(object):
    @staticmethod
    def check_name(name):
        splitted = name.split(" ")
        if len(splitted) < 2:
            print("Please enter your full name!")
            return False
        for one_name in splitted:
            if not one_name.isalpha():
                print("Please enter valid name!")
                return False
        return True

    @staticmethod
    def check_weight(weight):
        if not weight.isdigit():
             print("Weight should be numbers only!")
             return False
        else:
            if not int(weight) >= 50:
                return [weight, "weight is too low"]
            return [weight]

    @staticmethod
    def validate_gender(gender):
        gender = gender.lower()
        enable_genders = ["male", "m", "female", "f"]
        if not gender in enable_genders:
            print("Enter your gender like an example: 'm', 'male', 'f', 'female'")
            return False
        elif len(gender) == 1:
            gender = enable_genders[enable_genders.index(gender)-1]
        return NameFormat.name_corr_format(gender)


    @staticmethod
    def check_uniqeid_exist(uniqeid):
        uniqeid = uniqeid.upper()
        if FileOperator.csv_or_db() == "db":
            server_name, user_name, user_password, database_name = FileOperator.app_config_reader()
            db = sql.connect(host=server_name,user=user_name,password=user_password,charset='utf8',use_unicode=True, autocommit=True)
            cursor = db.cursor()
            query_in_users_exist = "SELECT unique_identifier FROM BloodDonationStorage.Donor WHERE unique_identifier = '"+uniqeid+"';"
            cursor.execute(query_in_users_exist)
            allusers = cursor.fetchall()
            if allusers:
                print("Already in the database.")
                return False
            else:
                return True
        else:
            file = open("Data/donors.csv", "r", encoding="utf-8")
            reader = csv.reader(file)
            for line in reader:
                if len(line) != 0 and uniqeid == line[6].upper():
                    print("Already in the database.")
                    file.close()
                    return False
            file.close()
            return True
    @staticmethod
    def validate_uniqeid(uniqeid):
        if uniqeid[:6].isdigit() and uniqeid[6:8].isalpha() and len(uniqeid) == 8:
            return ["Identity card", uniqeid.upper()]
        elif uniqeid[:6].isalpha() and uniqeid[6:8].isdigit() and len(uniqeid) == 8:
            return ["Passport", uniqeid.upper()]
        else:
            print("ID should contain 6 digits and 2 letters, the passport should contain 6 letters and 2 numbers.")
            return False

    @staticmethod
    def exp_uniqueid(uniqeid):
        if uniqeid >= datetime.now().date():
            return [uniqeid]
        else:
            return [uniqeid,"expired uniqeid"]

    @staticmethod
    def last_donation_more_than_three_month_ago(last_donation_date):
        today = datetime.now().date()

        # This if statement only runs in unit test case:
        if type(last_donation_date) is list:
            today = last_donation_date[1]
            last_donation_date = last_donation_date[0]

        if today.month > 3:
            modifier = -3
        else:
            modifier = 9
        if str(today.month + modifier) in "4,6,9,11" and today.day > 30:
            today = today.replace(day=30)
        elif today.month + modifier == 2 and today.year % 4 == 0 and today.day > 29:
            today = today.replace(day=29)
        elif today.month + modifier == 2 and today.year % 4 != 0 and today.day > 28:
            today = today.replace(day=28)
        if modifier == 9:
            today = today.replace(year=today.year - 1)
        date_three_month_ago = today.replace(month=today.month + modifier)

        if last_donation_date <= date_three_month_ago:
            return [last_donation_date]
        else:
            return [last_donation_date,"last blood donation in 3 months"]

    @staticmethod
    def check_arusicklastmonth(sick):
        sick_words = ["y", "yes"]
        healthy_words = ["n", "no"]
        if sick.lower() in sick_words:
            return ["Yes","sick in last month"]
        elif sick.lower() in healthy_words:
            return ["No"]
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

        provider_is_valid = phone_number[provider_index:provider_index + 2] in providers
        ending_is_digit = phone_number[provider_index + 2:].isdigit()

        is_valid = start_is_valid and \
                   provider_is_valid and \
                   len(phone_number) in [11, 12] \
                   and ending_is_digit

        if is_valid:
            return True
        else:
            print("Mobile number is not valid!")
            return False

    @staticmethod
    def rnd_hmg_generate():
        hmg_lvl = randint(80, 201)
        return hmg_lvl

    @staticmethod
    def validate_hmg():
        hmg_lvl = Validations.rnd_hmg_generate()
        if hmg_lvl <= 110:
            return [hmg_lvl,"hemoglobin level is too low"]
        else:
            return [hmg_lvl]

    @staticmethod
    def validate_hmg_from_keypad(hmg):
        if hmg.isdigit():
            if 80 <= int(hmg) <= 200:
                if int(hmg) <= 110:
                    return [hmg,"hemoglobin level is too low"]
                else:
                    return [hmg]
            else:
                print("Please enter a valid hemoglobin level between 80 and 200!")
                return False
        else:
            print("Hemoglobin level can contain only number!")
            return False

    @staticmethod
    def validate_email(email):
        is_valid = (email.count("@") == 1) and email[0].isalpha() and \
                   ((email.endswith(".hu") and len(email) > 5) or (email.endswith(".com") and len(email) > 6))
        if not is_valid:
            print("Email address not valid!")
            return False
        return True

    @staticmethod
    def validate_birthdate(birth_date):
        today = datetime.now().date()
        hundred_years_old = today.replace(year=today.year - 100)
        if birth_date > hundred_years_old:
            if today.month == 2 and today.day == 29:
                today = today.replace(day=today.day - 1)
            eighteen_years_ago = today.replace(year=today.year - 18)
            if birth_date <= eighteen_years_ago:
                return [birth_date]
            else:
                return [birth_date, "under 18 years old"]
        else:
            return [birth_date, "more than 100 years old"]

    @staticmethod
    def count_age_of_donor(birth_date):
        today = datetime.now().date()
        year_diff = today.year - birth_date.year
        if today.month < birth_date.month:
            year_diff -= 1
        elif today.month == birth_date.month and today.day < birth_date.day:
            year_diff -= 1
        return year_diff

    @staticmethod
    def blood_type_validation(blood_type):
        types = ("A+", "A-", "B+", "B-",  "AB+", "AB-", "0+", "0-")
        if blood_type.upper() in types:
            return blood_type.upper()
        else:
            print("Invalid blood type, please choose one of the following: A+, A-, B+, B-, AB+, AB-, 0+, 0-")
            return False

    @staticmethod
    def donor_suitable(is_suitable):
        notsuitableprefix = ""
        for one_data in is_suitable:
            if len(one_data) > 1:
                if notsuitableprefix == "":
                    notsuitableprefix = "The donor is not suitable because: " + one_data[1]
                else:
                    notsuitableprefix += " & " + one_data[1]
        if notsuitableprefix != "":
            return ["No", notsuitableprefix]
        else:
            return ["Yes", "The donor is suitable."]