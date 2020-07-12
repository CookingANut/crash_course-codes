file_name = r'chapter10\guest_book.txt'
message = 'Please enter your name.\n'
print("Enter 'q' to quit program.")

with open(file_name,'a') as file_object:
    while True:
        guest_name = input(message)
        if guest_name != 'q':
            print('Welcome, ' + guest_name + '!\n')
            file_object.write(guest_name + '\n')
        else:
            break