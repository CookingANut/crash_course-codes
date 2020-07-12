dream_places_lists = {}

active = True 

while active:
    name = input("Input your name: \n(input 'quit' to finish)")
    
    if  name != 'quit':
        dream_places = input("What is your dream place to go?")
        dream_places_lists[name] = dream_places
    
    else:
        active = False

#print(dream_places_lists)
for names, dreamplaces in dream_places_lists.items():
    print(names.title() + "'s dream place is " + dreamplaces + ".")

