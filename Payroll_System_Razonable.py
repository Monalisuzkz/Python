import sys
import time

# Payroll System
Employee = {}

# Slow print processing
def slow_na_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

# Add Employee
def AddEmployee():
    print("\n=========================")
    print("Add Employee")
    print("-----------------------------------------")
    
    EmployeeID = int(input("Employee ID: "))
    FullName = input("Full Name: ")
    Gender = input("Gender: ")
    Position = input("Position: ")
    RateDay = int(input("Rate/Day: "))
    DaysWorked = int(input("Days Worked: "))

    GrossPay = RateDay * DaysWorked
    print("Gross Pay: ", GrossPay)

    Employee[EmployeeID] = {
        "Full Name": FullName,
        "Gender": Gender,
        "Position": Position,
        "Rate/Day": RateDay,
        "Days Worked": DaysWorked,
        "Gross Pay": GrossPay
    }

    with open ("Payroll_System.txt", "a+") as file:
        for EmployeeID, Employee_info in Employee.items():
            file.write(f"Employee ID: {EmployeeID}\n")
            file.write(f"Full Name: {Employee_info['Full Name']}\n")
            file.write(f"Gender: {Employee_info['Gender']}\n")
            file.write(f"Position: {Employee_info['Position']}\n")
            file.write(f"Rate/Day: {Employee_info['Rate/Day']}\n")
            file.write(f"Days Worked: {Employee_info['Days Worked']}\n")
            file.write(f"Gross Pay: {Employee_info['Gross Pay']}\n")
            file.write("\n")

    print("\nEmployee Added!")
    slow_na_print("\nPress any key to return Menu......\n")

# Display Employee
def DisplayEmployee():
    print("\n=========================")
    print("Display Records")
    print("-----------------------------------------")
    
    try:
        with open("Payroll_System.txt", "r") as file:
            Rlines = file.readlines()

            if not Rlines:
                print("Records are Empty!")
            else:
                for i in range(0, len(Rlines), 8):
                    try:
                        EmployeeID = int(Rlines[i].split(":")[1].strip())
                        FullName = Rlines[i + 1].split(":")[1].strip()
                        Gender = Rlines[i + 2].split(":")[1].strip()
                        Position = Rlines[i + 3].split(":")[1].strip()
                        RateDay = int(Rlines[i + 4].split(":")[1].strip())
                        DaysWorked = int(Rlines[i + 5].split(":")[1].strip())
                        GrossPay = int(Rlines[i + 6].split(":")[1].strip())

                        print("Employee ID: ", EmployeeID)
                        print("Full Name: ", FullName)
                        print("Gender: ", Gender)
                        print("Position: ", Position)
                        print("Rate/Day: ", RateDay)
                        print("Days Worked: ", DaysWorked)
                        print("Gross Pay: ", GrossPay)
                        print("----------------------")

                    except (ValueError, IndexError):
                        continue

    except FileNotFoundError:
        print("File not found!")
    except IOError:
        print("Error reading the file!")
    except Exception as e:
        print("Unexpected error:", e)
        
    slow_na_print("\nPress any key to return Menu......\n")


# Clear Employee
def ClearEmployee():
    if Employee != 0:
        Employee.clear()
        print("All Records were deleted!")

        with open("Payroll_System.txt", "w") as file:
            file.write("")

        slow_na_print("\nPress any key to return Menu......\n")

    else:
        print("Records are empty!")
        slow_na_print("\nPress any key to return Menu......\n")

while True:
    print("=======================")
    print("[A]dd Employee")  
    print("[D]isplay Employee")
    print("[C]lear All")
    print("[E]xit")
    print("=======================")

    choice = input("Choice: ").upper()
    if choice.isnumeric():
        break

    match choice:

        case 'A':
            AddEmployee()

        case 'D':
            DisplayEmployee()

        case 'C':
            ClearEmployee()

        case 'E':
            sys.exit(0)