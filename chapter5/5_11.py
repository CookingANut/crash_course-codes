numbers_list=list(range(1,10))
print(numbers_list)
print("\n")

for number in numbers_list:
    if number==1:
        print("1st")
    elif number==2:
        print("2nd")
    elif number==3:
        print("3rd")
    else:
        print(str(number)+"th")