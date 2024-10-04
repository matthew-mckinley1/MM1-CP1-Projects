#Matthew McKinley Shopping List Manager
global currentList
currentList = []


def add():
    add = str(input("What item would you like to add to your shopping list?"))
    currentList.append(add)
    print(currentList)
def remove():
    remove = str(input("What item would you like to remove from your shopping list?"))
    if remove in currentList:
        currentList.remove(remove)
    else:
        print("That isn't in your list BUFFALO")
    print(currentList)
def clear():
    currentList = []
    print(currentList)

while True:
    action = input("""What would you like to do?
Enter 1 to add item
Enter 2 to remove item
Enter 3 to clear list
Enter 4 to leave the list:\n""")
    if action == "1":
        add()
    elif action == "2":
        remove()
    elif action == "3":
        clear()
    elif action == "4":
        print("Have a nice day!")
        break
    else:
        print("You typed something wrong you have been kicked out from walmart stupid")