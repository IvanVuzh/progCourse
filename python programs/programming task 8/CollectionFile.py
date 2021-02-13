from Caretaker import *
from Memento import *
from DecoratorsFile import *
from OrderFile import Order
import json


def truncate_utf8_chars(filename, count, ignore_newlines=True):
    """
    Truncates last `count` characters of a text file encoded in UTF-8.
    :param filename: The path to the text file to read
    :param count: Number of UTF-8 characters to remove from the end of the file
    :param ignore_newlines: Set to true, if the newline character at the end of the file should be ignored
    """
    with open(filename, 'rb+') as f:
        last_char = None

        size = os.fstat(f.fileno()).st_size

        offset = 1
        chars = 0
        while offset <= size:
            f.seek(-offset, os.SEEK_END)
            b = ord(f.read(1))

            if ignore_newlines:
                if b == 0x0D or b == 0x0A:
                    offset += 1
                    continue

            if b & 0b10000000 == 0 or b & 0b11000000 == 0b11000000:
                # This is the first byte of a UTF8 character
                chars += 1
                if chars == count:
                    # When `count` number of characters have been found, move current position back
                    # with one byte (to include the byte just checked) and truncate the file
                    f.seek(-1, os.SEEK_CUR)
                    f.truncate()
                    return
            offset += 1


class Collection:

    def __init__(self):
        self.list_of_orders = []
        self.memory = Caretaker()

    def undo(self):
        # print("undo")
        if self.memory.current_position > 0:
            to_remember = copy.deepcopy(Memento(self))
            self.list_of_orders = self.memory.undo(to_remember)
            # print("List of orders is", type(self.list_of_orders))
        else:
            print("#######This is first state. There is nothing to undo#######\n")

    def redo(self):
        if self.memory.undone > 0:
            to_remember = copy.deepcopy(Memento(self))
            self.list_of_orders = self.memory.redo(to_remember)
            # print("List of orders is", type(self.list_of_orders))
        else:
            print("#######This is last state. There is noting to redo#######\n")

    def get_len(self):
        return len(self.list_of_orders)

    def add_existed_list(self, _list_of_orders):
        self.list_of_orders = _list_of_orders

    def add_order(self, order):
        id_conflict = False
        for i in self.list_of_orders:
            if i.id == order.id:
                id_conflict = True
        if not id_conflict:
            to_memorize = Memento(self)
            self.memory.add_state(to_memorize)
            self.list_of_orders.append(order)

        """else:
            print("Order with such id already exists")
            new_id = input("Enter new id: ")
            order.set_id(new_id)
            self.add_order(order)"""    # працює тільки з консольним вводом :(

    def get_by_id(self, id_to_find):
        for i in self.list_of_orders:
            # print(i.make_str_for_print())
            if int(i.id) == int(id_to_find):
                # print("Found")
                return i
        return False

    def search(self, data):
        res = []
        for i in self.list_of_orders:
            if i.found_for_search(data):
                res.append(i.order_to_dict())
        return res

    def sort(self, sort_field, sort_direction):
        if (sort_field == 'id'
                or sort_field == 'amount'
                or sort_field == 'discount'):
            self.list_of_orders.sort(key=lambda Order: int(getattr(Order, Order.attr_dict[sort_field])))
        else:
            for name in Order.attr_dict:
                if sort_field == name:
                    self.list_of_orders.sort(key=lambda Order: getattr(Order, Order.attr_dict[name]))
        if sort_direction == 'desc':
            self.list_of_orders.reverse()
        return self.return_list_of_dicts()

    def print(self):
        for i in range(len(self.list_of_orders)):
            print(self.list_of_orders[i].make_str_for_print())

    def deleter(self, order_id):
        to_memorize = Memento(self)
        self.memory.add_state(to_memorize)
        # self.memory.show_memory()
        deleted = False
        for identifier in range(self.get_len() - 1):
            # print("iden=", identifier)
            if int(order_id) == self.list_of_orders[identifier].id:
                del self.list_of_orders[identifier]
                deleted = True
        return deleted

    def change2(self, order_id, what_to_change, new_data, file_name):
        to_memorize = Memento(self)
        self.memory.add_state(to_memorize)
        for identifier in range(self.get_len()):
            if order_id == self.list_of_orders[identifier].id:
                self.list_of_orders[identifier].changer2(what_to_change, new_data)
        self.rewriting_to_file(file_name)

    """
    def read_from_file(self, file_name):
        if Validators.file_not_empty(file_name):
            f = open(file_name)
            lines = f.readlines()
            # print(to_add.make_str())
            line_number = 0
            for i in range(len(lines)):
                to_add = Order
                line = lines[i]
                if i != len(lines) - 1:
                    line = line[:-1]
                # print("line is:", line)
                if Order.str_to_order2(to_add, line) != 1:
                    to_add = Order.str_to_order2(to_add, line)
                    self.list_of_orders.append(to_add)
                else:
                    print("Data error in line " + str(i + 1))
                line_number += 1
    """

    @Validators.read_from_file_decorator
    def read_from_file(self, file_name):
        f = open(file_name)
        data = json.load(f)
        for_error_iterator = 1
        for element in data:
            id_conflict = False
            to_add = Order(element)
            for i in self.list_of_orders:
                if i.id == to_add.id:
                    id_conflict = True
            if to_add.id != 0 and not id_conflict:
                self.list_of_orders.append(to_add)
            else:
                print("Error in element №", for_error_iterator)
            for_error_iterator += 1
        f.close()

    def rewriting_to_file(self, file_name):
        """with open(file_name, 'a') as file:
            for order in self.list_of_orders:
                to_file = order.order_to_dict()
                json.dump(to_file, file)"""
        dict_list = self.return_list_of_dicts()
        with open(file_name, 'w') as file:
            file.write(json.dumps(dict_list, indent=4))

    def return_list_of_dicts(self):
        dict_list = []
        for i in self.list_of_orders:
            dict_list.append(i.order_to_dict())
        return dict_list

    def edit_all_fields(self, order_id, new_data_dict):
        secure = copy.deepcopy(self.get_by_id(order_id).order_to_dict())
        valid = True
        to_return = dict()
        errors = dict()
        work_with = self.get_by_id(order_id)
        for i in new_data_dict:
            if i == 'id':
                if self.get_by_id(new_data_dict[i]):
                    valid = False
                    to_return['status'] = '400'
                    to_return['message'] = 'Invalid Input'
                    errors[i] = 'Such id is already used'

            if not work_with.edit_value(i, new_data_dict[i]):
                if valid is True:
                    valid = False
                    to_return['status'] = '400'
                    to_return['message'] = 'Wrong Input'
                errors[i] = 'Invalid input'
                to_return['errors'] = errors

        if not valid:
            self.edit_all_fields(order_id, secure)
        else:
            to_return['status'] = '200'
            to_return['message'] = 'Customer has been successfully updated.'
            to_return['customer'] = self.get_by_id(work_with.id).order_to_dict()
        return to_return
