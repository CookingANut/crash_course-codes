guests_numbers = input("How many guests do you have to eat? ")
guests_numbers = int(guests_numbers)

if guests_numbers >=8:
    print("Sorry, there is no seat for eating temporaryly.")
elif guests_numbers>=1:
    print("OK, there have spare seats for you to eat.")
else:
    print("Are you kidding?")