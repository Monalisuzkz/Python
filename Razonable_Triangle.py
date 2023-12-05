def Triangle(Base,Weight):
    Area = (Base * Weight) * 0.5
    return Area

while True:

    Base = float(input('Enter the Base length of the Triangle:'))
    Weight = float(input('Enter the Weight of the Triangle:'))

    Area = Triangle(Base,Weight)

    print('Area of Triangle is:', Area)

    cont = input('Do you want to try again? (yes/no): ')
    if cont.lower() != 'yes':
        break