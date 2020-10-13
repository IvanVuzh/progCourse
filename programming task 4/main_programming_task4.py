from OrderFile import Order
from ValidationFile import Validators
import datetime as dt
from CollectionFile import Collection
from ValidationFile import represents_int

# Клас ЗАМОВЛЕННЯ: ID, order_status (paid, refunded, not paid), amount, discount (percentage),
# order_date, shipped_date, customer_email

# Програма повинна містити меню для перевірки всіх можливостей.
# 2. Пошук повинен працювати по всіх полях автоматично без введення параметра пошуку,
# повинен знаходити всі записи по частковому співпадінні.
# 3. Сортування повинно працювати коректно і бути універсальним методом для всіх полів.
# Значення Test test повинні знаходитись поруч.
# 4. Додати можливість видалення запису (+ запис у файл) по ідентифікатору
# 5. Додати можливість додавання запису (+ запис у файл)
# 6. Додати можливість редагування запису (+ запис у файл) по ідентифікатору
# 7. Код повинен бути якісним: клас повинен бути в окремому файлі, назва файла
# не повинна бути захардкоджена, читання з файла - окрема функція, тощо.
# 8. Всі методи повинні бути універсальні і не залежати від кількості параметрів класу.


def test():
    data_dict = {'id': '3226', 'order_status': 'paid', 'amount': '5', 'discount': '10', 'order_date': '2019-09-22',
                 'shipped_date': '2019-09-22', 'customer_email': 'help@gmail.com'}
    test = Order(data_dict)
    # test2 = Order(data_dict)
    print(test.make_str_for_print())
    # print(test2.make_str())
    # print(Validators.validate_date("2020-10-08"))
    line = "153, paid, 5, 67, 2020-10-08, 2020-10-08, iasdsd@gmail.com"
    test = test.str_to_order(line)
    print(test.make_str_for_print())


def main():
    menu_choice = 0
    collection = Collection()
    read = input("Enter file name (eg. Text.txt):")
    while not Validators.validate_filename(read):
        read = input("Reenter file name (eg. Text.txt):")
    file_name = read
    if Validators.file_not_empty(file_name):
        collection.read_from_file(file_name)
    adding = Order
    # adding.print()
    # obj = dt.datetime(2019, 10, 19)
    # print(obj.strftime("%x"))
    # collection.print()
    while menu_choice != 7:
        print("You are in main menu. Possible options:\n"
              "1 - search some data through all info\n"
              "2 - sort collection by some argument\n"
              "3 - delete any order(by its number in list) and rewrite collection in file\n"
              "4 - add an order and rewrite collection in file\n"
              "5 - edit an order and rewrite collection in file\n"
              "6 - exit program\n"
              "Choose your option: ")
        read = input()
        while not Validators.menu_choice_and_sort_and_changer_validation(read):
            read = input()
        menu_choice = int(read)
        if menu_choice == 1:
            read = input("Enter data to be searched:")
            collection.search(read)
            print()
            print()
        elif menu_choice == 2:
            read = input("Enter a parameter to be sorted by:\n"
                         "1 - id\n"
                         "2 - order status\n"
                         "3 - amount of product bought\n"
                         "4 - discount\n"
                         "5 - order date\n"
                         "6 - shipped date\n"
                         "7 - customer email\n")
            while not Validators.menu_choice_and_sort_and_changer_validation(read):
                read = input()
            if int(read) == 1:
                sort_choice = 'id'
            elif int(read) == 2:
                sort_choice = 'order_status'
            elif int(read) == 3:
                sort_choice = 'amount'
            elif int(read) == 4:
                sort_choice = 'discount'
            elif int(read) == 5:
                sort_choice = 'order_date'
            elif int(read) == 6:
                sort_choice = 'shipped_date'
            elif int(read) == 7:
                sort_choice = 'customer_email'
            collection.sort(sort_choice)
            collection.print()
            print()
            print()
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
            print()
            print()
        elif menu_choice == 4:
            print("Enter a LINE which is similar to (with a ', ' as a delimiter or enter 0 to skip)\n"
                  "ID, order_status (paid, refunded, not paid), amount, discount (percentage), "
                  "order_date, shipped_date, customer_email")
            read = input()
            if represents_int(read) and int(read) == 0:
                pass
            else:
                to_add = Order
                to_add = Order.str_to_order(to_add, read)
                # print(to_add.make_str_for_print())
                collection.add_order(to_add)
                collection.rewriting_to_file(file_name)
            collection.print()
            print()
            print()
        elif menu_choice == 5:
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
                    while not Validators.menu_choice_and_sort_and_changer_validation(int(read)) \
                            or not represents_int(read):
                        read = input("Reenter an info to be changed")

                    to_change_field = int(read)
                    if int(read) == 1:
                        to_change_field = 'id'
                    elif int(read) == 2:
                        to_change_field = 'order_status'
                    elif int(read) == 3:
                        to_change_field = 'amount'
                    elif int(read) == 4:
                        to_change_field = 'discount'
                    elif int(read) == 5:
                        to_change_field = 'order_date'
                    elif int(read) == 6:
                        to_change_field = 'shipped_date'
                    elif int(read) == 7:
                        to_change_field = 'customer_email'
                    read = input("Enter new data:")
                    collection.change(to_change_id, to_change_field, read, file_name)
                    # if to_change_field == 1:
                        # if Validators.validate_id(read):
                            # collection.change(to_change_id, to_change_field, read)
                    # elif to_change_id == 3:
                        # if Validators.validate_amount(read):
                            # collection.change(to_change_id, to_change_field, read)
                    # elif to_change_id == 6 or to_change_field == 5:
                        # if Validators.validate_date(read):
                            # collection.change(to_change_id, to_change_field, read)
                    # elif to_change_field == 2:
                        # if Validators.payment_validation(read):
                            # collection.change(to_change_id, to_change_field, read)
                    # elif to_change_field == 4:
                        # if Validators.validate_discount(read):
                            # collection.change(to_change_id, to_change_field, read)
                    # elif to_change_field == 7:
                        # if Validators.validate_email(read):
                            # collection.change(to_change_id, to_change_field, read)
                    # collection.rewriting_to_file(file_name)
            collection.print()
            print()
            print()
        elif menu_choice == 6:
            print("Have a nice day! Goodbye!")


main()
