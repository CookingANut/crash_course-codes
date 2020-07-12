#储存所点披萨的信息
pizza={
    'crust': 'thick',
    'toppings': ['mushroom','extra cheese'],
}

#概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the follwing topping:")

for topping in pizza['toppings']:
    print("\t"+topping.title())