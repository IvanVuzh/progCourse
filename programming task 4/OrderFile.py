# Клас ЗАМОВЛЕННЯ: ID, order_status (paid, refunded, not paid), amount, discount (percentage),
# order_date, shipped_date, customer_email
import datetime
import re
from ValidationFile import Validators


def get_data_from_dict_by_key(dict_of_data, key):
    return dict_of_data[key]


class Order:
    attr_dict = {'id': 'id',
                 'order_status': 'order_status',
                 'amount': 'amount',
                 'discount': 'discount',
                 'order_date': 'order_date',
                 'shipped_date': 'shipped_date',
                 'customer_email': 'customer_email'}

    def __init__(self, dict_of_data):
        for key in dict_of_data:
            # print("key is", key, "\t value is", dict_of_data[key])
            setattr(self, key, dict_of_data[key])

    def str_to_order(self, line):
        line = line.split(", ")
        # print("line = ", line)
        is_error = False
        date_error = False
        if not Validators.validate_id(line[0]):
            print("Error in line (wrong id in line). Wrong data: " + line[0])
            is_error = True
        if not Validators.payment_validation(line[1]):
            print("Error in line (wrong order status in line). Wrong data: " + line[1])
            is_error = True
        if not Validators.validate_amount(line[2]):
            print("Error in line (wrong amount in line). Wrong data: " + line[2])
            is_error = True
        if not Validators.validate_discount(line[3]):
            print("Error in line (wrong discount in line). Wrong data: " + line[3])
            is_error = True
        if not Validators.validate_date(line[4]):   # still raising an error
            print("Error in line. Wrong order date in line. Incorrect data format, should be YYYY-MM-DD. Wrong data: "
                  + line[4])
            is_error = True
            date_error = True
        if not Validators.validate_date(line[5]):   # still raising an error
            print("Error in line. Wrong shipped date in line. Incorrect data format, should be YYYY-MM-DD. Wrong data: "
                  + line[5])
            is_error = True
            date_error = True
        if not date_error:
            if datetime.datetime.strptime(line[4], '%Y-%m-%d') > datetime.datetime.strptime(line[5], '%Y-%m-%d'):
                print("Error in line (order was made after shipping (change dates))")
                is_error = True
        if not Validators.validate_email(line[6]):
            print("Error in line (wrong email in line). Wrong data: " + line[6])
            is_error = True
        if not is_error:
            dictionary = self.attr_dict.copy()
            i = 0
            for name in self.attr_dict:
                # print(dictionary[name] + "=" + line[i])
                dictionary[name] = line[i].lower()
                # print(dictionary[name])
                i += 1
            # print("Created dictionary is", dictionary)
            res = Order(dictionary)
            return res
        else:
            print("######## Caught an error in data file ########")
            return 1

    def make_str_for_print(self):
        to_print = "#################################################################\n" \
                   "Order info: \n"
        for name in self.attr_dict:
            to_print += name + ': ' + str(getattr(self, self.attr_dict[name])) + '\n'
        to_print += "#################################################################"
        return to_print

    def make_str_for_file(self):
        to_write = ''
        for q in self.attr_dict:
            to_write += str(getattr(self, self.attr_dict[q])) + ', '
        to_write = to_write[:-2]
        to_write += '\n'
        return to_write
    # def read(self, file_name, line_number):
        # import linecache
        # line = linecache.getline(file_name, line_number)
        # print("Line is ", line)
        # line = line.split(", ")
        # if (Validators.validate_amount_or_id(line[0]) and Validators.payment_validation(line[1]) and
                # Validators.validate_amount_or_id(line[2]) and Validators.validate_discount(line[3]) and
                # Validators.validate_date(dt.datetime(int(line[4]), int(line[5]), int(line[6]))) and
                # Validators.validate_date(dt.datetime(int(line[7]), int(line[8]), int(line[9]))) and
                # Validators.validate_email(line[10])):
            # result = Order(line[0], line[1], line[2], line[3], int(line[4]), int(line[5]), int(line[6]), int(line[7]),
                       # int(line[8]), int(line[9]), line[10])
            # return result
        # else:
            # print("Error in file (wrong typename in line", line_number, ")!")

    def append_to_file(self, file_name, cut):
        if Validators.file_exists(file_name):
            file = open(file_name, "a")
            line = self.make_str_for_file()
            if cut:
                line = line[:-1]
            file.write(line)
        else:
            print("Error occurred while trying to append to file. File does no exists")

    # def changer(self, choice, new_data):
        # if choice == 1 and Validators.validate_id(new_data):
            # self.id = new_data
        # if choice == 2 and Validators.payment_validation(new_data):
            # self.order_status = new_data
        # if choice == 3 and Validators.validate_amount(new_data):
            # self.amount = new_data
        # if choice == 4 and Validators.validate_discount(new_data):
            # self.discount = new_data
        # if choice == 5 and Validators.validate_date(new_data):
            # self.order_date = new_data
        # if choice == 6 and Validators.validate_date(new_data):
            # self.shipped_date = new_data
        # if choice == 7 and Validators.validate_email(new_data):
            # self.customer_email = new_data

    def changer2(self, choice, new_data):
        for key in self.attr_dict:
            if key == choice:
                setattr(self, key, new_data)

    def for_search(self, data):
        for name in self.attr_dict:
            # print("Search in:", getattr(self, self.attr_dict[name]))
            if re.search(str(data), getattr(self, self.attr_dict[name])):
                print("Result:")
                print(self.make_str_for_print())
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
