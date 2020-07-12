message = "\nPlease enter your age: "

while True:
    info = input(message)
    if info != "quit":
        age =int(info)
        if age <3:
            print("You are free to enter.\n")
            continue
        elif 3 <= age <= 12:
            print("Your ticket price is 10 dollar.\n")
            continue
        elif age > 12:
            print("Your ticket price is 15 dollar.\n")
            continue
    else:
        break

