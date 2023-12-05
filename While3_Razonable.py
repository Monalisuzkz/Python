n = 5
row = 1

while row <= n:
    column = n 
    while column >= row:
        print('*', end = ' ')
        column -= 1
    print()
    row +=1