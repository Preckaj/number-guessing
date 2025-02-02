import random 
while True:
    print("Hello, Welcome to the Guessing Game!")
    print("What range do you want to pick?")
    print("1. 1-5")
    print("2. 1-10")
    print("3. 1-20")
    print("4. 1-50")
    print("5. 1-100")
    print("6. Exit")
    answer = input()
    if answer == "1":
        target = random.randint(1, 5)
        while True:
            try:
                number = int(input("Pick a number 1 - 5! "))
                break
            except ValueError:
                print("Invalid Number, try again.")
        if number == target:
            print("You won!")
        else:
            print(f" The number was {target}, You lost.")
    elif answer == "2":
        target = random.randint(1, 10)
        while True:
            try:
                number = int(input("Pick a number 1 - 10! "))
                break
            except ValueError:
                print("Invalid Number, try again.")
        if number == target:
            print("You won!")
        else:
            print(f" The number was {target}, You lost.")
    elif answer == "3":
        target = random.randint(1, 20)
        while True:
            try:
                number = int(input("Pick a number 1 - 20! "))
                break
            except ValueError:
                print("Invalid Number, try again.")
        if number == target:
            print("You won!")
        else:
            print(f" The number was {target}, You lost.")
    elif answer == "4":
        target = random.randint(1, 50)
        while True:
            try:
                number = int(input("Pick a number 1 - 50! "))
                break
            except ValueError:
                print("Invalid Number, try again.")
        if number == target:
            print("You won!")
        else:
            print(f" The number was {target}, You lost.")
    elif answer == "5":
        target = random.randint(1, 100)
        while True:
            try:
                number = int(input("Pick a number 1 - 100! "))
                break
            except ValueError:
                print("Invalid Number, try again.")
        if number == target:
            print("You won!")
        else:
            print(f" The number was {target}, You lost.")
    elif answer == "6":
        exit()
    else:
        print("Invalid Value, try again.")