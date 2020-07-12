cars=['bmw','audi','toyata','subaru']
#cars.sort()
#rint(cars)
#cars.sort(reverse=True) sort()方法使得列表按照字母顺序排列，
#print(cars)

print("Here is the original list:")
print(cars)

print("Here is the sorted list:") #函数sorted()使得列表暂时改变
print(sorted(cars))

print("Here is the original list again:")
print(cars)

cars.reverse()
print(cars)
print(len(cars))
