import math
def Circle(radius):
    Area = math.pi * radius * radius
    return Area

while True:

    radius = float(input('Enter the radius of the circle:'))

    Area = Circle(radius)
    print('Area of Circle is:', Area)

    cont = input('Do you want to try again? (yes/no): ')
    if cont.lower() != 'yes':
        break