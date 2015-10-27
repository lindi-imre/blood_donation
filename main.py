__author__ = 'Imre'


def check_zip_code(zip_code):
    if (len(zip_code) == 4) and (zip_code.isdigit()) and (int(zip_code[0]) != 0):
        return True


def get_zip_code():
    zip_code_string = ""
    while not check_zip_code(zip_code_string):
        zip_code_string = input("Enter a valid zip code: ")

    return int(zip_code_string)


def validate_zip_code(zip_code):
    if check_zip_code(zip_code):
        return True