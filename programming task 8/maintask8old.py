from OrderFile import Order
from DecoratorsFile import Validators
from CollectionFile import Collection
from DecoratorsFile import represents_int
from flask import Flask

# Використати патерн Знімок (Memento) для зберігання останніх 5 дій користувача над  колекцією
# екземплярів вказаного класу. Визначити два додаткові методи: undo, redo для повернення до n стану.

choice_to_attr_dict = {'1': 'id',
                       '2': 'order_status',
                       '3': 'amount',
                       '4': 'discount',
                       '5': 'order_date',
                       '6': 'shipped_date',
                       '7': 'customer_email'}
attr_dict = {'id': 'id',
                 'order_status': 'order_status',
                 'amount': 'amount',
                 'discount': 'discount',
                 'order_date': 'order_date',
                 'shipped_date': 'shipped_date',
                 'customer_email': 'customer_email'}


def sort_user_choice():
    read = input("Enter a parameter to be sorted by:\n"
                 "1 - id\n"
                 "2 - order status\n"
                 "3 - amount of product bought\n"
                 "4 - discount\n"
                 "5 - order date\n"
                 "6 - shipped date\n"
                 "7 - customer email\n")
    while not Validators.sort_and_changer_validation(read):
        read = input()
    sort_choice = choice_to_attr_dict[read]
    return sort_choice


def editing_the_collection(collection, file_name):
    read = input("Enter a number of order to be changed (enter 0 not ot change anything):")
    if represents_int(read):
        while collection.get_len() < int(read) or 0 > int(read):
            read = input("Reenter a number of order to be changed(enter 0 not to change anything)")
        if int(read) == 0:
            pass
        else:
            to_change_id = int(read)
            read = input("Enter an info to be changed\n"
                         "1 - id\n"
                         "2 - order status\n"
                         "3 - amount\n"
                         "4 - discount\n"
                         "5 - order date\n"
                         "6 - shipped date\n"
                         "7 - customer email\n")
            while not Validators.sort_and_changer_validation(int(read)) \
                    or not represents_int(read):
                read = input("Reenter an info to be changed")
            to_change_field = choice_to_attr_dict[read]
            read = input("Enter new data:")
            collection.change2(to_change_id, to_change_field, read, file_name)


def main():
    collection = Collection()
    collection.read_from_file("task8data.json")
    res = collection.search("paid")
    # for i in res:
        # print(i)
    data_dict = dict()
    data_dict["id"] = "100"
    data_dict["order_status"] = "not paid"
    data_dict["amount"] = "10"
    data_dict["discount"] = "11"
    data_dict["order_date"] = "['2020', '11', '28']"
    data_dict["shipped_date"] = "['2020', '11', '28']"
    data_dict["customer_email"] = "faes@gmail.com"

    collection.edit_all_fields(6, data_dict)
    collection.print()
    """menu_choice = 0
    collection = Collection()
    read = input("Enter file name (eg. data.json):")
    while not Validators.file_validation(read):
        read = input("Enter file name (eg. data.json):")
    file_name = read
    collection.read_from_file(file_name)
    collection.print()
    # print(collection.get_len())
    while menu_choice != 9:
        print("You are in main menu. Possible options:\n"
              "1 - search some data through all info\n"
              "2 - sort collection by some argument\n"
              "3 - delete any order(by its number in list) and rewrite collection in file\n"
              "4 - add an order and rewrite collection in file\n"
              "5 - edit an order and rewrite collection in file\n"
              "6 - print memento\n"
              "7 - undo\n"
              "8 - redo\n"
              "9 - exit program\n"
              "Choose your option: ")
        read = input()
        while not Validators.menu_choice_validation(read):
            read = input()
        menu_choice = int(read)
        if menu_choice == 1:
            read = input("Enter data to be searched:")
            collection.search(read)
            print()
            print()
        elif menu_choice == 2:
            sort_choice = sort_user_choice()
            collection.sort(sort_choice)
            collection.print()
        elif menu_choice == 3:
            read = input("Enter a number of order to be deleted(enter 0 not to delete anything)")
            if represents_int(read):
                while collection.get_len() < int(read) or 0 > int(read):
                    read = input("Reenter a number of order to be deleted(enter 0 not to delete anything)")
                if int(read) == 0:
                    break
                else:
                    collection.deleter(int(read), file_name)
            collection.print()

        elif menu_choice == 4:
            print("Enter a LINE which is similar to (with a ', ' as a delimiter or enter 0 to skip)\n"
                  "ID, order_status (paid, refunded, not paid), amount, discount (percentage), "
                  "order_date, shipped_date, customer_email")
            read = input()
            if represents_int(read) and int(read) == 0:
                pass
            else:
                to_add = Order
                to_add = Order.str_to_order2(to_add, read)
                collection.add_order(to_add)
                collection.rewriting_to_file(file_name)
            collection.print()

        elif menu_choice == 5:
            editing_the_collection(collection, file_name)
            collection.print()

        elif menu_choice == 6:
            collection.memory.show_memory()

        elif menu_choice == 7:
            collection.undo()
            collection.rewriting_to_file(file_name)

        elif menu_choice == 8:
            collection.redo()
            collection.rewriting_to_file(file_name)

        elif menu_choice == 9:
            print("Have a nice day! Goodbye!")"""


main()
