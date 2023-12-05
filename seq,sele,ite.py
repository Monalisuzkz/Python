#Sequence
def sum_of_two():
    num1 = int(input("Enter first num:"))
    num2 = int(input("Enter second num:"))
    
    sum = float(num1) + float(num2)
    print('The sum is =', sum)

#Selection
def if_elif_example():
    Age = int(input("Enter your age:"))

    if Age >= 60:
        print('Senior Discount')
    elif 18 <= Age < 60:
        print('No Discount')
    else:
        print('Junior Discount')

#Iteration
def fibo_numbers():
   #The first two values
    x = 0
    y = 1
    iteration = 0
    
    length = int(input("Enter a size of length:"))

#Condition to check if the length has a valid input
    if length <= 0:
        print("Please provide a number greater than zero")
    elif length == 1:
        print("This Fibonacci sequence has {} element".format(length), ":")
        print(x)
    else:
        print("This Fibonacci sequence has {} elements".format(length), ":")
    
    while (iteration < length):
        print(x, end = ',')
        z = x + y
        # MOdify values
        x = y 
        y = z
        iteration += 1

while True:
    print("\nPlease Choose: [1] Sequence [2] Selection [3] Iteration")
    choice = int(input("Enter here:")) 

    if choice == 1:
        print("Sequence: The sum of two")
        sum_of_two()
    elif choice == 2:
        print("Selection: Discount bus")
        if_elif_example()
    elif choice == 3:
        print("The fibonacci numbers")
        fibo_numbers()
    else:
        print("Please enter a valid choice")

    cont = input('Do you want to continue? (yes/no): ')
    if cont.lower() != 'yes':
        break