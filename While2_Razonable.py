n = 5
row = 1
add = 1
while row <= n:
    column = 1 
    while column <= row:
        print('*', end = ' ')
        column += 1
        add += 1
    print()
    row +=1