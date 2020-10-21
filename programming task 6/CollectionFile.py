from OrderFile import Order
from DecoratorsFile import Validators
import copy


class Collection:
    class Memento:
        # Використати патерн Знімок (Memento) для зберігання останніх 5 дій користувача над  колекцією
        # екземплярів вказаного класу. Визначити два додаткові методи: undo, redo для повернення до n стану.
        max_memory = 5
        current_position = 0
        undone = 0

        def __init__(self):
            self.memorized_collections = []

        def get_len(self):
            return len(self.memorized_collections)

        def add_state(self, state_before_last_change):
            # print("Last state is\n")
            # state_before_last_change.print()
            if len(self.memorized_collections) == 5:
                self.memorized_collections.pop(0)
                self.memorized_collections.append(state_before_last_change)
            else:
                # print("Else")
                self.memorized_collections.insert(self.current_position, state_before_last_change)
                for i in range(self.current_position + 1, len(self.memorized_collections)):
                    self.memorized_collections.pop(i)
                self.current_position += 1
            self.undone = 0
            # self.show_memory()

        def undo(self, current_state):
            if self.current_position > 0:
                to_return = copy.deepcopy(self.memorized_collections.pop(self.current_position - 1))
                self.memorized_collections.insert(self.current_position, current_state)
                self.current_position -= 1
                self.undone += 1
                return to_return
            else:
                print("This is first state. There is nothing to undo")

        def redo(self, current_state):
            if self.undone > 0:
                to_return = copy.deepcopy(self.memorized_collections.pop(self.current_position))
                self.memorized_collections.insert(self.current_position, current_state)
                self.current_position += 1
                self.undone -= 1
                return to_return
            else:
                print("This is last state. There is noting to redo")

        def show_memory(self):
            if self.get_len() == 0:
                print("Memory is empty")
            else:
                i = 0
                for state in self.memorized_collections:
                    print("State ", i, ':')
                    state.print()
                    i += 1

    def __init__(self):
        self.list_of_orders = []
        self.memory = self.Memento()

    def undo(self):
        if self.memory.current_position > 0:
            to_remember = copy.deepcopy(self)
            self.list_of_orders = self.memory.undo(to_remember).list_of_orders
        else:
            print("This is first state. There is nothing to undo\n")

    def redo(self):
        if self.memory.current_position > 0:
            to_remember = copy.deepcopy(self)
            self.list_of_orders = self.memory.redo(to_remember).list_of_orders
        else:
            print("This is last state. There is noting to redo")

    def get_len(self):
        return len(self.list_of_orders)

    def add_existed_list(self, _list_of_orders):
        self.list_of_orders = _list_of_orders

    def add_order(self, order):
        to_memorize = copy.deepcopy(self)
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
        to_memorize = copy.deepcopy(self)
        self.memory.add_state(to_memorize)
        # self.memory.show_memory()
        del self.list_of_orders[identificator - 1]
        self.rewriting_to_file(file_name)

    def change(self, identificator, what_to_change, new_data, file_name):
        to_memorize = copy.deepcopy(self)
        self.memory.add_state(to_memorize)
        self.list_of_orders[identificator - 1].changer2(what_to_change, new_data)
        self.rewriting_to_file(file_name)

    def change2(self, number_of_editing_element, field_to_change, new_data, file_name):
        to_memorize = copy.deepcopy(self)
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
                if Order.str_to_order2(to_add, line, line_number) != 1:
                    to_add = Order.str_to_order2(to_add, line, line_number)
                    self.list_of_orders.append(to_add)
                else:
                    print("Data error in line " + str(i + 1))
                line_number += 1

    def rewriting_to_file(self, file_name):
        f = open(file_name, "w")
        for i in range(len(self.list_of_orders)):
            cut = i == len(self.list_of_orders) - 1
            self.list_of_orders[i].append_to_file(file_name, cut)
