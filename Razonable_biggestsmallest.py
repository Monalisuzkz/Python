def check_biggest_number():

    if first_num > second_num and  first_num > third_num:
        print("\nThe Biggest Number is ", first_num)
        
    elif second_num > first_num and second_num > third_num:
        print("\nThe Biggest Number is ", second_num)
        
    else:
        print("\nThe Biggest Number is ", third_num)

def check_smallest_number():

    if first_num < second_num and  first_num < third_num:
        print("\nThe Smallest Number is ", first_num)
        
    elif second_num < first_num and second_num < third_num:
        print("\nThe Smallest Number is ", second_num)
        
    else:
        print("\nThe Smallest Number is ", third_num)
    
while True:
    try:
        first_num = int(input("Enter First Number: "))
        second_num = int(input("Enter Second Number: "))
        third_num = int(input("Enter Third Number: "))
    except ValueError:
        print("Error entered value. Please enter a value again.")
        continue

    check_biggest_number()
    check_smallest_number()

    cont = input('\nDo you want to check a number again? (yes/no): ')
    if cont.lower() != 'yes':
        break
