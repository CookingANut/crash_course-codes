available_toppings=['mushroom','olivers','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushroom','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+".")
    else:
        print("Sorry, we don't have "+requested_topping+".")

print("\nFinished making your pizza!")