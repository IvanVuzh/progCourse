from Caretaker import *
from Memento import *
from DecoratorsFile import *
from OrderFile import Order


class Collection:

    def __init__(self):
        self.list_of_orders = []
        self.memory = Caretaker()

    def undo(self):
        print("undo")
        if self.memory.current_position > 0:
            to_remember = Memento(self)
            self.list_of_orders = self.memory.undo(to_remember).get_memento_value().list_of_orders
        else:
            print("#######This is first state. There is nothing to undo#######\n")

    def redo(self):
        if self.memory.undone > 0:
            to_remember = Memento(self)
            self.list_of_orders = self.memory.redo(to_remember).get_memento_value().list_of_orders
        else:
            print("#######This is last state. There is noting to redo#######\n")

    def get_len(self):
        return len(self.list_of_orders)

    def add_existed_list(self, _list_of_orders):
        self.list_of_orders = _list_of_orders

    def add_order(self, order):
        to_memorize = Memento(self)
        self.memory.add_state(to_memorize)
        self.list_of_orders.append(order)

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

    def print(self):
        for i in range(len(self.list_of_orders)):
            print(self.list_of_orders[i].make_str_for_print())

    def deleter(self, identificator, file_name):
        to_memorize = Memento(self)
        self.memory.add_state(to_memorize)
        # self.memory.show_memory()
        del self.list_of_orders[identificator - 1]
        self.rewriting_to_file(file_name)

    def change(self, identificator, what_to_change, new_data, file_name):
        to_memorize = Memento(self)
        self.memory.add_state(to_memorize)
        self.list_of_orders[identificator - 1].changer2(what_to_change, new_data)
        self.rewriting_to_file(file_name)

    def change2(self, number_of_editing_element, field_to_change, new_data, file_name):
        to_memorize = Memento(self)
        self.memory.add_state(to_memorize)
        self.list_of_orders[number_of_editing_element - 1].edit_data(field_to_change, new_data)
        self.rewriting_to_file(file_name)

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

    def rewriting_to_file(self, file_name):
        f = open(file_name, "w")
        for i in range(len(self.list_of_orders)):
            cut = i == len(self.list_of_orders) - 1
            self.list_of_orders[i].append_to_file(file_name, cut)
