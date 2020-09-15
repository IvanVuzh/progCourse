N = int(input('Enter N (1-100): '))
steps = 0
blocks_in_step = 1
if(N < 1 or N > 100):
    print('Wrong number entered! Restart the program!')
else:
    while(N > 0):
        if(N >= blocks_in_step):
            N -= blocks_in_step
            steps += 1
            blocks_in_step += 1
        else:
            break
    print('The possible number of steps is 1 -', steps)
