name = str(input('Enter your name:'))
grade = int(input('Enter grade:'))

if grade > 90:
    print(name, 'A')
elif grade > 80:
    print(name, 'B')
elif grade > 70:
    print(name, 'C')
elif grade > 60:
    print(name, 'D')
else:
    print('F')