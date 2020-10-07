# 1. Валідація має бути написана на всі поля, наприклад, не може вік людини бути -10 чи 165.
# При введенні у числове поле літери, необхідно показувати помилку.
# Ім`я чи прізвище не може містити цифри чи спеціальних символів, тощо.
# Валідація повинна бути універсальною, тобто окремий метод на перевірку числа, окремий, на те, чи входить в окремі межі
# Валідація - це допоміжні методи, які мають знаходитись в окремому файлі (клас).
import re
import datetime as dt


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
                return False

    @staticmethod
    def menu_choice_and_sort_and_changer_validation(data):
        if represents_int(data):
            if 8 > int(data) > 0:
                return True
            else:
                print("wrong option entered. Reenter:")

    @staticmethod
    def validate_email(data):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, data):
            return True
        else:
            return False

    @staticmethod
    def validate_amount_or_id(data):
        if represents_int(data):
            if int(data) > 0:
                return True
            else:
                return False

    @staticmethod
    def payment_validation(data):
        if data == "paid" or data == "not paid" or data == "refunded":
            return True
        else:
            return False

    @staticmethod
    def validate_date(data):
        try:
            dt.datetime(int(data.strftime("%Y")), int(data.strftime("%m")), int(data.strftime("%d")))
            return True
        except ValueError:
            return False

# file ready
