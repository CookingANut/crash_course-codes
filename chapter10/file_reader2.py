filename = 'chapter10\pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())                   #print自带一个回车，txt文档内每行结束自己也带了一个回车，用rstrip()消除