def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def validator(N):
    checker = RepresentsInt(N)
    if(checker):
        if(int(N) < 1 or int(N) % 2 == 1):
            print('N is not an even positive number!')
            return False
        else:
            return True
    else:
        print('N is not an integer!')
        return False


def print_matrix(arr):
    for a in arr:
        ln = ""
        for i in a:
            ln += str(i) + " "
        print(ln)


def make_matrix(N):
    if int(N) == 1:
        for i in range(int(N)):
            print(i, end=" ")
            print()
    elif int(N) > 1:
        matrix = [[0] * int(N) for j in range(int(N))]
        matrix_odd_row = list(range(1, int(N) + 1))
        matrix_even_row = list(range(int(N), 0, -1))
        for i in range(int(N)):
            if i % 2 == 1:
                matrix[i] = matrix_odd_row
            else:
                matrix[i] = matrix_even_row
    print_matrix(matrix)


ender = "no"
while ender == "no":
    user_choice = input("You are now in menu. Start program run? (yes/no): ")

    while user_choice != "yes" and user_choice != "no":
        print("Entered wrong answer. Reruning question")
        user_choice = input("You are now in menu. Start program run? (yes/no): ")

    if user_choice == "yes":
        N = input("Enter n: ")
        if validator(N):
            make_matrix(N)
        ender = input("Exit program? (yes/no): ")
    elif user_choice == "no":
        ender = input("Exit program? (yes/no): ")
