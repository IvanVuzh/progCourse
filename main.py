N = int(input('Enter N (1-100): '))
max_steps = 0
#g =[[for x in xrange(100)] for y in xrange(100)]
g=[] #define empty matrix
row=[] #Mistake position
for i in range(100): #total row is 3
    row=[] #Credits for Hassan Tariq for noticing it missing
    for j in range(100): #total column is 3
        row.append(0) #adding 0 value for each column for this row
    g.append(row)
if(N <= 1 or N >= 100):
    print('Wrong number entered! Restart the program!')
else:
    for i in range(2, N+1):
        g[i][0] = 1
        for j in range (1, i):
            g[i][0] += g[i - j][j]
        for j in range (1, i):
            g[i][j] = g[i][j - 1] - g [i - j][j]
    print('the possible amount of variations of stairs structure is', g[N][0])