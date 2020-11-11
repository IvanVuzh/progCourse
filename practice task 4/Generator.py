def perfect_numbers_generator():
    x = 1
    while True:
        sum = x
        current_dilnyk = 1
        while current_dilnyk != x:
            if x % current_dilnyk == 0:
                sum -= current_dilnyk
            current_dilnyk += 1
        if sum == 0:
            # print(x)
            yield x
        x += 1
