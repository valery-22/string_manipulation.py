
while True:
    whatToEat = input("What do you fancy for dinner? ")
    if whatToEat.lower().strip()  =="pasta": 
        print("Get out the pasta maker.")
    elif whatToEat.lower().strip()  == "tacos":
        print("Let's do Taco Tuesday!")
    else: 
        print("Go search the fridge.")