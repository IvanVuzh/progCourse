import copy


class Memento:
    def __init__(self, given):
        self.state = copy.deepcopy(given)

    def get_memento_value(self):
        return self.state

    def print(self):
        self.state.print()
