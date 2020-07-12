themostloved_pizza=["pepperoni pizza","strawberry pizza","blueberry pizza" ]
friend_pizzas=themostloved_pizza[:]

friend_pizzas.append('pineapple pizza')

print("My favorite pizzas are:")
for pizza in themostloved_pizza:
    print(pizza)



print("\nMy friend's favorite pizzs are:")
for pizza in friend_pizzas:
    print(pizza)

#for onepizzy in themostloved_pizza:
    #print("I like "+onepizzy+".")

#print("\nFirst is "+themostloved_pizza[0]+".")    
#print("Second is "+themostloved_pizza[1]+".")   
#print("Third is "+themostloved_pizza[-1]+".") 
#print("I really love pizza.")