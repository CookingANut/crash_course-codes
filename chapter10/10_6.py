print('Please input 2 numbers, then I will plus them.')
print("Enter 'q' to quit.")
while True:
    first_number = input('Input the first number: ')
    if first_number == 'q':
        break
    second_number = input('Input the second number: ')
    if second_number == 'q':
        break

    try:
        value = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter number not text.")
    else:
        print("Result: " + str(value))