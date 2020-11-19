from Validation import Validators
from Validation import represents_int
from LList import LinkedList
from Iterator import Iterator


class Strategy:
    @staticmethod
    def generate(linked_list, pos, insertion):  # linked list is starting list
        given_list = linked_list
        first_part = insertion

        if given_list.size() == 0:
            return insertion
        else:
            current = given_list.head
            iter = 0
            while current.next_node:
                # print("current.next_node while 1 else")
                if int(pos) == iter:
                    first_part.get_last_node().next_node = current
                    break
                iter += 1

        if int(pos) == 0:
            return first_part

        else:
            # print("entered pos", pos)
            # if given_list.size() != 0:
            current = given_list.head
            iterator = 0
            while current.next_node:
                # print("current.next_node while 2 else", pos)
                iterator += 1
                if int(pos) == iterator:
                    current.next_node = first_part.head
                    break
        return given_list
# Якщо вибрана стратегія 1
# Вхідні дані:
# Позиція вставки
# Вихідні дані:
# Згенерований список


class StrategyOne(Strategy):
    @Validators.amount_deco
    def generate(self, linked_list, pos, amount):
        rez = Iterator(int(amount))
        to_return = LinkedList()
        for num in rez:
            to_return.add_tail(num)
        return super().generate(linked_list, pos, to_return)


class StrategyTwo(Strategy):
    @Validators.file_deco
    def generate(self, linked_list, pos, file_name):
        f = open(file_name)
        to_ints = f.read()
        to_ints = to_ints.split(", ")
        res = LinkedList()
        for i in range(len(to_ints)):
            if represents_int(to_ints[i]):
                to_ints[i] = int(to_ints[i])
                res.add_tail(to_ints[i])
            else:
                print("Element ", to_ints[i], "in file is not int. Its position is ", i + 1)
        return super().generate(linked_list, pos, res)


