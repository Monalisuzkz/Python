import mysql.connector

conn = mysql.connector.connect(hose='localhost',port="3306",user="root",password="",database="pythonhealthymealmarket")
cursor = conn.cursor()

selectquery = "select * from customerinfo"
cursor.execute()
records = cursor.fetchall()
print("Numbers of Customers in this market", cursor.rowcount)

for row in records:
    print("Customer ID", row[0])
    print("Name", row[1])
    print("Contact Number", row[2])
    print("Address", row[3])
    print()

    cursor.close()
    conn.close()
    
