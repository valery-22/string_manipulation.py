listNames = []

def printList():
    print()
for i in listNames:
    print(i)
    print()

while True:
    firstName = input("First Name: ").strip().capitalize()
    lastName = input("Last Name: ").strip().capitalize()
    fullName = f"{firstName} {lastName}"
    if fullName not in listNames:  
        listNames.append(fullName)
        printList()
    else:
        print("ERROR:duplicate name")