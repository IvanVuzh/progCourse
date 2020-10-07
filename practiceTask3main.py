from random import seed
from random import randint


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def add_head(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        index_arr = []
        it = 0
        current = self.head
        found = False
        while current:
            if current.get_data() == int(data):
                index_arr.append(it)
                found = True
                # print("Found K in x")
            current = current.get_next()
            it += 1
        # if current is None and found == False: # зайва *****, яка перериває програму
            # raise ValueError("Data not in list")
        return index_arr

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next_node):
            last = last.next_node
        last.next_node = new_node

    def print(self):
        current = self.head
        while current:
            print(current.get_data(), end=" ")
            current = current.get_next()
        print()

    def biggest(self):
        current = self.head
        biggest = int(current.data)
        while current:
            if int(current.data) > biggest:
                  biggest = int(current.data)
            current = current.get_next()
        return biggest

    def no_positive(self):
        current = self.head
        res = True
        while current:
            if int(current.data) > 0:
                res = False
            current = current.get_next()
        return res

    def cubing(self, n):
        current = self.head
        for i in range(n):
            new_val = current.data * current.data
            current.data = new_val
            current = current.get_next()


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def validator(N):
    if(RepresentsInt(N)):
        return True
    else:
        print(N, 'is not an integer!')
        return False


def cubing(self, n):
    current = self.head
    for i in range(n):
        new_val = current.data * current.data
        current.data = new_val
        current = current.get_next()
    return self


def list_input(x, N):
    for i in range(N):
        inputed = input()
        if validator(inputed):
            x.add_tail(int(inputed))
        else:
            print("Not int entered! Vector will contain 1 number less")
    return x


def rand_list(x, N):
    for i in range(N):
        x.add_tail(randint(-1000, 1000))
    return x
# Дано вектори x y z цілих чисел розмірності N.
# Якщо найбільший елемент вектора x дорівнює K і знаходиться в першій частині цього вектора,
# і якщо у векторі y немає додатніх елементів, тоді всі елементи,
# які передують його максимальному елементу замінити на їх куби.


ender = "no"
while ender == "no":
    user_choice = input("You are now in menu. Start program run? (yes/no): ")
    while user_choice != "yes" and user_choice != "no":
        print("Entered wrong answer. Reruning question")
        user_choice = input("You are now in menu. Start program run? (yes/no): ")
    if user_choice == "yes":
        x = LinkedList()
        y = LinkedList()
        z = LinkedList()
        random_choice = input("Make lists random? (yes/no): ")
        while random_choice != "yes" and random_choice != "no":
            print("Entered wrong answer. Reruning question")
            random_choice = input("Make lists random? (yes/no): ")
        if random_choice == "no":
            n = input("Enter N: ")
            if validator(n):
                N = int(n)
                print("Enter vector x:")
                x = list_input(x, N)
                print('x is')
                x.print()
                print("Enter vector y:")
                y = list_input(y, N)
                print('y is')
                y.print()
        elif random_choice == "yes":
            n = input("Enter N: ")
            if validator(n):
                N = int(n)
                x = rand_list(x, N)
                print('x is')
                x.print()
                y = rand_list(y, N)
                print('y is')
                y.print()
            # print("Enter vector z:")
            # z = list_input(z, N)
        k = input('Enter K:')
        if validator(k):
            k_in_x = x.search(k)  # щоб не було матрьошки функцій
            if x.biggest() == int(k):  # працює
                if len(k_in_x) == 1:   # працює
                    if k_in_x[0] < N // 2:    # працює
                        if y.no_positive():
                            max_in_y = y.biggest()
                            index_of_max_in_y = y.search(max_in_y)
                            if len(index_of_max_in_y) == 1:
                                y.cubing(index_of_max_in_y[0])
                            else:
                                print('More than 1 biggest number in list y')
                        else:
                            print('There are positive number(s) in list y')
                    else:
                        print('k is in the second part of list x', k_in_x[0])
                else:
                    print('There are more than one k in list x or no k in x')
            else:
                print('Biggest element in list x != k, biggest is', x.biggest())
            print('The result list y is:')
            y.print()
        ender = input("Exit program? (yes/no): ")
    elif user_choice == "no":
        ender = input("Exit program? (yes/no): ")
