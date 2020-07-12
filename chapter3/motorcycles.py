motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

#motorcycles=['honda','yamha','suzuki']
print(motorcycles)
#motorcycles[0]='ducati'

motorcycles.append('ducati') #方法append()将元素添加到列表末尾
print(motorcycles)

motorcycles.insert(0,'ducati') #方法insert()可以在列表的任何位置添加新的元素，在这里方法insert()在索引0处添加空间，并将值‘ducati’储存在这个地方，这种操作将列表中既有的每个元素都右移一个位置
print(motorcycles)


del motorcycles[0] #使用del删除了列表的第一个元素
print(motorcycles)
del motorcycles[-1]
print(motorcycles)

poped_motorcycles=motorcycles.pop() #方法pop()可以删除列表末尾的元素，并让你能够接着使用它
print(motorcycles)
print(poped_motorcycles)

motorcycles.pop(0) #pop()可以用来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可
print(motorcycles)

motorcycles=['honda','yamha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati') #不清楚要从列表中删除的值所处的位置，但是知道要删除元素的值，可以使用方法remove()
print(motorcycles)
motorcycles=['honda','yamha','suzuki','ducati']
print(motorcycles)

too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")



