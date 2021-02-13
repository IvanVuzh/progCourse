from Validation import Validators
import copy


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
        # found = False
        while current:
            if current.get_data() == int(data):
                index_arr.append(it)
                # found = True
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
        while last.next_node:
            last = last.next_node
        last.next_node = new_node

    def get_first(self):
        return self.head.get_data()

    def get_last(self):
        if self.size() != 0:
            last = self.head
            while last.get_next():
                last = last.get_next()
            return last.get_data()

    def get_last_node(self):
        if self.size() != 0:
            last = self.head
            while last.next_node:
                last = last.next_node
            return last

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

    @Validators.position_deco
    def delete_by_position(self, posi):
        pos = int(posi)
        if pos == 1:
            self.head = self.head.get_next()
        elif pos == self.size():
            if self.head.next_node is None:
                self.head = None
            else:
                traversal = self.head.next_node
                while traversal.next_node.next_node:
                    traversal = traversal.next_node
                traversal.next_node = None
        else:
            current = self.head.get_next()
            iter = 1
            previous = self.head
            while current:
                if iter == pos:
                    previous.set_next(current.get_next())
                else:
                    previous = current
                    current = current.get_next()
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    @Validators.position_deco
    def delete_between(self, posi1, posi2):
        pos1 = int(posi1)
        pos2 = int(posi2)
        to_do = pos2 - pos1
        while to_do != -1:
            self.delete_by_position(pos1)
            to_do -= 1
        return True

    def append_list(self, linked_list):
        if self.size() > 0:
            last = self.head
            while last.next_node:
                # print("list append while")
                last = last.next_node
            last.next_node = linked_list.head
        elif self.size() == 0:
            # print("elif")
            # print(linked_list.head.get_data())
            self.head = linked_list.head
