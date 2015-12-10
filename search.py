# -- coding: utf-8 --
import csv
import os.path
import getpass
from msvcrt import getch
import mysql.connector
from file_operator import FileOperator

user_name = getpass.getuser()
if os.path.isfile("C:/Users/" + user_name + "/AppData/Local/Programs/Python/Python35-32/Lib/site-packages/colorama-0.3.3-py3.5.egg"):
    from colorama import Fore, Style


class Search(object):
    @staticmethod
    def search_in_file(which_file):
        search_term = input("Search term: ")
        print("-" * 52)
        if FileOperator.csv_or_db() == 'db':
            Search.search_in_file_db(which_file, search_term)
        else:
            Search.search_in_file_csv(which_file, search_term)

    @staticmethod
    def search_in_file_db(which_file, search_term):
        num_of_find = 1
        server_name, user_name, user_password, database_name = FileOperator.app_config_reader()
        sql_search_term = " LIKE '%" + search_term + "%' OR "
        if 'donors' in which_file:
            table_name = '.Donor'
        else:
            table_name = '.Event'
        sql_command, result, header = [], [], []
        sql_command.append("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE " + \
                     "`TABLE_SCHEMA`='" + database_name + "' AND `TABLE_NAME`='" + table_name[1:] + "';")
        sql_command.append("SELECT * FROM " + database_name + table_name + " WHERE ")
        dbcon = mysql.connector.connect(user=user_name, password=user_password, host=server_name, database=database_name)
        cursor = dbcon.cursor()
        cursor.execute(sql_command[0])
        for cursor_message in cursor:
            header.append(cursor_message[0])
            for one_message in cursor_message:
                sql_command[1] += one_message + sql_search_term
        sql_command[1] = sql_command[1][0:len(sql_command[1]) - 4]
        cursor.execute(sql_command[1])
        for cursor_message in cursor:
            if Search.search_and_print(search_term, header, cursor_message, num_of_find):
                num_of_find += 1
        if num_of_find == 1:
            print("There is no data corresponding to this query...")
        dbcon.close()

    @staticmethod
    def search_in_file_csv(which_file, search_term):
        num_of_find = 1
        first = True
        with open(which_file, "r", encoding="utf-8") as csvfile:
            filereader = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in filereader:
                if first:
                    first_row = row
                    for i, header in enumerate(first_row):
                        header = header.replace("_", " ")
                        first_row[i] = header[0].upper() + header[1:]
                    first = False
                    continue
                if Search.search_and_print(search_term, first_row, row, num_of_find):
                    num_of_find += 1
            if num_of_find == 1:
                print("There is no data corresponding to this query...")

    @staticmethod
    def search_and_print(search_term, first_row, row, i):
        finder = 0
        found = {}
        for (header, one_element) in zip(first_row, row):
            one_element = str(one_element)
            one_element = one_element.lower()
            search_term = search_term.lower()
            while one_element.find(search_term, finder) >= 0:
                if finder == 0:
                    found[header] = str(one_element.find(search_term))
                else:
                    found[header] = found.get(header) + "," + str(one_element.find(search_term, finder))
                finder += one_element.find(search_term, finder) - finder + 1
            finder = 0
        if found:
            is_first_element = True
            for (header, one_element) in zip(first_row, row):
                one_element = str(one_element)
                if found.get(header) is not None and os.path.isfile("C:/Users/" + user_name + "/AppData/Local/Programs/Python/Python35-32/Lib/site-packages/colorama-0.3.3-py3.5.egg"):
                    results = found[header].split(",")
                    print_digit = 0
                    if is_first_element:
                        print(str(i) + "." + " " * (24-len(header)-len(str(i))) + header + ": ", end="")
                    else:
                        print(" " * (25-len(header)) + header + ": ", end="")
                    for next_result in results:
                        one_result = int(next_result)
                        print(one_element[print_digit:one_result] + Fore.RED + \
                              one_element[one_result:one_result+len(search_term)] + Style.RESET_ALL, end="")
                        print_digit = one_result + len(search_term)
                    print(one_element[print_digit:])
                else:
                    if is_first_element:
                        print(str(i) + "." + " " * (24-len(header)-len(str(i))) + header + ": " + one_element)
                    else:
                        print(" " * (25-len(header)) + header + ": " + one_element)
                is_first_element = False
            found = {}
            print("-" * 52)
            if i % 2 == 0:
                getch()
            return True
