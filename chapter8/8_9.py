def show_magicians(magicians):
    for magician in magicians:
        print("Magician name: " + magician.title())




#1           这里解释下#1和#2为什么会有完全不同的结果
def make_great(magicians):   #注意这里的magicians是一个列表，定义为该函数接受一个列表
    great_magicians = []
    while magicians:
        add_great = "The Great " + magicians.pop()
        great_magicians.append(add_great)         #while循环结束后 给出的列表magicians为[]，并且great_magicians为最后需要的列表
    
    
    #magicians = great_magicians[:]          #问题的关键就出在这里， 这里的magicians为一个定义名称，不是之前函数定义的列表，这里只是把目标列表的副本赋值给了这个定义的magicians这个变量, 原来的列表还是为[]，所以一定要弄清楚函数所接受形参的类型是什么
    for great_magician in great_magicians:      
        magicians.append(great_magician)          #这里的magicians才是原来的magicians，通过不断地把目标列表里的元素添加进原来的列表来完成目的

magicians = ["lulu","zhenf","yanyan"]

show_magicians(magicians)
make_great(magicians)
#print(magicians)
show_magicians(magicians)


#2
#magicians = ["lulu","zhenf","yanyan"]            来看看#2，此时的magicians是一个列表
#great_magicians = []
#while magicians:
#     add_great = "The Great " + magicians.pop()
#     great_magicians.append(add_great)             经过while循环后，magician变为[], great_magicians是目标列表

#magicians = great_magicians[:]                    结果在这里，把great_magicians的副本给了magicians，此时的magicians是另外一个列表了,原来magicians代表的列表依然存在，还是[],只是没有名字代表它了而已
#print(magicians)                                  所以总结就是，在函数定义里的magicians永远都是那个原来的列表，而在正常代码里面，magicians代表的东西随时可以被改变

