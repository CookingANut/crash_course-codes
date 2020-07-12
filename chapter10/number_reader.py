import json

filename = r'chapter10\numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)