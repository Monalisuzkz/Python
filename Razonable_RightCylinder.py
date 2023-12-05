import math

def RightCylinder(radius,height):
    Area = 2 * math.pi * radius * height + 2 * math.pi * math.pow(radius, 2)
    return Area

while True:

    radius = float(input('Enter the radius of the cylinder:'))
    height = float(input('Enter the height of the cylinder:'))

    area = RightCylinder(radius,height)

    print('Area of the cylinder is:', area)

    cont = input('Do you want to try again? (yes/no): ')
    if cont.lower() != 'yes':
        break