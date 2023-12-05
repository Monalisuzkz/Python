import pymysql
import getpass
import hashlib
import os

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Establish a connection to the MySQL database
connection = pymysql.connect(
    host='localhost',
    user='root',
    database='prac_db'
)

def register_user():
    clearscreen()
    cursor = connection.cursor()

# User registration
    email = input("Enter email: ")
#getpass method to hide your password while you input in the terminal
    password = getpass.getpass("Enter Password: ")
#hashlib method is to hide your password to the mysql table you entered
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM register WHERE Email=%s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Your email entered is already in use. Please use a different email.")
    else:
        cursor.execute("INSERT INTO register (Email, Password) VALUES (%s, %s)", (email, password_hash))
        connection.commit()
        clearscreen()
        print("Registered Successfully!!!")

def login_user():
    clearscreen()
    cursor = connection.cursor()
# User login
    email = input("Enter email: ")
#getpass method to hide your password while you input in the terminal
    password = getpass.getpass("Enter Password: ")
#hashlib method is to hide your password to the mysql table you entered
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM register WHERE Email=%s AND Password=%s", (email, password_hash))
    user = cursor.fetchone()

    if user:
        clearscreen()
        print("Login Successful!")
    else:
        clearscreen()
        print("Login Failed. Please check your email and password.")
        reset_password = input("Forgot your password? Enter 'yes' to reset your password: ")
        if reset_password.lower() == "yes":
            reset_user_password(email)

#change new password if you forget your current password
def reset_user_password(email):
    clearscreen()
    cursor = connection.cursor()
#getpass method to hide your password while you input in the terminal
    new_password = getpass.getpass("Enter a new password: ")
#hashlib method is to hide your password to the mysql table you entered
    password_hash = hashlib.sha256(new_password.encode()).hexdigest()
    
    cursor.execute("UPDATE register SET Password=%s WHERE Email=%s", (password_hash, email))
    connection.commit()
    
    clearscreen()
    print("Password Reset Successfully!")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            clearscreen()
            break
        else:
            clearscreen()
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

connection.close()

