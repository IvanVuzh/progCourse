# Клас ЗАМОВЛЕННЯ: ID, order_status (paid, refunded, not paid), amount, discount (percentage),
# order_date, shipped_date, customer_email
import datetime
import re
from DecoratorsFile import Validators


def dates_check(date1, date2):
    try:
        datetime.datetime.strptime(date1, '%Y-%m-%d')
        datetime.datetime.strptime(date2, '%Y-%m-%d')
        return True
    except ValueError:
        return False


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
               'amount': 'set_amount',
               'discount': 'set_discount',
               'order_date': 'set_order_date',
               'shipped_date': 'set_shipped_date',
               'customer_email': 'set_email'}
    error_messages = ["Error in line (wrong id in line)",
                      "Error in line (wrong order status in line)",
                      "Error in line (wrong amount in line)",
                      "Error in line (wrong discount in line)",
                      "Error in line (wrong order date in line)",
                      "Error in line (wrong shipped date in line)",
                      "Error in line (wrong customer email in line)"]

    def __init__(self, dict_of_data):
        for key in dict_of_data:
            setattr(self, key, dict_of_data[key])

    def str_to_order(self, line):
        line = line.split(", ")
        all_is_validated = True
        error_list = []
        line_iter = 0
        for field in self.attr_dict:
            validator_name = Validators.validators_of_order_fields[field]
            if not getattr(Validators, validator_name)(line[line_iter]):
                error_list.append(line_iter)
                all_is_validated = False
            if line_iter != len(line):
                line_iter += 1
            if dates_check(line[4], line[5]):
                all_is_validated = Validators.two_dates_validation(line[4], line[5])
        if all_is_validated:
            dictionary = self.attr_dict.copy()
            i = 0
            for name in self.attr_dict:
                dictionary[name] = line[i].lower()
                i += 1
            res = Order(dictionary)
            return res
        else:
            for error in error_list:
                print(self.error_messages[error])
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
            if re.search(str(data), getattr(self, self.attr_dict[name])):
                print("Result:")
                print(self.make_str_for_print())