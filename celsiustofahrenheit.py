while True:
    celsius = float(input('Enter celsisus:'))
    fahrenheit = (celsius * 1.8) + 32

    print('%0.1f degree Celsius is equal to %.0lf degree Fahrenheit' %(celsius,fahrenheit))

    cont = input('Would you still continue? (yes/no)')
    if cont.lower() != 'yes':
        break