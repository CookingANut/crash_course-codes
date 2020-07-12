#字符串就是一系列字符，在Python中，用括号括起来的都是字符串，其中的引号可以是单引号也可以是双引号

name="ada Lovelace"
print(name.title()) #以首字母大写的方式显示
print(name.upper()) #全部大写
print(name.lower()) #全部小写

#在print()语句中，方法title()出现在这个变量的后面，方法是Python可对数据执行的操作，name.title()中，name后面的句点(.)让Python对变量name执行方法title()指定的操作，每个方法后面都跟着一对括号，只是因为方法通常需要额外的信息来完成其工作
#这种信息是在括号内提供的，title()不需要额外的信息，因此它后面的括号是空的。

first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name #Python中使用+来合并字符串
print(full_name)
print("Hello, "+full_name.title()+"!")