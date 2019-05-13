items = ["T-shirt","Sweater"]
x = True
while x:
    request = input("welcome to our shop, what do you want (C,R,U,D)? :")
    request = request.upper()
    if request == "R":
        print("Our items:", end ="")
        print(*items, sep=",")
    elif request == "C":
        new_item = input("Enter new item:")
        items.append(new_item)
        print("Our items:", end ="")
        print(*items, sep=",")
    elif request == "U":
        update_position = int(input("Update position?"))
        new__item = input("New item?")
        items[update_position-1] = new__item
        print("Our items:", end ="")
        print(*items, sep=",")
    elif request == "D":
        delete_position = int(input("Delete position?"))
        del items[delete_position-1]
        print("Our items:", end ="")
        print(*items, sep=",")
    else:
        print("Unknown request")
        x = False