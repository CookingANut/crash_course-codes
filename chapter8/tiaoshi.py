magicians = ["lulu","zhenf","yanyan"] 
great_magicians = []
while magicians:
     add_great = "The Great " + magicians.pop()
     great_magicians.append(add_great)
magicians = great_magicians[:]

print(magicians)