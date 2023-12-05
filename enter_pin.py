print('BANK OF KYOUKAPRISM')

pin = int(input('Enter your PIN: '))

while pin != 1234:
    pin = int(input('Incorrect PIN. Enter you PIN again: '))

    if pin == 1234:
        print('PIN accepted!')