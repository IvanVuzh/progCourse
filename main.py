#Згенерувати послідовність досконалих чисел розмірності n.
# Досконале число - це натуральне число, яке дорівнює сумі всіх своїх дільників, не включаючи самого себе.
# Наприклад, число 28 - досконале число, тому що 28 = 1 + 2 + 4 + 7 + 14.
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
        print('N is not an integer!')
        return False


def computing(N):
    ideal_numbers = []
    test = 1
    dilnyky_list = []
    while (len(ideal_numbers) != int(N)):
        sum = 0
        current_dilnyk = 1
        dilnyky_list.clear()

        while (current_dilnyk != test):
            if (test % current_dilnyk == 0):
                dilnyky_list.append(current_dilnyk)
            current_dilnyk += 1
        for i in dilnyky_list:
            sum += i
        if (sum == test):
            ideal_numbers.append(test)
        test += 1
    return ideal_numbers


N = input("Enter a number N: ")
if(validator(N)):
    res = computing(N)
    print('Number list: ', res)
