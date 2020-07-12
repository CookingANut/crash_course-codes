#with open('pi_digits.txt') as file_object:  
#此时的 pi_digits.txt 在chapter10文件夹下                 
#如果工作区目录是python_work，则下面这样打开.txt的方式是不行的，因为只会在python_work下找
#如果工作区目录是chapter10，则这样打开是可以的



with open(r'chapter10\pi_digits.txt') as file_object:        #关键字with在不需要访问文件后将其关闭
    contents = file_object.read()
    print(contents.rstrip())

with open(r'D:\python_work\习题源代码\chapter_10\pi_digits.txt') as f:
    contents =f.read()
    print(contents.rstrip())