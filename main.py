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


def array_input(x, N):
    for i in range(N):
        inputed = input()
        if(validator(inputed)):
            x.append(int(inputed))
        else:
            print("Not int entered! Vector will contain 1 number less")
    return x


def biggest_in_array(arr):
    biggest = -99999999
    for i in range(0, len(arr)):
        if(int(arr[i]) > biggest):
            biggest = int(arr[i])
    return biggest


def indexes_of_K(arr, K):
    index_arr = []
    for i in range(0, len(arr)):
        if(int(arr[i]) == int(K)):
           index_arr.append(i)
    # print('Index of k in array is', index_arr)
    return index_arr


def indexes_of_K_for_practice(arr, K):
    index_arr = []
    operation_made = 0
    print('Made an array for indexes')
    print('Start loop through array which is checking if i-element is equal to K')
    for i in range(0, len(arr)):
        operation_made += 1
        if(int(arr[i]) == int(K)):
            print('element with index', i, 'is equal to K, add it to array of indexes')
            operation_made += 1
            index_arr.append(i)
    # print('Index of k in array is', index_arr)
    print('Operations made:', operation_made)
    print('The result is:')
    return index_arr


def no_positive(arr):
    result = True
    for i in range(0, len(arr)):
        if(int(arr[i]) > 0):
            print(arr[i], 'is bigger than 0')
            result = False
    return result


def cubing_array(arr, index):
    cube_of_el = 0
    for i in range(index):
        cube_of_el = arr[i] * arr[i]
        arr[i] = cube_of_el
    return arr
# Дано вектори x y z цілих чисел розмірності N.
# Якщо найбільший елемент вектора x дорівнює K і знаходиться в першій частині цього вектора,
# і якщо у векторі y немає додатніх елементів, тоді всі елементи,
# які передують його максимальному елементу замінити на їх куби.
n = input("Enter N: ")
if(validator(n)):
    N = int(n)
    x = []
    y = []
    z = []
    inputed = 0
    print("Enter vector x:")
    x = array_input(x, N)
    print('x is', x)
    print("Enter vector y:")
    y = array_input(y, N)
    print('y is', y)
    # print("Enter vector z:")
    # z = array_input(z, N)
    k = input('Enter K:')
    if(validator(k)):
        k_in_x = indexes_of_K(x, k) # щоб не було матрьошки функцій
        if(biggest_in_array(x) == int(k)):  # працює
            if(len(k_in_x) == 1):   # працює
                if(k_in_x[0] < (N-N%2)/2):    # працює
                    if(no_positive(y)):
                        max_in_y = biggest_in_array(y)
                        index_of_max_in_y = indexes_of_K(y, max_in_y)
                        if(len(index_of_max_in_y) == 1):
                            y = cubing_array(y, index_of_max_in_y[0])
                        else:
                            print('More than 1 biggest number in array y')
                    else:
                        print('There are positive number(s) in array y')
                else:
                    print('k is in the second part of array x', k_in_x[0])
            else:
                print('There are more than one k in array x')
        else:
            print('Biggest element in array x != k', biggest_in_array(x))
        print('The result array y is:', y)
        # Доповнити завдання №2 (програмування).
        # В результуючому масиві знайти число, яке дорівнює К за допомогою бінарного пошуку.
        # Вивести позицію елемента, якщо елементів декілька, то позиції всіх елементів.
        # Вивести кількість операцій, необхідних для пошуку, та всі здійснені всі операції.
    K = input("Enter number to be found (K):")
    if(validator(K)):
        print('Checked if K is an integer')
        print(indexes_of_K_for_practice(y, K))
        print('printed result')
