# Клас ЗАМОВЛЕННЯ: ID, order_status (paid, refunded, not paid), amount, discount (percentage),
# order_date, shipped_date, customer_email
import datetime
import re
from DecoratorsFile import Validators


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
    setters = {'id': 'set_id',
               'order_status': 'set_status',
               'amount': 'amount',
               'discount': 'discount',
               'order_date': 'order_date',
               'shipped_date': 'shipped_date',
               'customer_email': 'customer_email'}
    error_messages = ["Error in line (wrong id in line)",
                      "Error in line (wrong order status in line)",
                      "Error in line (wrong amount in line)",
                      "Error in line (wrong discount in line)",
                      "Error in line (wrong order date in line)",
                      "Error in line (wrong shipped date in line)",
                      "Error in line (wrong customer email in line)"]

    def __init__(self, dict_of_data):
        for key in dict_of_data:
            # print("key is", key, "\t value is", dict_of_data[key])
            setattr(self, key, dict_of_data[key])

    def str_to_order2(self, line):
        line = line.split(", ")
        # print("line = ", line)
        all_is_validated = True
        error_list = []
        line_iter = 0
        # print(line)
        for field in self.attr_dict:
            validator_name = Validators.validators_of_order_fields[field]
            if not getattr(Validators, validator_name)(line[line_iter]):
                error_list.append(line_iter)
                all_is_validated = False
            if line_iter != len(line):
                line_iter += 1
        if datetime.datetime.strptime(line[4], '%Y-%m-%d') > datetime.datetime.strptime(line[5], '%Y-%m-%d'):
            print("Error in line (order was made after shipping (change dates))")
            all_is_validated = False
        if all_is_validated:
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
            for error in error_list:
                print(self.error_messages[error])
            # print("######## Caught an error in data file in line", line_number + 1, "########")
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

    def append_to_file(self, file_name, cut):
        if Validators.file_exists(file_name):
            file = open(file_name, "a")
            line = self.make_str_for_file()
            if cut:
                line = line[:-1]
            file.write(line)
        else:
            print("Error occurred while trying to append to file. File does no exists")

    def changer2(self, choice, new_data):
        for key in self.attr_dict:
            if key == choice:
                setattr(self, key, new_data)

    def edit_data(self, field_to_edit, new_data):
        validator_name = Validators.validators_of_order_fields[field_to_edit]
        if getattr(Validators, validator_name)(new_data):
            setattr(self, self.setters[field_to_edit], new_data)
        else:
            print("Wrong info entered")

    @Validators.id_decorator
    def set_id(self, new_id):
        setattr(self, 'id', new_id)
        return True

    @Validators.status_decorator
    def set_status(self, new_status):
        setattr(self, 'order_status', new_status)
        return True

    @Validators.amount_decorator
    def set_amount(self, new_amount):
        setattr(self, 'amount', new_amount)
        return True

    @Validators.discount_decorator
    def set_discount(self, new_discount):
        setattr(self, 'discount', new_discount)
        return True

    @Validators.date_decorator
    def set_order_date(self, new_order_date):
        setattr(self, 'order_date', new_order_date)
        return True

    @Validators.date_decorator
    def set_shipped_date(self, new_shipped):
        setattr(self, 'shipped_date', new_shipped)
        return True

    @Validators.email_decorator
    def set_email(self, new_email):
        setattr(self, 'customer_email', new_email)
        return True

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
