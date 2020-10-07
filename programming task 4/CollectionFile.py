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

from OrderFile import Order
import os


def file_not_empty(file_name):
    if os.stat(file_name).st_size == 0:
        return False
    else:
        return True


class Collection:
    def __init__(self):
        self.list_of_orders = []

    def get_len(self):
        return len(self.list_of_orders)

    def add_existed_list(self, _list_of_orders):
        self.list_of_orders = _list_of_orders

    def add_order(self, order):
        self.list_of_orders.append(order)

    def search(self, data):
        for i in range(len(self.list_of_orders)):
            self.list_of_orders[i].for_search(data)

    def sort(self, user_choice):
        if user_choice == 1:
           self.list_of_orders.sort(key=lambda Order: Order.id)
        if user_choice == 2:
            self.list_of_orders.sort(key=lambda Order: Order.order_status)
        if user_choice == 3:
            self.list_of_orders.sort(key=lambda Order: Order.amount)
        if user_choice == 4:
            self.list_of_orders.sort(key=lambda Order: Order.discount)
        if user_choice == 5:
            self.list_of_orders.sort(key=lambda Order: Order.order_date)
        if user_choice == 6:
            self.list_of_orders.sort(key=lambda Order: Order.shipped_date)
        if user_choice == 7:
            self.list_of_orders.sort(key=lambda Order: Order.customer_email)

    def print(self):
        for i in range(len(self.list_of_orders)):
            self.list_of_orders[i].print()

    def deleter(self, identificator, file_name):
        del self.list_of_orders[identificator]
        self.rewriting_to_file(file_name)

    def change(self, identificator, what_to_change, new_data):
        self.list_of_orders[identificator - 1].changer(what_to_change, new_data)

    def read_from_file(self, file_name):
        if file_not_empty(file_name):
            f = open(file_name)
            lines = f.readlines()
            to_add = Order(0, "n/a", 0, 0, 1970, 1, 1, 1970, 1, 1, "n/a")
            for i in range(len(lines)):
                line = lines[i]
                if i != len(lines) - 1:
                    line = line[:-1]
                to_add = to_add.make(line)
                self.list_of_orders.append(to_add)

    def rewriting_to_file(self, file_name):
        f = open(file_name, "w")
        for i in range(len(self.list_of_orders)):
            self.list_of_orders[i].append_to_file(file_name)
