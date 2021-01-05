from Validation import Validators


class Context:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, _strategy):
        self.strategy = _strategy

    def get_strategy(self):
        return self.strategy

    @Validators.decorator_context
    def generate(self, l_list, pos, given):
        if self.strategy is not None:
            return self.strategy.generate(l_list, pos, given)
        else:
            print('No strategy chosen')
            return False
