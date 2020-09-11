#Згенерувати послідовність досконалих чисел розмірності n.
# Досконале число - це натуральне число, яке дорівнює сумі всіх своїх дільників, не включаючи самого себе.
# Наприклад, число 28 - досконале число, тому що 28 = 1 + 2 + 4 + 7 + 14.

N = int(input("Enter a number N: "))
ideal_numbers = []
test = 1
dilnyky_list = []
while(len(ideal_numbers) != N):
    sum = 0
    current_dilnyk = 1
    dilnyky_list.clear()
    if(N > 1):
        while(current_dilnyk != test):
            if(test % current_dilnyk == 0):
                dilnyky_list.append(current_dilnyk)
            current_dilnyk += 1
        for i in dilnyky_list:
            sum += i
        if(sum == test):
            ideal_numbers.append(test)
        test += 1

print('Number list: ', ideal_numbers)
