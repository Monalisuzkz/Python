import sys
import time

# Student Management System
StudentInfo = {}

# Slow print processing
def slow_na_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

# Read Records from File
def read_records_from_file():
    existing_records = {}
    with open("Student_Record.txt", "r") as file:
        lines = file.readlines()

        for i in range(0, len(lines), 3):
            try:
                student_id = int(lines[i].split(":")[1].strip())
                full_name = lines[i + 1].split(":")[1].strip()

                existing_records[student_id] = {'Full Name': full_name}
            except (ValueError, IndexError):
                continue

    return existing_records

# Add Student
def AddStudent():
    print("\n=========================")
    print("Add Record")
    print("-----------------------------------------")

    AddStudentID = int(input("Student ID: "))
    FullName = input("Full Name: ")

    StudentInfo[AddStudentID] = {"Full Name": FullName}

    with open("Student_Record.txt", "a+") as file:
        file.write(f"Student ID: {AddStudentID}\n")
        file.write(f"Full Name: {FullName}\n")
        file.write("\n")

    print("Student Added!")
    print("========================")
    slow_na_print("Press any key to continue......\n")

# Remove Student
def RemoveStudent():
    print("\n=========================")
    print("Remove Record")
    print("-----------------------------------------")

    existing_records = read_records_from_file()

    if not existing_records:
        print("No student records to remove")
    else:
        RemoveStudentID = int(input("Student ID: "))
        found = False

        if RemoveStudentID in existing_records:
            del existing_records[RemoveStudentID]
            found = True
            print(f"Student Record with ID {RemoveStudentID} deleted!")

            with open("Student_Record.txt", "w") as file:
                for student_id, student_info in existing_records.items():
                    file.write(f"Student ID: {student_id}\n")
                    file.write(f"Full Name: {student_info['Full Name']}\n")
                    file.write("\n")

        if not found:
            print(f"No student found with ID {RemoveStudentID}.")

    print("========================")
    slow_na_print("Press any key to continue......\n")

# Update Student
def UpdateStudent():
    print("\n=========================")
    print("Update Record")
    print("-----------------------------------------")

    existing_records = read_records_from_file()

    if not existing_records:
        print("No student records to update")
    else:
        UpdateStudentID = int(input("Student ID: "))
        UpdateFullName = input("Full Name: ")
        found = False

        if UpdateStudentID in existing_records:
            existing_records[UpdateStudentID]['Full Name'] = UpdateFullName
            found = True
            print(f"Student Record with ID {UpdateStudentID} updated!")

            with open("Student_Record.txt", "w") as file:
                for student_id, student_info in existing_records.items():
                    file.write(f"Student ID: {student_id}\n")
                    file.write(f"Full Name: {student_info['Full Name']}\n")
                    file.write("\n")

        if not found:
            print(f"No student found with ID {UpdateStudentID}.")

    print("========================")
    slow_na_print("Press any key to continue......\n")

# Display Student
def DisplayStudent():
    print("\n=========================")
    print("Display Records")
    print("-----------------------------------------")

    existing_records = read_records_from_file()

    if not existing_records:
        print("Records are Empty!")
    else:
        for student_id, student_info in existing_records.items():
            print("Student ID: ", student_id)
            print("Full Name: ", student_info['Full Name'])
            print("----------------------")

    slow_na_print("\nPress any key to continue......\n")

# Main Menu of the Program
while True:
    print("=======================")
    print("[A]dd Student")
    print("[R]emove Student")
    print("[U]pdate Student")
    print("[D]isplay Student")
    print("[E]xit")
    print("=======================")

    choice = input("Choice: ").upper()
    if choice.isnumeric():
        break

    match choice:
        case 'A':
            AddStudent()
        case 'R':
            RemoveStudent()
        case 'U':
            UpdateStudent()
        case 'D':
            DisplayStudent()
        case 'E':
            sys.exit(0)
