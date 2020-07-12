def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    #print(toppings)
    print("\nMaking a " + str(size) + "-inch pizza with the fowllowing toppings: ")
    for topping in toppings:
        print("- " + topping)
