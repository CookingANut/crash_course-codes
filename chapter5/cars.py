cars=['audi','bmw','subaru','toyota']

for car in cars:
    if cars=='bmw':               #这是我编的一个bug，原因是cars=="bmw",写错了，应该是car=="bmw"。本来cars就不是="bmw",而是cars=['audi','bmw','subaru','toyota']，所以只会运行else语句
        print(car.upper())
    else:
        print(car.title())

print(cars[1].upper())
print("\n")

for car in cars:
    if car=='bmw':    
         print(car.upper())          
    else:
        print(car.title())