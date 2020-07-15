for i in range(1,6,1):
    for j in range(1,6,1):
        if j<=6-i:
            print('*',end='')
        else:
            print(' ',end='')
    print('\n')
