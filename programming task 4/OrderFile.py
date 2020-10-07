# Клас ЗАМОВЛЕННЯ: ID, order_status (paid, refunded, not paid), amount, discount (percentage),
# order_date, shipped_date, customer_email
import datetime as dt
import re
from ValidationFile import Validators


class Order:
    def __init__(self, _id, _order_status, _amount, _discount, order_date_year, order_date_month, order_date_day,
                 shipped_date_year, shipped_date_month, shipped_date_day, _customer_email):
        if Validators.validate_amount_or_id(_id):
            self.id = int(_id)
        # else:
            # print("Wrong id")
        if Validators.payment_validation(_order_status):
            self.order_status = _order_status
        if Validators.validate_amount_or_id(_amount):
            self.amount = _amount
        if Validators.validate_discount(_discount):
            self.discount = _discount
        if Validators.validate_date(dt.datetime(order_date_year, order_date_month, order_date_day)):
            self.order_date = dt.datetime(order_date_year, order_date_month, order_date_day)
        if Validators.validate_date(dt.datetime(shipped_date_year, shipped_date_month, shipped_date_day)):
            self.shipped_date = dt.datetime(shipped_date_year, shipped_date_month, shipped_date_day)
        if Validators.validate_email(_customer_email):
            self.customer_email = _customer_email

    def print(self):
        print("Order info:")
        print("ID:", self.id, end="\t")
        print("Order status:", self.order_status, end="\t")
        print("Amount of products:", self.amount, end="\t")
        print("Discount:", self.discount, '%', end="\t")
        print("Order date:", self.order_date.strftime("%x"), end="\t")
        print("Shipped date:", self.shipped_date.strftime("%x"), end="\t")
        print("Customer email:", self.customer_email, end="\n")

    def read(self, file_name, line_number):
        import linecache
        line = linecache.getline(file_name, line_number)
        # print("Line is ", line)
        line = line.split(", ")
        if (Validators.validate_amount_or_id(line[0]) and Validators.payment_validation(line[1]) and
                Validators.validate_amount_or_id(line[2]) and Validators.validate_discount(line[3]) and
                Validators.validate_date(dt.datetime(int(line[4]), int(line[5]), int(line[6]))) and
                Validators.validate_date(dt.datetime(int(line[7]), int(line[8]), int(line[9]))) and
                Validators.validate_email(line[10])):
            result = Order(line[0], line[1], line[2], line[3], int(line[4]), int(line[5]), int(line[6]), int(line[7]),
                       int(line[8]), int(line[9]), line[10])
            return result
        else:
            print("Error in file (wrong typename in line", line_number, ")!")

    def append_to_file(self, file_name):
        file = open(file_name, "a")
        line = (str(self.id) + ", " + str(self.order_status) + ", " + str(self.amount) + ", " + str(self.discount)
                + ", " + self.order_date.strftime("%Y") + ", " + self.order_date.strftime("%m") + ", " +
                self.order_date.strftime("%d") + ", " + self.shipped_date.strftime("%Y") + ", " +
                self.order_date.strftime("%m") + ", " + self.order_date.strftime("%d") + ", " +
                str(self.customer_email) + "\n")
        file.write(line)

    def make(self, line):
        line = line.split(", ")
        # print("line = ", line)
        if (Validators.validate_amount_or_id(line[0]) and Validators.payment_validation(line[1]) and
                Validators.validate_amount_or_id(line[2]) and Validators.validate_discount(line[3]) and
                Validators.validate_date(dt.datetime(int(line[4]), int(line[5]), int(line[6]))) and
                Validators.validate_date(dt.datetime(int(line[7]), int(line[8]), int(line[9]))) and
                Validators.validate_email(line[10])):
            result = Order(int(line[0]), line[1], int(line[2]), int(line[3]), int(line[4]), int(line[5]), int(line[6]), int(line[7]),
                        int(line[8]), int(line[9]), line[10])
        # result.print()
            return result
        else:
            print("Error in file (wrong typename in line)")

    def changer(self, choice, new_data):
        if choice == 1 and Validators.validate_amount_or_id(new_data):
            self.id = new_data
        if choice == 2 and Validators.payment_validation(new_data):
            self.order_status = new_data
        if choice == 3 and Validators.validate_amount_or_id(new_data):
            self.amount = new_data
        if choice == 4 and Validators.validate_discount(new_data):
            self.discount = new_data
        if choice == 5 and Validators.validate_date(new_data):
            self.order_date = new_data
        if choice == 6 and Validators.validate_date(new_data):
            self.shipped_date = new_data
        if choice == 7 and Validators.validate_email(new_data):
            self.customer_email = new_data

    def for_search(self, data):
        if re.search(str(data), str(self.id)):
            print("Result:")
            self.print()
        elif data == self.amount:
            print("Result:")
            self.print()
        elif re.search(str(data), str(self.order_status)):
            # re.search не юзати бо paid i not paid будуть показуватись разом?
            print("Result:")
            self.print()
        elif data == self.discount:
            print("Result:")
            self.print()
        elif re.search(str(data), self.order_date.strftime("%Y")) or re.search(str(data), self.order_date.strftime("%d")) or re.search(str(data), self.order_date.strftime("%m")):
            print("Result:")
            self.print()
        elif re.search(str(data), self.order_date.strftime("%x")):
            print("Result:")
            self.print()
        elif re.search(str(data), self.shipped_date.strftime("%Y")) or re.search(str(data), self.shipped_date.strftime("%d")) or re.search(str(data), self.shipped_date.strftime("%m")):
            print("Result:")
            self.print()
        elif re.search(str(data), self.shipped_date.strftime("%x")):
            print("Result:")
            self.print()
        elif re.search(str(data), self.customer_email):
            print("Result:")
            self.print()
# Створити клас та включити в нього необхідні конструктори та методи доступу до полів класу. Перевантажити операції
# введення, виведення в потік та інші, які необхідні для виконання завдання. Вхідні дані зчитувати з текстового файлу.
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
