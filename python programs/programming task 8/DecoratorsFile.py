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

    validators_of_order_fields = {'id': 'validate_id',
                                  'order_status': 'payment_validation',
                                  'amount': 'validate_amount',
                                  'discount': 'validate_discount',
                                  'order_date': 'validate_date',
                                  'shipped_date': 'validate_date',
                                  'customer_email': 'validate_email'}

    @staticmethod
    def discount_decorator(discount_setter):
        def validate_discount(order_self, data):
            if represents_int(data):
                if 99 < int(data) or int(data) < 0:
                    print("Entered wrong data! Discount must be 0-100")
                    return False
                else:
                    return discount_setter(order_self, data)
            else:
                return False
        return validate_discount

    @staticmethod
    def validate_discount(data):
        if represents_int(data):
            if 99 < int(data) or int(data) < 0:
                # print( + data)
                return False
            else:
                # print("Validated")
                return True
        else:
            print("Error in line (discount not int). Wrong data: " + data)
            return False

    # ----------------------------------------------------------------------------

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
        regex = '[a-z0-9](.json)$'
        if re.search(regex, file_name):
            return True
        else:
            return False

    @staticmethod
    def read_from_file_decorator(func):
        def file_validation(collection, filename):
            if Validators.validate_filename(filename):
                if Validators.file_exists(filename):
                    if Validators.file_not_empty(filename):
                        return func(collection, filename)
                    else:
                        print("File empty")
                        return False
                else:
                    print("File does not exist")
                    return False
            else:
                print("Wrong filename")
                return False
        return file_validation

    @staticmethod
    def file_validation(filename):
        if Validators.validate_filename(filename):
            if Validators.file_exists(filename):
                if Validators.file_not_empty(filename):
                    return True
                else:
                    print("File empty")
                    return False
            else:
                print("File does not exist")
                return False
        else:
            print("Wrong filename")
            return False

    # ----------------------------------------------------------------------------
    @staticmethod
    def sort_and_changer_validation(data):
        if represents_int(data):
            if 8 > int(data) > 0:
                return True
            else:
                print("wrong option entered. Reenter:")

    @staticmethod
    def menu_choice_validation(data):
        if represents_int(data):
            if 10 > int(data) > 0:
                return True
            else:
                print("wrong option entered. Reenter:")

    # ----------------------------------------------------------------------------

    @staticmethod
    def validate_email(data):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, data):
            return True
        else:
            # print("Error in line (wrong email in line). Wrong data: " + data)
            return False

    @staticmethod
    def email_decorator(email_setter):
        def validate_email(order_self, data):
            data = data.lower()
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if re.search(regex, data):
                # print("email ok")
                return email_setter(order_self, data)
            else:
                return False
        return validate_email

    # ----------------------------------------------------------------------------

    @staticmethod
    def validate_amount(data):
        if represents_int(data):
            if int(data) > 0:
                return True
            else:
                # print("Error in line (wrong amount in line). Wrong data: " + data)
                return False
        else:
            # print("Error in line (amount not int). Wrong data: " + data)
            return False

    @staticmethod
    def amount_decorator(amount_setter):
        def validate_amount(order_self, data):
            if represents_int(data):
                if int(data) > 0:
                    return amount_setter(order_self, data)
                else:
                    return False
        return validate_amount
    # ----------------------------------------------------------------------------

    @staticmethod
    def validate_id(data):
        if represents_int(data):
            if int(data) > 0:
                return True
            else:
                # print("Error in line (wrong id in line). Wrong data: " + data)
                return False
        else:
            print("Error in line (id not int). Wrong data: " + data)
            return False

    @staticmethod
    def id_decorator(id_setter):
        def validate_id(order_self, data):
            if represents_int(data):
                if int(data) > 0:
                    return id_setter(order_self, data)
                else:
                    return False
        return validate_id
    # ----------------------------------------------------------------------------

    @staticmethod
    def payment_validation(data):
        if data == "paid" or data == "not paid" or data == "refunded":
            return True
        else:
            # print("Error in line (wrong payment status in line). Wrong data: " + data)
            return False

    @staticmethod
    def status_decorator(status_setter):
        def payment_validation(order_self, data):
            if data == "paid" or data == "not paid" or data == "refunded":
                return status_setter(order_self, data)
            else:
                return False
        return payment_validation
    # ----------------------------------------------------------------------------

    @staticmethod
    def validate_date(data):
        data = data.split("-")
        if (not represents_int(data[0])
                or not represents_int(data[1])
                or not represents_int(data[2])):
            # print("not int in data")
            return False
        year = int(data[0])
        month = int(data[1])
        day = int(data[2])
        # print("Year: " + str(year) + "\t month: " + str(month) + "\tday: " + str(day))
        try:
            datetime.date(year, month, day)
            return True
        except ValueError:
            # print("This is the incorrect date string format. It should be YYYY-MM-DD")
            return False

    @staticmethod
    def date_decorator(date_setter):
        def validate_date(order_self, data):
            date = form_str_to_date_format(data)
            if (not represents_int(date[0])
                    or not represents_int(date[1])
                    or not represents_int(date[2])):
                # print("not int in data")
                return False
            year = int(date[0])
            month = int(date[1])
            day = int(date[2])
            # print("Year: " + str(year) + "\t month: " + str(month) + "\tday: " + str(day))
            try:
                datetime.date(year, month, day)
                return date_setter(order_self, data)
            except ValueError:
                # print("This is the incorrect date string format. It should be YYYY-MM-DD")
                return False
        return validate_date
# file ready


def form_str_to_date_format(data):
    to_return = []
    data = data[:-1]
    # print("data=", data)
    data = data[1:]
    # print("data=", data)
    data = data.split(", ")
    # print("data=", data)
    for i in data:
        i = i[:-1]
        i = i[1:]
        to_return.append(i)
    # print("to return")
    # print(to_return)
    return to_return
