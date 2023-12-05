def Rectangle(length,width):
    area = length * width 
    return area
while True:

    length = float(input('Enter the length of Rectangle:')) #Enter the length
    width = float(input('Enter the width of Rectangle:')) #Enter the width

    area = Rectangle(length,width)
    print('Area of Rectangle is:', area)

    conti = input('Do you want to try again? (yes/no): ')
    if conti.lower() != 'yes':
        break


