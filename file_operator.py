__author__ = 'Slezak Attila'
import mysql.connector
import os
import csv
import time
from save_menu_old import SaveMenuOldFashioned

class FileOperator(object):
    @staticmethod
    def delete_from_database(which_file, where, value):
        if FileOperator.csv_or_db() == 'db':
            FileOperator.delete_from_sql_database(which_file, where, value)
        else:
            FileOperator.delete_from_csv_database(which_file, where, value)

    @staticmethod
    def delete_from_sql_database(which_file, where, value):
        server_name, user_name, user_password, database_name = FileOperator.app_config_reader()
        if where == 'id':
            table_name = '.Event'
        else:
            table_name = '.Donor'
        sql_command = []
        sql_command.append("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE " + \
                     "`TABLE_SCHEMA`='" + database_name + "' AND `TABLE_NAME`='" + table_name[1:] + "';")
        sql_command.append("SELECT * FROM " + database_name + table_name + " WHERE " + where + " = '" + value + "';")
        dbcon = mysql.connector.connect(user=user_name, password=user_password, host=server_name, database=database_name)
        cursor = dbcon.cursor()
        result = []
        header = []
        print(sql_command)
        for i, one_command in enumerate(sql_command):
            cursor.execute(one_command)
            for cursor_message in cursor:
                if i == 0:
                    header.append(cursor_message[0])
                else:
                    result.append(cursor_message)
        if len(result) != 0:
            if len(result) == 1:
                print("The result:")
            elif len(result) > 1:
                print("There are " + str(len(result)) + " results:")
            print("-" * 52)
            for i in range(len(result)):
                is_first_element = True
                for (head, one_element) in zip(header, result[i]):
                    one_element = str(one_element)
                    if is_first_element:
                        print(str(i+1) + "." + " " * (24 - len(str(i+1)) - len(head)) + head + ": " + one_element)
                        is_first_element = False
                    else:
                        print(" " * (25 - len(head)) + head + ": " + one_element)
                print("-" * 52)
            select = SaveMenuOldFashioned.save_menu(2, "Do you really want to delete?")
            if select:
                sql_command = "DELETE FROM " + database_name + table_name + " WHERE " + where + " = '" + value + "';"
                cursor.execute(sql_command)
                print("\nDeletion has been successfully finished.")
        else:
            print("There is no data corresponding to this query...")
            print("The deletion was unsuccessful.")
        dbcon.close()
        time.sleep(2)

    @staticmethod
    def delete_from_csv_database(which_file, where, value):
        num_of_deletion = False
        result_lines = []
        with open(which_file, "r", encoding="utf-8") as csvfile:
            filereader = csv.reader(csvfile, delimiter=",", quotechar='"')

            is_first_row = True
            for i, row in enumerate(filereader):
                if is_first_row:
                    first_row = row
                    is_first_row = False
                    continue
                for (header, one_element) in zip(first_row, row):
                    if header == where and one_element.upper() == value.upper():
                        result_lines.append(i)
                        num_of_deletion += 1

        if num_of_deletion != 0:
            with open(which_file, "r", encoding="utf-8") as csvfile:
                filereader = csv.reader(csvfile, delimiter=",", quotechar='"')

                if num_of_deletion == 1:
                    print("There is " + str(num_of_deletion) + " result:")
                elif num_of_deletion > 1:
                    print("There are " + str(num_of_deletion) + " results:")
                print("-" * 52)
                is_first_row = True
                find_num = 1
                for i, row in enumerate(filereader):
                    if is_first_row:
                        first_row = row
                        is_first_row = False
                        continue
                    elif i in result_lines:

                        is_first_element = True
                        for (header, one_element) in zip(first_row, row):
                            if is_first_element:
                                print(str(find_num) + "." + " " * (24 - len(str(find_num)) - len(header)) + header + ": " + one_element)
                                is_first_element = False
                            else:
                                print(" " * (25 - len(header)) + header + ": " + one_element)
                        print("-" * 52)
                        find_num += 1

            select = SaveMenuOldFashioned.save_menu(2, "Do you really want to delete?")
            if select:
                with open(which_file, "r", encoding="utf-8") as csvfile:
                    filereader = csv.reader(csvfile, delimiter=",", quotechar='"')
                    file = open("Data/temporary.csv", "w", encoding='utf-8')
                    for i, row in enumerate(filereader):
                        if i not in result_lines:
                            is_first_element = True
                            for one_element in row:
                                if is_first_element:
                                    file.write(one_element)
                                    is_first_element = False
                                else:
                                    file.write("," + one_element)
                            file.write("\n")
                    file.close()
                os.remove(which_file)
                os.rename("Data/temporary.csv", which_file)
                print("\nDeletion has been successfully finished.")
                time.sleep(2)
        else:
            print("There is no data corresponding to this query...")
            print("The deletion was unsuccessful.")
            time.sleep(2)

    @staticmethod
    def save_new_data(every_file_data, header, path):
        if FileOperator.csv_or_db() == 'db':
            FileOperator.save_new_data_db(every_file_data, header, path)
        else:
            FileOperator.save_new_data_csv(every_file_data, header, path)

    @staticmethod
    def save_new_data_csv(every_file_data, header, path):
        header_exists = True
        next_id = 1
        file = open(path, "r", encoding='utf-8')
        one_line = file.readline()
        if 'donations' in path:
            id_s = []
            for line in file:
                first_colon = line.find(",")
                id_s.append(line[0:first_colon])
            while str(next_id) in id_s:
                next_id += 1
        file.seek(0)
        whole_file = file.read()
        file.close()
        if one_line != header:
            header_exists = False
        if not header_exists:
            file = open(path, "w", encoding='utf-8')
            file.write(header)
            file.write(whole_file)
            file.close()
        file = open(path, "a", encoding='utf-8', newline="")
        first = True
        for one_data in every_file_data:
            if first and 'donations' in path:
                file.write(str(next_id) + "," + str(one_data))
                first = False
            elif first:
                file.write(str(one_data))
                first = False
            else:
                file.write("," + str(one_data))
        file.write("\n")
        file.close()

    @staticmethod
    def save_new_data_db(every_file_data, header, path):
        table_name = ""
        if 'donations' in path:
            table_name = ".Event"
            header = header[3:]
        else:
            table_name = ".Donor"
        FileOperator.create_database()
        server_name, user_name, user_password, database_name = FileOperator.app_config_reader()

        sql_command = "INSERT INTO " + database_name + table_name + " ("+ header + ") VALUES ("
        first = True
        for one_data in every_file_data:
            if first:
                sql_command += "'" + str(one_data) + "'"
                first = False
            elif one_data == 'Never' and 'donors' in path:
                sql_command += ", " + "NULL"
            else:
                sql_command += ", '" + str(one_data) + "'"
        sql_command += ");"
        dbcon = mysql.connector.connect(user=user_name, password=user_password, host=server_name, database=database_name)
        cursor = dbcon.cursor()
        cursor.execute(sql_command)
        dbcon.close()

    @staticmethod
    def save_changes(file_path, file_line_number, changed_obj):

        if file_path == "Data/donations.csv":
            change_val = [changed_obj.id, str(changed_obj.date_of_event), str(changed_obj.start_time),
                          str(changed_obj.end_time), changed_obj.zip_code, changed_obj.city, changed_obj.address,
                          changed_obj.available_beds, changed_obj.planned_donor_number, changed_obj.final_donor_number]
            for j in range(len(change_val)):
                if j == 1 and FileOperator.csv_or_db() == 'csv':
                    change_val[j] = str(change_val[j]).replace("-", ".")
                elif j in [2, 3] and len(str(change_val[j])) > 5:
                    change_val[j] = str(change_val[j])[:len(str(change_val[j]))-3]

        elif file_path == "Data/donors.csv":
            change_val = [changed_obj.name,changed_obj.weight,changed_obj.gender,changed_obj.birth_date,
                          changed_obj.last_donation,changed_obj.sick,changed_obj.uniqeid,
                          changed_obj.expuniqeid, changed_obj.blood_type,changed_obj.hemoglobin,
                          changed_obj.email,changed_obj.phone_number, changed_obj.suitable]
            for j in range(len(change_val)):
                if type(change_val[j]) == list:
                    if change_val[j][0] == "Passport" or change_val[j][0] == "Identity card":
                        change_val[j] = change_val[j][1]
                    else:
                        change_val[j] = change_val[j][0]
                if j in [3, 4, 7] and FileOperator.csv_or_db() == 'csv':
                    change_val[j] = str(change_val[j]).replace("-", ".")
        if FileOperator.csv_or_db() == 'db':
            FileOperator.save_changes_db(file_path, file_line_number, change_val)
        else:
            FileOperator.save_changes_csv(file_path, file_line_number, change_val)

    @staticmethod
    def save_changes_db(file_path, id_and_header, change_val):
        server_name, user_name, user_password, database_name = FileOperator.app_config_reader()
        if 'donors' in file_path:
            table_name, id_name = '.Donor', 'unique_identifier'
        else:
            table_name, id_name = '.Event', 'id'
        sql_command = "UPDATE " + database_name + table_name + " SET "
        for one_header, one_value in zip(id_and_header[1], change_val):
            if one_value != 'Never':
                sql_command += one_header + " = '" + str(one_value) + "', "
            else:
                sql_command += one_header + " = NULL, "
        sql_command = sql_command[0:len(sql_command)-2] + " WHERE " + id_name + " = '" + id_and_header[0] + "';"
        dbcon = mysql.connector.connect(user=user_name, password=user_password, host=server_name, database=database_name)
        cursor = dbcon.cursor()
        cursor.execute(sql_command)
        dbcon.close()

    @staticmethod
    def save_changes_csv(file_path, file_line_number, change_val):
        file = open(file_path, "r", encoding='utf-8')
        reader = csv.reader(file)
        lines_in_file = []
        for i, line in enumerate(reader):
            if i == file_line_number:
                lines_in_file.append(change_val)
            else:
                lines_in_file.append(line)
        file.close()

        file = open(file_path, "w", encoding='utf-8', newline="")
        for i, line in enumerate(lines_in_file):
            first = True
            for one_data in line:
                if first:
                    file.write(str(one_data))
                    first = False
                else:
                    file.write("," + str(one_data))
            file.write("\n")
        file.close()

    @staticmethod
    def csv_or_db():
        file = open('app.config', 'r', encoding='utf-8')
        get_file = file.read()
        file.close()
        for i in range(3):
            where_is_data = get_file.find('"')
            get_file = get_file[where_is_data + 1:]
        if get_file[:2] == 'db':
            return 'db'
        else:
            return 'csv'

    @staticmethod
    def app_config_reader():
        app_config_data_types = ['Server=', 'Uid=', 'Pwd=', 'Database=']
        app_config_values = []
        file = open('app.config', 'r', encoding='utf-8')
        app_file = file.read()
        file.close()
        for what in app_config_data_types:
            where_is_data = app_file.find(what)
            data_value = app_file[where_is_data + len(what):]
            where_is_data = data_value.find(';')
            app_config_values.append(data_value[:where_is_data])
        return app_config_values

    @staticmethod
    def create_database():
        create_files = ['create_db.sql', 'create_donor.sql', 'create_event.sql', 'create_relations.sql']
        sql_commands = []
        server_name, user_name, user_password, database_name = FileOperator.app_config_reader()

        for one_file in create_files:
            file = open('Data/' + one_file, 'r', encoding='utf-8')
            sql_commands.append(file.read())
            file.close()
        dbcon = mysql.connector.connect(user=user_name, password=user_password, host=server_name)
        cursor = dbcon.cursor()
        for one_command in sql_commands:
            if database_name != 'BloodDonationStorage':
                while one_command.find('BloodDonationStorage') != -1:
                    where_is_database_name = one_command.find('BloodDonationStorage')
                    one_command = one_command[:where_is_database_name] + database_name + \
                                one_command[where_is_database_name+20:]
            cursor.execute(one_command)
        dbcon.close()
