filename = 'chapter10\learning_python.txt'
#with open(filename) as file_object:                                 #出现只print了一次的原因就在于
    #1                                                               #忽略了迭代时指针的移动，一个文件是一个可迭代的对象，当我们读完整个file_object的时候，指针的状态指向了最后一行，在第二次迭代 
    #read1 = file_object.read()                                      #就是例如左边进行for循环进行第二次迭代，此时指针已经指向最后一行，就是一个空列表，对空的文件迭代就是什么都没有
    #x = read1.replace('Python','C')                                 #解决办法就是在第二次迭代前加上file_object.seek(0),将file_object复位到第一位
    #print(x)
    #2
    #for line in file_object:
        #print(line.strip())
    #3
    #read3 = file_object.readlines()

#for line in read3:
    #print(line)

file_object = open(filename)

read1 = file_object.read()
x = read1.replace('Python','C')
print(x)

file_object.seek(0)
for line in file_object:
    print(line.strip())

file_object.seek(0)
read3 = file_object.readlines()
for line in read3:
    print(line.strip())

file_object.close()




    