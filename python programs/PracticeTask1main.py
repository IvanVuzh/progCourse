def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def validator(N):
    checker = RepresentsInt(N)
    if(checker):
        if(int(N) < 1 or int(N) > 100):
            print('N is not 1-100!')
            return False
        else:
            return True
    else:
        print('N is not an integer!')
        return False


def makematrix(N):
    g = []
    for i in range(N + 1):
        row = []
        for j in range(N + 1):
            row.append(0)
        g.append(row)  # матриця для функції NхN заповнена нулями
    return g


def calculate(N):
    g = makematrix(N)
    for i in range(2, N+1):
        g[i][0] = 1 #(n>j ? 1 : 0)
        for j in range(1, i):
            g[i][0] += g[i - j][j] #+ (G(n-j-1, j+1) + G(n-j-2, j+2) + ... +G(0,n)), оскільки j->i a i->N
        for j in range(1, i):
            g[i][j] = g[i][j - 1] - g[i - j][j] #G(n,j) = G(n,j-1) - G(n-j,j)
    return g[N][0]


N = input('Enter N (1-100): ')
#print(RepresentsInt(N))
if(validator(N)):
    #print('yes')
    #G(n,j) = (n>j ? 1 : 0) + (G(n-j-1, j+1) + G(n-j-2, j+2) + ... +G(0,n)) оскільки n>j, то (n>j ? 1 : 0) = 1 завжди по формулі G(n,j) = G(n,j-1) - G(n-j,j)
    result = calculate(int(N))
    print('the possible amount of variations of stairs structure is', result)
