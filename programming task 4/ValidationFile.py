# 1. Валідація має бути написана на всі поля, наприклад, не може вік людини бути -10 чи 165.
# При введенні у числове поле літери, необхідно показувати помилку.
# Ім`я чи прізвище не може містити цифри чи спеціальних символів, тощо.
# Валідація повинна бути універсальною, тобто окремий метод на перевірку числа, окремий, на те, чи входить в окремі межі
# Валідація - це допоміжні методи, які мають знаходитись в окремому файлі (клас).
import re
import datetime
import os


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Validators:
    @staticmethod
    def validate_discount(data):
        if represents_int(data):
            if 100 > int(data) > -1:
                return True
            else:
                print("########Wrong discount data########")
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
            print("File doesn't exist")
            return False

    @staticmethod
    def menu_choice_and_sort_and_changer_validation(data):
        if represents_int(data):
            if 8 > int(data) > 0:
                return True
            else:
                print("wrong option entered. Reenter:")

    @staticmethod
    def validate_filename(file_name):
        regex = '[a-z0-9](.txt)$'
        if re.search(regex, file_name):
            return True
        else:
            print("########Error in filename########")
            return False

    @staticmethod
    def validate_email(data):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, data):
            return True
        else:
            print("########Error in email address########")
            return False

    @staticmethod
    def validate_amount(data):
        if represents_int(data):
            if int(data) > 0:
                return True
            else:
                print("########Error in amount########")
                return False

    @staticmethod
    def validate_id(data):
        if represents_int(data):
            if int(data) > 0:
                return True
            else:
                print("########Error in id########")
                return False

    @staticmethod
    def payment_validation(data):
        if data == "paid" or data == "not paid" or data == "refunded":
            return True
        else:
            print("########Error in payment info########")
            return False

    @staticmethod
    def validate_date(data):
        try:
            datetime.datetime.strptime(data, '%Y-%m-%d')
            return True
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

# file ready
