class Iterator:
    def __init__(self, n):
        self.x = 0
        self.amount = n
        self.returned = 0
        # print("self.x = " + str(self.x))

    def __iter__(self):
        return self

    def __next__(self):
        if self.returned == self.amount:
            # print("raise StopIteration")
            raise StopIteration
        self.returned += 1
        while True:
            self.x += 1
            sum = self.x
            current_dilnyk = 1
            if self.amount == 1:
                return 1
            if self.amount > 1:
                # print("if self.amount > 1:")
                while current_dilnyk != self.x:
                    if self.x % current_dilnyk == 0:
                        sum -= current_dilnyk
                    current_dilnyk += 1
                if sum == 0:
                    # print("returning " + str(self.x))
                    return self.x
