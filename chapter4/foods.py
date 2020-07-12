my_foods=['pizza','falafel','carrot cake']


#friend_foods=my_foods[:] 复制列表


#my_foods.append('cannoil')
#friend_foods.append('ice cream')

#print("My favorite foods are:")
#print(my_foods)

#print("My friend' favorite foods are:")
#print(friend_foods)

#这个行不通
friend_foods=my_foods  #这种语法实际上是让Python将新变量friend_foods关联到包含my_foods中的列表，因此这两个变量都指向同一个列表
print(friend_foods)
my_foods.append('cannoli')
print(friend_foods)


