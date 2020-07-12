filename = 'chapter10\siddhartha.txt'
#filename = r'chapter10\test1.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.lower().count('the'))