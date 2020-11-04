from CollectionFile import *
import copy


class Caretaker:
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
        if len(self.memorized_collections) == self.max_memory:
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
        print("undone=", self.undone)
        # print("cur pos =", self.current_position)
        if self.current_position > 0:
            to_return = copy.deepcopy(self.memorized_collections.pop(self.current_position - 1))
            # to_return =
            self.memorized_collections.insert(self.current_position, current_state)
            self.current_position -= 1
            # print("cur pos =", self.current_position)
            self.undone += 1
            print("undone=", self.undone)
            return to_return
        else:
            print("This is first state. There is nothing to undo")

    def redo(self, current_state):
        # print(self.undone)
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