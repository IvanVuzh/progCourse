# Створити клас: колекція, який буде працювати з масивом екземплярів класу.
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
import os
from OrderFile import Order
from ValidationFile import Validators


class Collection:
    def __init__(self):
        self.list_of_orders = []

    def get_len(self):
        return len(self.list_of_orders)

    def add_existed_list(self, _list_of_orders):
        self.list_of_orders = _list_of_orders

    def add_order(self, order, file_name):
        self.list_of_orders.append(order)
        self.rewriting_to_file(file_name)

    def search(self, data):
        for i in range(len(self.list_of_orders)):
            self.list_of_orders[i].for_search(data)

    def sort(self, user_choice):
        if (user_choice == 'id'
                or user_choice == 'amount'
                or user_choice == 'discount'):
            self.list_of_orders.sort(key=lambda Order: int(getattr(Order, Order.attr_dict[user_choice])))
        else:
            for name in Order.attr_dict:
                if user_choice == name:
                    self.list_of_orders.sort(key=lambda Order: getattr(Order, Order.attr_dict[name]))

    # def edit_order(self):

    def print(self):
        for i in range(len(self.list_of_orders)):
            print(self.list_of_orders[i].make_str_for_print())

    def deleter(self, identificator, file_name):
        del self.list_of_orders[identificator - 1]
        self.rewriting_to_file(file_name)

    def change(self, identificator, what_to_change, new_data, file_name):
        self.list_of_orders[identificator - 1].changer2(what_to_change, new_data)
        self.rewriting_to_file(file_name)

    def read_from_file(self, file_name):
        if Validators.file_not_empty(file_name):
            f = open(file_name)
            lines = f.readlines()
            # print(to_add.make_str())
            for i in range(len(lines)):
                to_add = Order
                line = lines[i]
                if i != len(lines) - 1:
                    line = line[:-1]
                # print("line is:", line)
                if Order.str_to_order(to_add, line) == 1:
                    print("Data error in line " + str(i + 1))
                else:
                    to_add = Order.str_to_order(to_add, line)
                    self.list_of_orders.append(to_add)

    def rewriting_to_file(self, file_name):
        f = open(file_name, "w")
        for i in range(len(self.list_of_orders)):
            cut = i == len(self.list_of_orders) - 1
            self.list_of_orders[i].append_to_file(file_name, cut)
