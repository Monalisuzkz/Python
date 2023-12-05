mylist = []

while True:

    print("\n[1]Add","\n[2]Remove","\n[3]Change","\n[4]Display","\n[5]Exit")
    choice = int(input("Choose you want to do:"))

    if choice == 1:
        additem = input("Add an Item here:")
        mylist.append(additem)
        print("Item added!")
        print(mylist)

    elif choice == 2:
        delindex = int(input("Enter an Index to remove: "))
        del mylist[delindex]
        print("Item removed!")
        print(mylist)

    elif choice == 3:
        changeindex = int(input("Enter an Index to change: "))
        change = input("Enter new item here to change: ")
        mylist[changeindex] = change
        print("Item changed!")
        print(mylist)

    elif choice == 4:
        print(mylist)

    else:
        break