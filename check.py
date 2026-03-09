import re
import string

def check_password_length():
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RESET = "\033[0m]"


    if len(password)<=5:
        print(RED + 'The Password is Weak 🔴' + RESET)
    elif len(password)>=6 and len(password)<=10:
        print(YELLOW + 'The Password is Medium 🟡' + RESET)
    else:
        print(GREEN + 'The Password is Strong 🟢' + RESET)
    return

def check_password_complexity():
    pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).+$"

    if re.match(pattern, password):
        print('The password has at least 1 uppercase letter, 1 number, and 1 special character ✅')
        return True
    return False

def give_hints_password():
    punctuation_password = set(string.punctuation)
    if(any(char.isupper() for char in password) == False):
        print('HINT: Add at least 1 uppercase letter 🅰️')
    if(any(char.isdigit() for char in password) == False):
        print('HINT: Add at least 1 number 🔢')
    if(any(char in punctuation_password for char in password) == False):
        print('HINT: Add at least 1 special character ❗')

while True: 
    try:
        print('Welcome to the Password Strength Checker!')
        password = input('Enter your password: ')
        password_length = len(password)
        print(f'Password Length: {password_length} characters')
        
    except ValueError:
        print('Error entered value. Please enter a value again.')
        continue

    check_password_length()
    check_password_complexity()
    give_hints_password()

    cont = input('\nDo you want to check your password again? (yes/no): ')
    if cont.lower() != 'yes':
        break

