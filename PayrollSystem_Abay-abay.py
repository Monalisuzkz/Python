Employee = {}

def Add_Employee():
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

    with open ("PayrollSystem.txt", "a+") as file:
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
    print("\nPress any key to return Menu......\n")

def Display_Employee():
    print("\n=========================")
    print("Display Records")
    print("-----------------------------------------")
    
    try:
        with open("PayrollSystem.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print("Records are Empty!")
            else:
                for i in range(0, len(lines), 8):
                    try:
                        EmployeeID = int(lines[i].split(":")[1].strip())
                        FullName = lines[i + 1].split(":")[1].strip()
                        Gender = lines[i + 2].split(":")[1].strip()
                        Position = lines[i + 3].split(":")[1].strip()
                        RateDay = int(lines[i + 4].split(":")[1].strip())
                        DaysWorked = int(lines[i + 5].split(":")[1].strip())
                        GrossPay = int(lines[i + 6].split(":")[1].strip())

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
        
    print("\nPress any key to return Menu......\n")

def Clear_Employee():
    if Employee != 0:
        Employee.clear()
        print("All Records were deleted!")

        with open("Payroll_System.txt", "w") as file:
            file.write("")

        print("\nPress any key to return Menu......\n")

    else:
        print("Records are empty!")
        print("\nPress any key to return Menu......\n")

while True:
    print("=======================")
    print("[A]dd Employee")  
    print("[D]isplay Employee")
    print("[C]lear All")
    print("[E]xit")
    print("=======================")

    choice = input("Choice: ").upper()

    match choice:
        case 'A':
            Add_Employee()
        case 'D':
            Display_Employee()
        case 'C':
            Clear_Employee()
        case 'E':
            break