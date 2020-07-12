def toppings(*topins):
    print("Your ordered pizza is including below toppings:")
    for topin in topins:
        print("- " + topin.title())

toppings("cheese")
toppings("banaba","ham")
toppings("hot-gog", 'green peppers','tomato')
