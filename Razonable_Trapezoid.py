def trapezoid(a,b,h):
    area = (a + b) / 2 * h
    return area

while True:

    a = float(input('Enter the length of Trapezoid (base 1):'))
    b = float(input('Enter the length of Trapezoid (base 2):'))
    h = float(input('Enter the height of Trapezoid:'))

    area = trapezoid(a,b,h)
    print('Area of the trapezoid is:', area)

    cont = input('Do you want to try again? (yes/no): ')
    if cont.lower() != 'yes':
        break