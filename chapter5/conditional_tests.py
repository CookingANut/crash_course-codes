strings=['APPLE','aPPLE','strawberry','watermelon']
numbers=[1,1,1,3,2,4,5,5.5,5.8,5.9,5.99,6,7]

#condition test 1
print(strings[0]==strings[1])
print(strings[0]==strings[2])

#condition test 2
for string in strings:
    if string.lower()=='apple':
        print("I love "+string)
    else:
        print(string+"\n")

#condition test 3
#for number in numbers:
#    if number ==1:
#        print("This number=1")
#    else:
#        print("This number!=1")

print("Are all numbers !=1?")
for number in numbers:
    if number !=1:
        print(str(number)+" is not equal 1")
    else:
        print(str(number)+" is equal 1")

#condition test 4
print("\nIn this list, the number >=5 and <6 is:")
for number in numbers:
    if number>=5 and number<6:
        print(number)

#condition test 5
print("\nIs orange not in the string?")
strings1='orange'
if strings1 not in strings:
    print("There is no orange")
else:
    print("There have orange")