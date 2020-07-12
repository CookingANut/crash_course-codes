request_toppings=['mushrooms','green peppers','extra cheese']

for request_topping in request_toppings:
    if request_topping=='green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding "+request_topping+".")

print("\nFinished making your pizza!")
