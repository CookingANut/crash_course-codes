squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)    

digits=list(range(1,10))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))


#列表解析 ，要使用这种语法，首先指定一个描述性的列表名，如squares；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。
squaress=[value**2 for value in range(1,11)]
print(squaress)

#在这个示例中，表达式为value**2，接下来，编写一个循环，用于给表达式提供值，再加上右方括号。