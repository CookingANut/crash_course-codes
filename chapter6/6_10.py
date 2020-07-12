favorite_numbers={
    "lulu": [1,2,3,4,6,8,9,2,3,7,8,9,9,9,9,9,9,9,9],
    "zhenf": [1],
    "yanyan": [1,5,9,8],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print("\n"+name.title() + "'s favorite number is:" )
        for number in set(numbers):
            print(number)
    else:
        print("\n"+name.title() + "'s favorite numbers are:")
        for number in set(numbers):
            print(number)
print("\n")
#print(favorite_numbers["lulu"])