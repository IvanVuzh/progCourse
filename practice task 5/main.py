"""
2 стратегії
Генерувати за допомогою ітератора
Зчитувати дані з файла
Повна валідація, виконання програми не повинно бути перерване, крім того
випадку, коли я вибираю 8 пункт меню.
Меню:
    Використати стратегію 1 для вставки в список
    Вхідні дані: -
    Вихідні дані: Далі працюємо за стратегією 1, поки не змінимо

Використати стратегію 2 для вставки у список
    Генерувати дані
    Якщо вибрана стратегія 1
    Вхідні дані:
Позиція вставки
Якщо вибрана стратегія 2
Вхідні дані: Назва файла
Позиція вставки
Вихідні дані:
Згенерований список
Видалити елемент за вказаною позицією
Видалити декілька елементів в межах початкової та кінцевої позиції
Метод для роботи зі списком
Вивести список
Вихід

"""
from random import randint
from LList import *
from Iterator import *
from Context import Context
from Strategy import *
from Validation import Validators
from Validation import represents_int


for_tests = LinkedList()
for i in range(5):
    for_tests.add_tail(i)


@Validators.position_deco
def func(list, a, b, c):
    print(a+b+c)


@Validators.position_deco
def func2(list, a, b):
    print(a+b)


def test():
    for_tests2 = LinkedList()
    for i in range(5):
        for_tests2.add_tail(i)
    for_tests3 = LinkedList()
    for_tests3.append_list(for_tests2)
    for_tests3.print()


def cubing(self, n):
    current = self.head
    for i in range(n):
        new_val = current.data * current.data
        current.data = new_val
        current = current.get_next()
    return self


def list_choice_func():
    user_choice = input("Choose a list to work with (1 or 2):")
    while user_choice != "1" and user_choice != '2':
        user_choice = input("Choose a list to work with (1 or 2):")
    return int(user_choice)


def menu_ui():
    user_choice = input("You are in main menu. Possible options:\n"
                        "1 - choose first strategy (generator)\n"
                        "2 - choose second strategy (file reading)\n"
                        "3 - generate data according to chosen strategy\n"
                        "4 - delete element at chosen position\n"
                        "5 - delete a sequence of elements between chosen positions\n"
                        "6 - transform second list according to given rule\n"
                        "7 - show lists\n"
                        "8 - exit program\n"
                        "Choose your option: ")
    while not represents_int(user_choice) and (int(user_choice) < 1 or int(user_choice) > 8):
        user_choice = input("Reenter your choice")
    # print("user_choice=", user_choice)
    return user_choice


def main():
    first_list = LinkedList()
    second_list = LinkedList()
    list_dict = {1: first_list,
                 2: second_list}
    first_strat = StrategyOne()
    second_strat = StrategyTwo()
    strategy_to_use = Context()
    option = int(menu_ui())
    while option != 8:
        # print("Option is", option)
        if option == 1:
            strategy_to_use.set_strategy(first_strat)
            print("Using first strategy")

        elif option == 2:
            strategy_to_use.set_strategy(second_strat)
            print("Using second strategy")

        elif option == 3:
            # print("\noption 3\n")
            list_choice = list_choice_func()
            position = input('Enter position to insert new values: ')
            data = input('Enter the value of the parameter (amount to generate or name of file): ')
            new_list = strategy_to_use.generate(list_dict[list_choice], position, data)
            if new_list is not False:
                print('New list:')
                new_list.print()
                list_dict[list_choice] = new_list
                # print('New list:')
                # list_dict[list_choice].print()

        elif option == 4:
            list_choice = list_choice_func()
            position = input('Enter position of an element you want to delete: ')
            if list_dict[list_choice].delete_by_position(position):
                print('List with element removed at position', position, "is", list_dict[list_choice])

        elif option == 5:
            list_choice = list_choice_func()
            print("Enter the positions for numbers to be deleted between:")
            start = input("Enter starting position: ")
            end = input("Enter ending position: ")
            list_dict[list_choice].delete_between(start, end)

        elif option == 6:
            print("starting function")
            if list_dict[1].size() == list_dict[2].size():
                N = list_dict[1].size()
                k = input('Enter K:')
                if represents_int(k):
                    k_in_x = list_dict[1].search(k)  # щоб не було матрьошки функцій
                    if list_dict[1].biggest() == int(k):  # працює
                        if len(k_in_x) == 1:  # працює
                            if k_in_x[0] < N // 2:  # працює
                                if list_dict[2].no_positive():
                                    max_in_y = list_dict[2].biggest()
                                    index_of_max_in_y = list_dict[2].search(max_in_y)
                                    if len(index_of_max_in_y) == 1:
                                        list_dict[2].cubing(index_of_max_in_y[0])
                                    else:
                                        print('More than 1 biggest number in list y')
                                else:
                                    print('There are positive number(s) in list y')
                            else:
                                print('k is in the second part of list x', k_in_x[0])
                        else:
                            print('There are more than one k in list x or no k in x')
                    else:
                        print('Biggest element in list x != k, biggest is', list_dict[1].biggest())
                    print('The result list is:')
                    list_dict[2].print()
            else:
                print("lists must be same length")

        elif option == 7:
            if list_dict[1].size() != 0:
                print("First list:")
                list_dict[1].print()
            else:
                print("First list is empty")
            if list_dict[2].size() != 0:
                print("Second list:")
                list_dict[2].print()
            else:
                print("Second list is empty")

        elif option == 8:
            break

        option = int(menu_ui())


# func(for_tests, 1, 2, 3)
# func2(for_tests, 6, 2)
main()
# test()
