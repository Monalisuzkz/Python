
def Dictionary():
    return {}

info = {}

while True:

    id = int(input("Enter your ID: "))
    if id == 0:
        break

    name = input("Enter your Name: ")
    if name.isdigit():
        break

    info[id] = name

    print(info)