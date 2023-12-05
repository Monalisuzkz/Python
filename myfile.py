#Reading text File
xyz = open("record.txt","r")
print(xyz.read())
xyz.close()

#Writing text File
student=open("record.txt","a+")

Sid=input("Student ID: ")
fname=input("Full Name: ")

student.write(f"Student ID: {Sid} \n")
student.write(f"Full Name: {fname} \n")

#display record
print(student.read())
student.close()
