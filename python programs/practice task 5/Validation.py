import re
import os


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Validators:
    @staticmethod
    def file_deco(func):
        def validate_file(obj, linked_list, pos, file_name):
            all_is_ok = True
            regex = '[a-z0-9](.txt)$'
            if not re.search(regex, file_name):
                print("Invalid filename input")
                all_is_ok = False
            if not os.path.exists(file_name):
                print("Such file does not exist")
                all_is_ok = False
            else:
                if os.stat(file_name).st_size == 0:
                    print("File is empty")
                    all_is_ok = False
            if all_is_ok:
                return func(obj, linked_list, pos, file_name)
            else:
                return False
        return validate_file

    # ---------------------------------------------------------------------------- file validation

    @staticmethod
    def amount_deco(func):
        def validate_amount(obj, linked_list, pos, amount):
            if represents_int(amount):
                if int(amount) < 4:
                    return func(obj, linked_list, pos, amount)
                else:
                    print("To much numbers to generate, can't do this")
            else:
                print("Amount not int")
        return validate_amount

    @staticmethod
    def decorator_context(func):
        def validate_context(obj, linked_list, pos, amount):
            if represents_int(pos):
                if int(pos) < 0 or int(pos) > linked_list.size():
                    print("Wrong position entered")
                    return False
                return func(obj, linked_list, pos, amount)
        return validate_context

    @staticmethod
    def position_deco(func):
        def validate_positions(linked_list, *args):
            all_is_ok = True
            all_are_ints = True
            for pos in args:
                if not represents_int(pos):
                    all_are_ints = False
            if all_are_ints:
                for pos in args:
                    if int(pos) < 1 or int(pos) > linked_list.size():
                        all_is_ok = False
            if all_is_ok:
                return func(linked_list, *args)
            else:
                print("One or more positions is/are out of list range")
        return validate_positions
