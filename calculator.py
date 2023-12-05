while True:
    num1 = int(input('Enter First Number: '))
    num2 = int(input('Enter Second Number: '))

    print('\nChoose operation: + | - | / | * ')
    operation = input('Please type the operation: ')

    if operation == '+':
        add = num1 + num2
        print('Result:', add)
    elif operation == '-':
        sub = num1 - num2
        print('Result:', sub)
    elif operation == '/':
        if num2 == 0:
            print('Error: Division by zero is not allowed.')
        else:
            div = num1 / num2
            print('Result:', div)
    elif operation == '*':
        mul = num1 * num2
        print('Result:', mul)
    else:
        print('Error, Please Try Again.')

    cont = input('Do you still want to do another calculation? (yes/no): ')
    if cont.lower() != 'yes':
        break
