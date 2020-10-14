# Доповнити завдання № 1 з програмування,
# написавши власні ітератор та генератор для генерації даних для списку завдання.
# Програма повинна мати меню для вибору способу генерації списку з можливістю виходу з меню.
# Розділити програму на декілька файлів, кожен з яких відповідає за свою структурну одиницю.
from Generator import perfect_numbers_generator
from IteratorClassFile import Iterator


def menu_ui():
    print("### You are now in menu ###")
    print("Choose option:")
    print("1 - generate a list by Generator")
    print("2 - enter a list by Iterator")
    print("3 - exit program")
    to_return = input()
    if represents_int(to_return):
        return to_return
    else:
        to_return = input("Reenter correct number(1-3)!")


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def main():
    # Згенерувати послідовність досконалих чисел розмірності n.
    # Досконале число - це натуральне число, яке дорівнює сумі всіх своїх дільників, не включаючи самого себе.
    # Наприклад, число 28 - досконале число, тому що 28 = 1 + 2 + 4 + 7 + 14.
    while True:
        list_of_perfect_numbers = []
        user_choice = menu_ui()
        # print("Your choice is " + user_choice)
        while int(user_choice) != 1 and int(user_choice) != 2 and int(user_choice) != 3:
            user_choice = input("Reenter correct number(1-3)!")
        if int(user_choice) == 1 or int(user_choice) == 2:
            # print("Your choice is 1 or 2 " + user_choice)
            N = input("Enter a number N: ")
            while not represents_int(N) or int(N) < 0:
                N = input("Wrong input! Reenter positive integer")
            n = int(N)

            if int(user_choice) == 1:
                for i in perfect_numbers_generator():
                    list_of_perfect_numbers.append(i)
                    if len(list_of_perfect_numbers) == n:
                        break
            if int(user_choice) == 2:
                iterator_result = Iterator(n)
                for i in iterator_result:
                    list_of_perfect_numbers.append(i)
            print("List of perfect numbers:")
            # for i in range(n):
            print(list_of_perfect_numbers)
        if int(user_choice) == 3:
            print("Have a nice day! Goodbye!")
            break


main()
