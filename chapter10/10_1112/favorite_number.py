import json

filename = 'chapter10/10_1112/favorite_number.json'

try:
    with open(filename) as file_object:
        contents = json.load(file_object)
           
except FileNotFoundError:
    favorite_number = input("Please input your favorite number: ")
    with open(filename,'w') as file_object:
        json.dump(favorite_number,file_object)
else:
    print("I know your favorite number! It's " + contents)
