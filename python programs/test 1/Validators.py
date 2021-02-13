import re
import datetime
import os


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Validation:
    validators_of_employee_fields = {'name': 'validate_name',
                                     'salary': 'validate_salary',
                                     'first_working_date': 'validate_working_date',
                                     'last_working_date': 'validate_working_date'}

    @staticmethod
    def validate_name(data):
        if data.isalpha():
            return True
        else:
            return False

    @staticmethod
    def validate_salary(data):
        if len(data.rsplit('.')[-1]) == 2:
            return True
        else:
            return False

    @staticmethod
    def validate_working_date(data):
        data = data.split("-")
        if (not represents_int(data[0])
                or not represents_int(data[1])
                or not represents_int(data[2])):
            return False
        # print(data)
        year = int(data[2])
        month = int(data[1])
        day = int(data[0])
        if year > 2014:
            # print("Year: " + str(year) + "\t month: " + str(month) + "\tday: " + str(day))
            try:
                datetime.date(year, month, day)
                return True
            except ValueError:
                # print("This is the incorrect date string format. It should be YYYY-MM-DD")
                return False

    @staticmethod
    def file_not_empty(file_name):
        if os.stat(file_name).st_size == 0:
            return False
        else:
            # print("File isn't empty")
            return True

    @staticmethod
    def file_exists(file_name):
        if os.path.exists(file_name):
            return True
        else:
            return False

    @staticmethod
    def validate_filename(file_name):
        regex = '[a-z0-9](.txt)$'
        if re.search(regex, file_name):
            return True
        else:
            return False

    @staticmethod
    def worked_time_validation(first, last):
        # print(last, "-", first)
        first = first.split("-")
        last = last.split("-")
        # print(last[0], last[1], last[2])
        if int(last[2]) - int(first[2]) > 0 or int(last[1]) - int(first[1]) > 3:
                #b (int(last[1]) - int(first[1]) == 3 and int(last[0]) - int(first[0]) > 0):
            return True
        else:
            print("Error in line (worker hasn't worked for 3 of more month)")
            return False
