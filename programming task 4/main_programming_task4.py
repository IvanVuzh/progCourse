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
menu_choice = 0
collection = Collection()
file_name = "data.txt"
collection.read_from_file(file_name)
adding = Order(1, "not paid", 1, 0, 1970, 1, 1, 1970, 1, 1, "noemail@gmail.com")
# adding.print()
# obj = dt.datetime(2019, 10, 19)
# print(obj.strftime("%x"))
# collection.print()
while menu_choice != 7:
    print("You are in main menu. Possible options:\n"
          "1 - print collection of orders\n"
          "2 - search some data through all info\n"
          "3 - sort collection by some argument\n"
          "4 - delete any order(by its number in list) and rewrite collection in file\n"
          "5 - add an order and rewrite collection in file\n"
          "6 - edit an order and rewrite collection in file\n"
          "7 - exit program\n"
          "Choose your option: ")
    read = input()
    while not Validators.menu_choice_and_sort_and_changer_validation(read):
        read = input()
    menu_choice = int(read)
    if menu_choice == 1:
        collection.print()
        print()
        print()
    elif menu_choice == 2:
        read = input("Enter data to be searched:")
        collection.search(read)
        print()
        print()
    elif menu_choice == 3:
        read = input("Enter a parameter to be sorted by:\n"
                     "1 -id\n"
                     "2 - order status\n"
                     "3 - amount of product bought\n"
                     "4 - discount\n"
                     "5 - order date\n"
                     "6 - shipped date\n"
                     "7 - customer email\n")
        while not Validators.menu_choice_and_sort_and_changer_validation(read):
            read = input()
        collection.sort(int(read))
        collection.print()
        print()
        print()
    elif menu_choice == 4:
        read = input("Enter a number of order to be deleted(enter 0 not to delete anything)")
        if represents_int(read):
            while collection.get_len() < int(read) or 0 > int(read):
                read = input("Reenter a number of order to be deleted(enter 0 not to delete anything)")
            if int(read) == 0:
                break
            else:
                collection.deleter(int(read), file_name)
        print()
        print()
    elif menu_choice == 5:
        print("Enter a LINE which is similar to (with a ', ' as a delimiter or enter 0 to skip)\n"
              "ID, order_status (paid, refunded, not paid), amount, discount (percentage), "
              "order_date, shipped_date, customer_email")
        read = input()
        if represents_int(read) and int(read) == 0:
            pass
        else:
            adding.make(read)
            collection.add_order(adding)
            collection.rewriting_to_file(file_name)
        print()
        print()
    elif menu_choice == 6:
        read = input("Enter a number of order to be changed (enter 0 not ot change anything):")
        if represents_int(read):
            while collection.get_len() < int(read) or 0 > int(read):
                read = input("Reenter a number of order to be deleted(enter 0 not to delete anything)")
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
                while not Validators.menu_choice_and_sort_and_changer_validation(int(read)) or not represents_int(read):
                    read = input("Reenter an info to be changed")
                to_change_field = int(read)
                read = input("Enter new data:")
                if to_change_field == 1 or to_change_field == 3:
                    if Validators.validate_amount_or_id(read):
                        collection.change(to_change_id, to_change_field, read)
                elif to_change_id == 6 or to_change_field == 5:
                    if Validators.validate_date(read):
                        collection.change(to_change_id, to_change_field, read)
                elif to_change_field == 2:
                    if Validators.payment_validation(read):
                        collection.change(to_change_id, to_change_field, read)
                elif to_change_field == 4:
                    if Validators.validate_discount(read):
                        collection.change(to_change_id, to_change_field, read)
                elif to_change_field == 7:
                    if Validators.validate_email(read):
                        collection.change(to_change_id, to_change_field, read)
                collection.rewriting_to_file(file_name)
        print()
        print()
    elif menu_choice == 7:
        print("Have a nice day! Goodbye!")
