def show_magicians(magicians):
    for magician in magicians:
        print("Magician name: " + magician.title())

def make_great(magicians):  
    great_magicians = []
    while magicians:
        add_great = "The Great " + magicians.pop()
        great_magicians.append(add_great)         
    
    for great_magician in great_magicians:      
        magicians.append(great_magician)
    
    return magicians      

magicians1 = ["lulu","zhenf","yanyan"]
magicians2 = make_great(magicians1[:])

show_magicians(magicians1)
show_magicians(magicians2)