N = int(input('Enter N (1-100): '))
max_steps = 0
g = []
for i in range(100):
    row = []
    for j in range(100):
        row.append(0)
    g.append(row)
#матриця для функції 100х100 заповнена нулями

#G(n,j) = (n>j ? 1 : 0) + (G(n-j-1, j+1) + G(n-j-2, j+2) + ... +G(0,n))

#оскільки n>j, то (n>j ? 1 : 0) = 1 завжди

#по формулі G(n,j) = G(n,j-1) - G(n-j,j)

if(N <= 1 or N >= 100):
    print('Wrong number entered! Restart the program!')
else:
    for i in range(2, N+1):
        g[i][0] = 1 #(n>j ? 1 : 0)
        for j in range(1, i):
            g[i][0] += g[i - j][j] #+ (G(n-j-1, j+1) + G(n-j-2, j+2) + ... +G(0,n)), оскільки j->i a i->N
        for j in range(1, i):
            g[i][j] = g[i][j - 1] - g[i - j][j] #G(n,j) = G(n,j-1) - G(n-j,j)
    print('the possible amount of variations of stairs structure is', g[N][0])
