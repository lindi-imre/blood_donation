__author__ = 'Kozma Balazs'
from msvcrt import getch
from file_operator import FileOperator
import mysql.connector
import csv


class ListingDataBase(object):
    @staticmethod
    def listing_database(which_file):
        if FileOperator.csv_or_db() == 'db':
            ListingDataBase.listing_database_db(which_file)
        else:
            ListingDataBase.listing_database_csv(which_file)

    @staticmethod
    def listing_database_db(which_file):
        server_name, user_name, user_password, database_name = FileOperator.app_config_reader()
        if 'donors' in which_file:
            table_name = '.Donor'
        else:
            table_name = '.Event'
        sql_command, result, header = [], [], []
        sql_command.append("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE " + \
                     "`TABLE_SCHEMA`='" + database_name + "' AND `TABLE_NAME`='" + table_name[1:] + "';")
        sql_command.append("SELECT * FROM " + database_name + table_name)
        dbcon = mysql.connector.connect(user=user_name, password=user_password, host=server_name, database=database_name)
        cursor = dbcon.cursor()
        for i, one_command in enumerate(sql_command):
            cursor.execute(one_command)
            for cursor_message in cursor:
                if i == 0:
                    header.append(cursor_message[0])
                else:
                    result.append(cursor_message)
        if len(result) != 0:
            if len(result) == 1:
                print("There is only one result:")
            elif len(result) > 1:
                print("There are " + str(len(result)) + " results:")
            print("-" * 52)
            for i in range(len(result)):
                ListingDataBase.printer(i + 1, header, result[i])
        else:
            print("There is no data corresponding to this query...")
        dbcon.close()
        getch()

    @staticmethod
    def listing_database_csv(which_file):
        print("-" * 52)
        is_there_any_data = False
        with open(which_file, "r", encoding="utf-8") as csvfile:
            filereader = csv.reader(csvfile, delimiter=",", quotechar='"')
            is_first_row = True
            for i, row in enumerate(filereader):
                if is_first_row:
                    first_row = row
                    for i, header in enumerate(first_row):
                        header = header.replace("_", " ")
                        first_row[i] = header[0].upper() + header[1:]
                    is_first_row = False
                    continue
                is_there_any_data = True
                ListingDataBase.printer(i, first_row, row)
        if not is_there_any_data:
            print("Sorry, the database is empty...")

    @staticmethod
    def printer(i, first_row, row):
        is_first_element = True
        for (head, one_element) in zip(first_row, row):
            one_element = str(one_element)
            if is_first_element:
                print(str(i) + "." + " " * (24 - len(str(i)) - len(head)) + head + ": " + one_element)
                is_first_element = False
            else:
                print(" " * (25 - len(head)) + head + ": " + one_element)
        print("-" * 52)
        if i % 2 == 0 and i != 0:
            getch()