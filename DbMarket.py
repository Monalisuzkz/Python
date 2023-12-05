import time
import sys
import mysql.connector
from datetime import datetime

# Menu List
menu_list = {
    1: {'SaladName': 'Kani Salad', 'price': 6.75},
    2: {'SaladName': 'Spicy Bean Sprout Salad', 'price': 7.89},
    3: {'SaladName': 'Broccolini Gomaae', 'price': 9.50},
    4: {'SaladName': 'Apple Walnut Salad', 'price': 5.59},
    5: {'SaladName': 'Honey Sesame Shirataki Noodles Salad', 'price': 10.89}
}

# Slow print processing
def slow_na_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

# Customer Information / "CustomerInfo" sa DATABASE
def CustomerInformation():
    while True:
        try:
            Name = input('Enter your Name: ')
            ContactNumber = input('Enter your Contact Number: ')
            return Name, ContactNumber
        except ValueError:
            print("Invalid input. Please enter valid information.")

# Function para sa MYSQL Insert Into CustomerInfo
def InsertCustomerInfo(Name, ContactNumber):
    try:
        conn = mysql.connector.connect(host='localhost', port="3306", user="root", password="", database="PythonMarket")
        cursor = conn.cursor()

        insert_query = "INSERT INTO customerinfo (Name, ContactNumber) VALUES (%s, %s)"
        CustomerInfodata = (Name, ContactNumber)

        cursor.execute(insert_query, CustomerInfodata)
        conn.commit()

        # Get the last inserted CustomerID
        customer_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return customer_id

    except mysql.connector.Error as e:
        print(f'Error inserting customer information: {e}')
        return None

# Function para sa MYSQL Insert Into Orders
def InsertCustomerOrders(CustomerID, order):
    try:
        conn = mysql.connector.connect(host='localhost', port="3306", user="root", password="", database="PythonMarket")
        cursor = conn.cursor()

        for selected_meal in order:
            SaladName = selected_meal["SaladName"]
            Quantity = selected_meal["quantity"]
            Price = selected_meal["price"]

            insert_query = "INSERT INTO customerorders (CustomerID, SaladName, Quantity, Price) VALUES (%s, %s, %s, %s)"
            CustomerOrdersdata = (CustomerID, SaladName, Quantity, Price)

            cursor.execute(insert_query, CustomerOrdersdata)
            conn.commit()

            # Get the last inserted OrderID
            order_id = cursor.lastrowid

            
        cursor.close()
        conn.close()

        return order_id
    
    except mysql.connector.Error as e:
        print(f'Error inserting customer order: {e}')
        return None

# Function para sa MYSQL Insert Into Purchases
def InsertCustomerPurchases(OrderID, CustomerID, TotalAmount, PaymentMethod, Address):
    try:
        conn = mysql.connector.connect(host='localhost', port="3306", user="root", password="", database="PythonMarket")
        cursor = conn.cursor()

        insert_query = "INSERT INTO customerpurchases (OrderID, CustomerID, TotalAmount, PaymentMethod, Address) VALUES (%s, %s, %s, %s, %s)"
        CustomerPurchasesData = (OrderID, CustomerID, TotalAmount, PaymentMethod, Address)

        cursor.execute(insert_query, CustomerPurchasesData)
        conn.commit()
        
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print(f'Error inserting customer purchase: {e}')
        return None
# Print Purchase Receipt here:
def CustomerPurchasesReceipt(purchase_data):
    print("\n-------- Purchase Receipt --------")
    print("Purchase Date: ", purchase_data["PurchaseDate"])
    print("Name: ", purchase_data["Name"])

    # Iterate through each item in the order and format it
    for item in purchase_data["Order"]:
        formatted_item = f"{item['quantity']} {item['SaladName']} - ${item['price'] * item['quantity']:.2f}"
        print("Order:", formatted_item)
        
    print("Contact Number: ", purchase_data["Contact Number"])
    print("Total Amount: $", purchase_data["TotalAmount"])
    print("Payment Method: ", purchase_data["PaymentMethod"])
    print("Delivery Address: ", purchase_data["Address"])
    print("---------------------------------")

# Main
while True:
    print('------Welcome to Skeweroo Healthy Meal Shop------')
    print('')
    print('Menu:')

    order = []  # List to store selected items
    total_price = 0.0

    while True:
        for key, item in menu_list.items():
            print(f'[{key}] {item["SaladName"]} - ${item["price"]:.2f}')

        OrderChoice = int(input("Please enter your Choice here: "))

        if OrderChoice == 0:
            break

        elif OrderChoice in menu_list:
            selected_meal = menu_list[OrderChoice]
            quantity = int(input(f'Enter the quantity for {selected_meal["SaladName"]}: '))

            if quantity > 0:
                selected_meal['quantity'] = quantity
                order.append(selected_meal)
                total_price += selected_meal['price'] * quantity

                add_more = input("Do you want to add more? (yes/no): ")
                if add_more.lower() != 'yes':
                    break
            else:
                print('Invalid quantity. Please enter a valid quantity.')

    if not order:
        print('No items in your order. Please start over.')
        continue

    # Calculate total price
    total_price = sum(item["price"] * item["quantity"] for item in order)

    # Display selected items
    print('\nYour order:')
    for item in order:
        print(f'{item["quantity"]} {item["SaladName"]} - ${item["price"] * item["quantity"]:.2f}')
    print(f'Total Price: ${total_price:.2f}')

    slow_na_print('Processing...')
    print('\nPlease fill your information here.\n')
    Name, ContactNumber = CustomerInformation()

    while True:
        PaymentMethod = input('Enter Payment Method: ')
        if PaymentMethod:
            break
        else:
            print('Payment Method cannot be empty.')

    while True:
        Address = input('Enter your Address: ')
        if Address:
            break
        else:
            print('Address cannot be empty.')

    print("\nThank you for your order!")

    # Insert customer information and get the CustomerID
    CustomerID = InsertCustomerInfo(Name, ContactNumber)

    if CustomerID is not None:
        # Insert orders and get the OrderID
        OrderID = InsertCustomerOrders(CustomerID, order)

        if OrderID is not None:
            # It will insert the purchase information here:
            purchase_data = InsertCustomerPurchases(OrderID, CustomerID, total_price, PaymentMethod, Address)

        if OrderID is not None:
            # It will insert the purchase information here:
            purchase_data = {
                "PurchaseDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": Name,
                "Order": order,
                "Contact Number": ContactNumber,
                "TotalAmount": total_price,
                "PaymentMethod": PaymentMethod,
                "Address": Address
            }

            receipt = CustomerPurchasesReceipt(purchase_data)

    else:
        print("Error inserting customer purchase.")

    cont = input('\nDo you want to do another purchase? (yes/no): ')
    if cont.lower() != 'yes':
        break
